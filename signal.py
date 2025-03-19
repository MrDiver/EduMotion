
from typing import Callable, Self, Any
from log_symbols import symbols
from logging import Logger


class Signal:
    counter = 0
    currentSignal: "Signal | None" = None
    logger = None
    def __init__(self: Self, func, name: str=""):
        if Signal.logger is None:
            Signal.logger = Logger(name="Signal", level="DEBUG")
        Signal.logger.info(f"{symbols.LogSymbols.INFO} Creating Signal {name}")
        self.func = func
        self.value = None
        self.dirty = True
        self.name = name + str(self.counter)
        self.subscribers = set()
        Signal.counter += 1

    def makedirty(self) -> None:
        self.dirty = True
        for s in self.subscribers:
            s.makedirty()

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        if args and len(args) == 1:
            self.set(args[0])
            return self.value
        oldSignal = Signal.currentSignal
        if oldSignal is not None:
            self.subscribers.add(oldSignal)

        Signal.currentSignal = self
        if self.dirty:
            self.value = self.func(*args, **kwds)
            self.dirty = False
        
        Signal.currentSignal = oldSignal
        return self.value

    def set(self, funcOrVal: Any) -> None:
        self.makedirty()
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
        else:
            self.func = lambda: funcOrVal
            self.dirty = False
            self.value = funcOrVal


    def __repr__(self) -> str:
        return f"{self.name}{'_d' if self.dirty else ''}{self.subscribers if self.subscribers else ''}"



__all__ = ["Signal"]
