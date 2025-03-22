import re
from typing import Any, Callable, Self, cast, overload, override, Iterable
from weakref import WeakSet
from enum import Enum
from collections import deque
import weakref


class SDMState(Enum):
    REGISTERING = 0
    EXECUTING = 1
    RECOMPUTING = 2


class Signal:
    state: SDMState = SDMState.EXECUTING
    current: "Signal | None" = None
    counter: int = 0
    __slots__ = [
        "id",
        "name",
        "value",
        "func",
        "is_source",
        "dirty",
        "subscribers",
        "sources",
        "__weakref__",
    ]

    def __init__(
        self: Self,
        funcOrVal: Callable[[], Any] | Any,
        name: str = "",
    ):
        self.id: int = Signal.counter
        self.name: str = name + str(self.counter)
        self.value: Any | None
        self.func: Callable[[], Any]
        self.is_source: bool

        Signal.counter += 1

        # Handling Signals
        self.dirty: bool = True
        self.subscribers: WeakSet[Signal] = (
            WeakSet()
        )  # Immediate Subscribers filled by calling subscribe
        self.sources: WeakSet[Signal] = WeakSet()  # Immediate Sources for debugging
        weakref.finalize(self, self.deconstruct)

    def set(self, funcOrVal: Callable[[], Any] | Any) -> None:
        # Checking if func is a function and then setting it as source
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
            self.value = None
            self.is_source = False
        else:
            self.func = lambda x=funcOrVal: x
            self.value = funcOrVal
            self.is_source = True

        self.markDirty()
        # Lambdas wihout any defaults are also considered sources
        # Flatten list if there are nested lists
        if self.func.__defaults__ is None:
            self.is_source = True
            return

        self.sources.clear()
        for source in self.func.__defaults__:
            if isinstance(source, Iterable):
                self.sources.update(source)
            elif isinstance(source, Signal):
                self.sources.add(source)

        for source in self.sources:
            source.subscribe(cast(Signal, self))

    def subscribe(self, signal: "Signal") -> None:
        self.subscribers.add(signal)

    def unsubscribe(self, signal: "Signal") -> None:
        self.subscribers.remove(signal)

    @overload
    def __call__(self, *arg: Callable[[], Any]) -> None: ...

    @overload
    def __call__(self, *arg: Any) -> None: ...

    def __call__(self, *arg: Callable[[], Any] | Any | None) -> Any | None:
        if arg:
            self.set(arg[0])
            return

        if Signal.state == SDMState.EXECUTING:
            if self.dirty:
                self.scheduleRecompute()
        return self.value

    def scheduleRecompute(self) -> None:
        Signal.state = SDMState.RECOMPUTING
        queue = deque([self])
        sorted_signals: list[Signal] = []

        while queue:
            signal = queue.popleft()
            sorted_signals.append(signal)
            queue.extend(source for source in signal.sources if source.dirty)  # type: ignore

        for signal in reversed(sorted_signals):
            signal.recompute()

        Signal.state = SDMState.EXECUTING

    def recompute(self) -> None:
        self.value = self.func()
        self.dirty = False

    def markDirty(self, recurse=True) -> None:
        if self.dirty:
            return
        self.dirty = True
        if not recurse:
            return
        queue = deque([x for x in self.subscribers if not x.dirty])
        while queue:
            signal = queue.popleft()
            if signal.dirty:
                continue
            signal.markDirty(False)
            queue.extend(signal.subscribers)

    def deconstruct(self):
        for source in self.sources:
            source.unsubscribe(cast(Signal, self))

    @override
    def __repr__(self) -> str:
        return f"{self.name}"


__all__ = ["Signal"]
