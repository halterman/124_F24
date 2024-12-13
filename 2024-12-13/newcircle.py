from circle import Circle
from point import Point

class NewCircle(Circle):
    def __init__(self, c: Point, r: float) -> None:
        super().__init__(c, r)

    def __repr__(self) -> str:
        return f'({self.center.x}. {self.center.y}) {self.radius}'
