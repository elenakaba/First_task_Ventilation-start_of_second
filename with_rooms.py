import math
import matplotlib.pyplot as plt
from shapely.geometry import Point

from ventilation_coverage import VentilationCoverage
from vent_body import VentBody
from building import Building


def plot_shape_graphics(shape):
    _x, _y = shape.exterior.xy
    plt.plot(_x, _y)


def create_and_plot_vent(_x, _y):
    vent = VentBody(_x, _y)
    vent_radius = VentilationCoverage(_x, _y)
    plot_shape_graphics(vent.rectangle)
    plot_shape_graphics(vent_radius.show_as_circle())


def calculate_vents_per_wall_length(distance, step):
    vents = math.ceil((abs(distance) / abs(step)))
    return vents


def user_input():
    print("Hello Mr. Lagzdiņš, \n please insert how big your building you wish to be: \n (in meters)")

    while True:
        x = input("please insert the width of the building:")
        if confirm_valid_input(x):
            break
    while True:
        y = input("please insert the length of the building:")
        if confirm_valid_input(y):
            break
    return int(x), int(y)


def confirm_valid_input(input_string):
    if input_string.isdigit():
        return True
    print("Please only insert digits")
    return False


def check_if_vent(polygon, coordinate_tuple):
    if polygon.contains(Point(coordinate_tuple)):
        return True
    return False


class VentCalculator:
    def __init__(self, building_dimensions=user_input()):

        self.width_height = building_dimensions
        self.room_width = 25
        self.vertical_overlap_distance = 54
        self.ventilated_area_radius = 30
        self.building = Building(self.width_height)

        if building_dimensions[0] < building_dimensions[1]:
            self.height = building_dimensions[0]
            self.building_width = building_dimensions[1]
        else:
            self.height = building_dimensions[1]
            self.building_width = building_dimensions[0]

        self.number_of_rooms = math.ceil(self.building_width / self.room_width)

        self.rows = calculate_vents_per_wall_length((
                self.height + self.ventilated_area_radius), self.vertical_overlap_distance)
        self.vents = 0
        self.non_vents = 0

    def iterate_rooms(self):
        for i in range(self.number_of_rooms):
            if i == range(self.number_of_rooms)[-1]:
                room_width = self.building_width % 25 if self.building_width % 25 != 0 else 25
            else:
                room_width = self.room_width
            horizontal_offset = i * 25
            room = Building((room_width, self.height), horizontal_offset)
            plot_shape_graphics(room.rectangle)
            self.distribute_vents(horizontal_offset)

    def distribute_vents(self, horizontal_offset):
        for row in range(self.rows):
            coordinate_x = horizontal_offset + 12.5
            if coordinate_x > self.building_width:
                coordinate_x = self.building_width
            coordinate_y = self.vertical_overlap_distance * row
            if coordinate_y > self.height:
                coordinate_y = self.height
            create_and_plot_vent(coordinate_x, coordinate_y)
            self.increment_vents(coordinate_x, coordinate_y)

    def increment_vents(self, coordinate_x, coordinate_y):
        if check_if_vent(self.building.rectangle, (coordinate_x, coordinate_y)):
            self.vents += 1
        else:
            self.non_vents += 1


if __name__ == '__main__':
    calc = VentCalculator()
    calc.iterate_rooms()
    print("There are " + str(calc.vents) + " vents.")
    print("And " + str(calc.non_vents) + " windows or doors.")
    print("Total sum =", calc.vents * 40 + calc.non_vents * 10, "EUR")
    plt.show()

