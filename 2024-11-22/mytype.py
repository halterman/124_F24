class MyType:
    def __init__(self) -> None:
        self.x = 0
    def inc(self) -> None:
        self.x += 1
    def get(self) -> int:
        return self.x
