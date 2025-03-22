from sig.reactsignal import Signal


class Animatable:
    def __init__(self):
        self.x = Signal( 0, "x")
        self.y = Signal( 0, "y")
        self.color = Signal(lambda: (0, 0, 0, 255), "color")
