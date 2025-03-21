from typing import Any, override
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtOpenGLWidgets import QOpenGLWidget
import skia


class SkiaWidget(QOpenGLWidget):
    def __init__(self, parent: Any = None) -> None:
        super().__init__(parent)
        # Optionally configure the surface format
        self.gr_context = None
        self.sk_surface = None

    @override
    def initializeGL(self, /) -> None:
        # Called once to initialize OpenGL; create a Skia GPU context.
        # Make sure you have set up an appropriate context in your system.
        self.gr_context = skia.GrDirectContext.MakeGL()
        self.create_skia_surface()

    def create_skia_surface(self):
        # Get the dimensions of the widget
        width, height = self.width(), self.height()
        # Retrieve framebuffer info from QOpenGLWidget
        fb_id = self.defaultFramebufferObject()
        # Create Skia render target info (this API may differ based on skia-python version)
        fb_info = skia.GrGLFramebufferInfo(fb_id, skia.kRGBA_8888_ColorType)
        print(fb_info)
        image_info = skia.ImageInfo.MakeN32Premul(width, height)
        backend_render_target = skia.GrBackendRenderTarget(width, height, 0, 0, fb_info)
        print(backend_render_target)
        # Create a Skia surface from the backend render target
        self.sk_surface = skia.Surface.MakeFromBackendRenderTarget(
            self.gr_context,
            backend_render_target,
            skia.kBottomLeft_GrSurfaceOrigin,
            skia.kRGBA_8888_ColorType,
            None,
            None,
        )
        if self.sk_surface is None:
            print("Failed to create Skia surface!")
            exit(1)

    @override
    def paintGL(self):
        # If the surface hasn't been created or the widget was resized, recreate it.
        if (
            self.sk_surface is None
            or self.width() != self.sk_surface.width()
            or self.height() != self.sk_surface.height()
        ):
            self.create_skia_surface()
        canvas = self.sk_surface.getCanvas()
        # Clear the canvas
        canvas.clear(skia.ColorWHITE)
        # Draw a simple Bezier curve as an example
        paint = skia.Paint(
            Color=skia.ColorBLUE,
            AntiAlias=True,
            StrokeWidth=4,
            Style=skia.Paint.kStroke_Style,
        )
        path = skia.Path()
        path.moveTo(50, self.height() // 2)
        path.cubicTo(
            150, 50, 250, self.height() - 50, self.width() - 50, self.height() // 2
        )
        canvas.drawPath(path, paint)
        # Flush Skia commands so they get executed on the GPU.
        self.sk_surface.flushAndSubmit()


if __name__ == "__main__":
    # surface = skia.Surface(640, 480)
    # with surface as canvas:
    #     paint = skia.Paint()
    #     paint.setAntiAlias(True)
    #     paint.setColor(skia.ColorWHITE)
    #     canvas.drawPaint(paint)
    #     paint.setColor(skia.ColorRED)
    #     canvas.drawRect(skia.Rect(100, 100, 200, 200), paint)
    # image = surface.makeImageSnapshot()
    # image.save("output.png", skia.kPNG)
    app = QApplication([])
    label = QLabel("Hello World!")
    label.show()
    skia_widget = SkiaWidget()
    skia_widget.show()
    _ = app.exec()
