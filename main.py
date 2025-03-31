import sys
import time
import debugpy
from typing import Any, Callable, Generator, override, TypedDict, Unpack
import weakref
import skia
import glfw
import contextlib
from OpenGL import GL
from sig import tween
from sig.animatable import Animatable
from dataclasses import dataclass
import numpy as np


class GlfwWindow:
    def __init__(self, width: int = 1920, height: int = 1080):
        if not glfw.init():
            raise RuntimeError("Failed to initialize GLFW")
        glfw.window_hint(glfw.STENCIL_BITS, 8)
        self.window: Any = glfw.create_window(
            width, height, "Skia GLFW Example", None, None
        )
        glfw.make_context_current(self.window)
        _ = weakref.finalize(self, self.close)

    def clear_screen(self):
        GL.glClearColor(1, 1, 1, 1)
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

    def swap_buffers(self):
        glfw.swap_buffers(self.window)
        glfw.poll_events()

    def should_close(self):
        return glfw.window_should_close(self.window)

    def close(self):
        glfw.destroy_window(self.window)
        glfw.terminate()


class SkiaSurface(GlfwWindow):
    def __init__(self, width: int = 1920, height: int = 1080):
        super().__init__(width, height)
        self.context: skia.GrDirectContext | None = skia.GrDirectContext.MakeGL()
        if self.context is None:
            raise RuntimeError("Failed to create GrDirectContext")
        width, height = glfw.get_framebuffer_size(self.window)
        backend_render_target = skia.GrBackendRenderTarget(
            width,
            height,
            0,
            0,
            skia.GrGLFramebufferInfo(0, GL.GL_RGBA8),
        )
        assert backend_render_target.isValid(), "Failed to create GrBackendRenderTarget"
        self.surface = skia.Surface.MakeFromBackendRenderTarget(
            self.context,
            backend_render_target,
            skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType,
            skia.ColorSpace.MakeSRGB(),
        )
        assert self.surface is not None, "Failed to create Skia surface"

    @override
    def close(self):
        super().close()
        self.context.abandonContext()


class Renderer:
    def __init__(self):
        self.gl = SkiaSurface()
        self.surface = self.gl.surface
        self.window = self.gl.window
        self.gen = tween.tween(1, lambda x: x, tween.easeInOutQuad)

    def draw(self, animatable: Animatable, canvas: skia.Canvas):
        paint = skia.Paint()
        paint.setColor(skia.ColorRED)
        canvas.drawCircle(animatable.x(), animatable.y(), 50, paint)

    def draw_frame(self, list_of_animatables: list[Animatable]):
        self.gl.clear_screen()
        with self.surface as canvas:
            for animatable in list_of_animatables:
                self.draw(animatable, canvas)
        self.surface.flushAndSubmit()
        self.gl.swap_buffers()


class TimeEvent:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.value: Any = None


class AnimationKwargs(TypedDict):
    mapping: Callable[[float], float]


class Animation:
    def __init__(self, mapping: Callable[[float], float] = tween.linear) -> None:
        self._start: TimeEvent | float | None = None
        self._end: TimeEvent | float | None = None
        self.name: str = "Generic"
        self.mapping: Callable[[float], float] = mapping

    def begin(self): ...
    def animate(self, dt: float): ...
    def finalize(self): ...

    def get_start(self) -> float:
        assert self._start is not None
        return self._start.value if isinstance(self._start, TimeEvent) else self._start

    def set_start(self, start: float | TimeEvent):
        self._start = start

    def get_end(self) -> float:
        assert self._end is not None
        return self._end.value if isinstance(self._end, TimeEvent) else self._end

    def set_end(self, end: float | TimeEvent):
        self._end = end

    def __iter__(self):
        frames = (self.get_end() - self.get_start()) * tween.FPS
        self.begin()
        for frame in np.linspace(0, 1, int(frames)):
            yield self.animate(self.mapping(frame))
        self.finalize()


class Shift(Animation):
    def __init__(
        self, animatable: Animatable, shift: float, **kwargs: Unpack[AnimationKwargs]
    ) -> None:
        super().__init__(**kwargs)
        self.name: str = "Shift"
        self.animatable: weakref.ref = weakref.ref(animatable)
        self.shift: float = shift
        self.start_x: float = 0

    @override
    def begin(self):
        if (animatable := self.animatable()) is not None:
            self.start_x = animatable.x()
        # Maybe Locking for Signal

    @override
    def animate(self, dt: float):
        if (animatable := self.animatable()) is not None:
            animatable.x(self.start_x + self.shift * dt)

    @override
    def finalize(self): ...


class Timeline:
    def __init__(self):
        self.scenes: list[Scene] = []
        self.animations: list[Animation] = []
        self.time_events: list[TimeEvent] = []


# TODO: TimeEvents can be created by passing a string to the start_time parameter of the play function in the scene


class Scene:
    def __init__(self):
        self.animatables: set[Animatable] = set()

    def add(self, animatable: Animatable):
        self.animatables.add(animatable)

    def remove(self, animatable: Animatable):
        self.animatables.remove(animatable)


if __name__ == "__main__":
    # debugpy.listen(5678)
    # debugpy.wait_for_client()

    renderer = Renderer()
    animatable = Animatable()
    animatable.y(512)
    animatable2 = Animatable()
    animatable2.x(lambda x=animatable.x: x() + 100)
    animatable2.y(700)

    # TODO: This should still use durations and internally use start
    animation = Shift(animatable, 512, mapping=tween.easeInOutQuad)
    animation.set_start(0)
    animation.set_end(3)
    for x in animation:
        # TODO: Figure out how to use delta times for live display or figure out how to make consistent framerate
        start = time.time()
        renderer.draw_frame([animatable, animatable2])
        end = time.time()
        duration = end - start
        if 1 / tween.FPS - duration > 0:
            time.sleep(1 / tween.FPS - duration)
    animation = tween.tween(
        3, lambda n: animatable.y((1 - n) * 512), tween.easeInOutQuad
    )
    for y in animation:
        renderer.draw_frame([animatable, animatable2])
