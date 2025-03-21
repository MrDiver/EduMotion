from reactsignal import Signal


class Animatable:
    def __init__(self):
        self.x = Signal(lambda: 0, "x")
        self.y = Signal(lambda: 0, "y")
        self.width = Signal(lambda: 0, "width")
        self._left = Signal(lambda: self.x() - self.width(), "left")
        self.alpha = Signal(lambda: 0, "alpha")
        self.scale = Signal(lambda: 1, "scale")
        self.dirty = True

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self.x(lambda: self.x() - self.width() + value())
