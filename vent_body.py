from shapely.geometry import Polygon

OFFSET = 0.5  # half the length of the side of a 1 meter by 1 meter square


class VentBody:
    def __init__(self, x, y):
        rectangle_point_start = (abs(x - OFFSET), abs(y - OFFSET))
        rectangle_point_one = (abs(x + OFFSET), abs(y - OFFSET))
        rectangle_point_two = (abs(x + OFFSET), abs(y + OFFSET))
        rectangle_point_three = (abs(x - OFFSET), abs(y + OFFSET))
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
    building = Building(rectangle_dimensions=rectangle_dimensions)
    print(building)
    print(building.calculate_area())
