import matplotlib.pyplot as plt
from shapely.geometry import Polygon


COORDINATE_SYSTEM_ORIGIN = 0.0


class Building:
    def __init__(self, rectangle_dimensions, offset=0):
        origin = COORDINATE_SYSTEM_ORIGIN + offset
        rectangle_width = rectangle_dimensions[0]
        rectangle_height = rectangle_dimensions[1]
        rectangle_point_start = (origin, COORDINATE_SYSTEM_ORIGIN)
        rectangle_point_one = (origin + rectangle_width, COORDINATE_SYSTEM_ORIGIN)
        rectangle_point_two = (origin + rectangle_width, rectangle_height)
        rectangle_point_three = (origin, rectangle_height)
        rectangle_coordinates = (
            rectangle_point_start,
            rectangle_point_one,
            rectangle_point_two,
            rectangle_point_three,
            rectangle_point_start
        )

        self.rectangle = Polygon(rectangle_coordinates)

    def calculate_area(self):
        return self.rectangle.area


if __name__ == '__main__':
    width_height = (100.0, 80.0)
    building = Building(width_height)
    print(building)
    print(building.calculate_area())

