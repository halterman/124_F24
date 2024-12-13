class Widget:
    def __init__(self, v: int) -> None:
        self.value = v
        self.qual = 10

    def double(self):
        self.value *= 2

    def get(self) -> int:
        return self.value - self.qual


class Gadget(Widget):
    def __init__(self) -> None:
        super().__init__(100)

    def get(self) -> int:
        return super().get() + self.qual
