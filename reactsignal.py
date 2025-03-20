from typing import Any, Callable, Self, cast, overload, override
from weakref import WeakSet
import weakref
from logger_config import logger
from enum import Enum
from collections import deque


class SDMState(Enum):
    REGISTERING = 0
    EXECUTING = 1
    RECOMPUTING = 2


class Signal:
    state: SDMState = SDMState.EXECUTING
    current: "Signal | None" = None
    counter: int = 0

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

        # Checking if func is a function and then setting it as source
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
            self.value = None
            self.is_source = False
        else:
            self.func = lambda x=funcOrVal: x
            self.value = funcOrVal
            self.is_source = True
        Signal.counter += 1

        # Lambdas wihout any defaults are also considered sources
        sources = [x for x in self.func.__defaults__ or [] if isinstance(x, Signal)]
        if len(sources) == 0:
            self.is_source = True

        # Handling Signals
        self.dirty: bool = True
        self.subscribers: WeakSet[Signal] = (
            WeakSet()
        )  # Immediate Subscribers filled by calling subscribe
        self.sources: WeakSet[Signal] = WeakSet(
            sources
        )  # Immediate Sources for debugging

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
        if Signal.state == SDMState.EXECUTING:
            logger.debug(f"Executing {self}")
            if self.isDirty():
                self.scheduleRecompute()
        if Signal.state == SDMState.RECOMPUTING:
            logger.debug(f"Called as Dep {self}")
        return self.value

    def scheduleRecompute(self) -> None:
        Signal.state = SDMState.RECOMPUTING
        queue = deque([cast(Signal, self)])
        sorted_signals: list[Signal] = []

        while queue:
            signal = queue.popleft()
            sorted_signals.append(signal)
            queue.extend(source for source in signal.sources if source.dirty)

        for signal in reversed(sorted_signals):
            signal.recompute()

        Signal.state = SDMState.EXECUTING

    def recompute(self) -> None:
        self.value = self.func()
        self.dirty = False

    def isDirty(self) -> bool:
        return self.dirty

    def markDirty(self, recurse=True) -> None:
        self.dirty = True
        if not recurse:
            return
        queue = deque(self.subscribers)
        while queue:
            signal = queue.popleft()
            signal.markDirty(False)
            queue.extend(signal.subscribers)

    def set(self, funcOrVal: Callable[[], Any] | Any) -> None:
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
        else:
            self.value = funcOrVal
            self.func = lambda: funcOrVal
        self.markDirty()

    def deconstruct(self):
        for source in self.sources:
            source.unsubscribe(cast(Signal, self))

    @override
    def __repr__(self) -> str:
        return f"{self.name}"


__all__ = ["Signal"]
