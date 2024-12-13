from point import Point
import math

class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.center = center
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius * self.radius

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

