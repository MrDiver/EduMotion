from logging import Logger
from typing import Any, Callable, Deque, Self
from weakref import WeakSet, ref
from logger_config import logger
from enum import Enum
from collections import deque


class Signal:
    counter = 0
    currentSignal: "Signal | None" = None

    def __init__(self: Self, funcOrVal, name: str = ""):
        self.id = Signal.counter
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
            self.value = None
            self.isComputation = True
        else:
            self.func = lambda: funcOrVal
            self.isComputation = False
            self.value = funcOrVal
        self.name = name + str(self.counter)
        Signal.counter += 1
        SDM.registerSignal(self)

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        logger.debug(f"Calling signal {self}")
        if SDM.context == SDMState.REGISTERING:
            SDM.signalDependent(self)
        if SDM.context == SDMState.EXECUTING:
            if SDM.isDirty(self):
                SDM.scheduleRecompute(self)
        return self.value

    def set(self, funcOrVal: Any) -> None:
        if isinstance(funcOrVal, Callable):
            self.func = funcOrVal
            SDM.markDirty(self)
        else:
            self.value = funcOrVal
            self.func = lambda: funcOrVal
            SDM.markClean(self)

    def recompute(self) -> None:
        if SDM.isDirty(self):
            self.value = self.func()
        else:
            logger.warning(f"Signal {self} recomputed without being dirty")

    def __repr__(self) -> str:
        return f"{self.name}"

    def __del__(self) -> None:
        SDM.unregisterSignal(self)


class SignalNode:
    def __init__(self, signal: Signal) -> None:
        self.dirty = True
        self.signal = ref(signal)
        self.subscribers: WeakSet[SignalNode] = WeakSet()
        self.dependents: WeakSet[SignalNode] = WeakSet()

    def __repr__(self) -> str:
        if self.signal() is not None:
            return f"N({self.signal().name})"
        return "N(None)"


class SDMState(Enum):
    REGISTERING = 0
    EXECUTING = 1
    RECOMPUTING = 2


# Signal Dependency Manager
class SDM:
    graph = {}
    noSignals = 0
    context = SDMState.REGISTERING
    currentNode: SignalNode = None

    @staticmethod
    def registerSignal(signal: Signal) -> None:
        logger.debug(f"Registering signal {signal}")
        SDM.noSignals += 1
        node = SignalNode(signal)
        SDM.graph[signal.id] = node
        SDM.context = SDMState.REGISTERING
        SDM.currentNode = node
        try:
            signal.func()
        except Exception as e:
            ...
        SDM.context = SDMState.EXECUTING

    @staticmethod
    def signalDependent(signal: Signal) -> None:
        if SDM.context == SDMState.REGISTERING:
            # logger.debug(f"Signal {signal} is dependent on {SDM.currentNode}")
            SDM.currentNode.dependents.add(SDM.graph[signal.id])
            signalNode = SDM.graph[signal.id]
            signalNode.subscribers.add(SDM.currentNode)

    @staticmethod
    def scheduleRecompute(signal: Signal) -> None:
        SDM.context = SDMState.RECOMPUTING
        logger.debug(f"Schedule recomputation for {signal}")
        # Build queue of dirty dependencies
        rootNode = SDM.graph[signal.id]
        queue: Deque[SignalNode] = deque([rootNode])
        sorted_signals: list[SignalNode] = [rootNode]
        while queue:
            current = queue.popleft()
            for dependent in current.dependents:
                if dependent.dirty:
                    sorted_signals.append(dependent)
                    queue.append(dependent)

        for node in reversed(sorted_signals):
            node.signal().recompute()
            node.dirty = False
        SDM.context = SDMState.EXECUTING

    @staticmethod
    def markDirty(signal: Signal) -> None:
        # logger.debug(f"Marking signal {signal} dirty")
        signalNode = SDM.graph[signal.id]
        signalNode.dirty = True
        dirty_queue = deque()
        dirty_queue.append(signalNode)
        while dirty_queue:
            current = dirty_queue.popleft()
            for subscriber in current.subscribers:
                if not subscriber.dirty:
                    subscriber.dirty = True
                    dirty_queue.append(subscriber)

    @staticmethod
    def isDirty(signal: Signal) -> bool:
        return SDM.graph[signal.id].dirty

    @staticmethod
    def markClean(signal: Signal):
        SDM.graph[signal.id].dirty = False

    @staticmethod
    def unregisterSignal(signal: Signal):
        # logger.debug(f"Unregistering signal {signal}")
        SDM.noSignals -= 1
        SDM.graph.pop(signal.id)


__all__ = ["Signal", "SDM"]
