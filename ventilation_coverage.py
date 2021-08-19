import math
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt


class VentilationCoverage:

    def __init__(self, x, y, l=30):
        c = [[x + math.cos(math.radians(angle)) * l, y + math.sin(math.radians(angle)) * l] for angle in range(90, 450, 60)]
        self.hexagon = Polygon(c)
        self.side = l
        self.center = (x, y)
        self.circle = Point(self.center).buffer(self.side)

    def calculate_hexagonal_area(self):
        return self.hexagon.area

    def calculate_circular_area(self):
        return self.circle.area

    def show_as_hexagon(self):
        return self.hexagon

    def show_as_circle(self):
        return self.circle


if __name__ == '__main__':
    hexagon = VentilationCoverage(0.0, 0.0)
    hexagon_two = VentilationCoverage(52.0, 0.0)
    hexagon_three = VentilationCoverage(26.0, 45.0)
    hexagon_four = VentilationCoverage(26.0, -45.0)
    print(hexagon.show_as_hexagon())
    print(hexagon.calculate_hexagonal_area())
    print(hexagon.show_as_circle())
    print(hexagon.calculate_circular_area())
    x, y = hexagon.hexagon.exterior.xy
    plt.plot(x, y)
    x, y = hexagon_two.hexagon.exterior.xy
    plt.plot(x, y)
    x, y = hexagon_three.hexagon.exterior.xy
    plt.plot(x, y)
    x, y = hexagon_four.hexagon.exterior.xy
    plt.plot(x, y)
    plt.show()
