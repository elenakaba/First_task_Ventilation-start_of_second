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
        x = input("please insert the smaller of the two building dimensions:")
        if confirm_valid_input(x):
            break
    while True:
        y = input("please insert the bigger of the two building dimensions:")

        """Optimization purposes"""

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
    def __init__(self, building_dimensions):
        self.width_height = building_dimensions

        self.horizontal_overlap_distance = 52
        self.vertical_overlap_distance = 45
        self.ventilated_area_radius = 30

        self.building = Building(self.width_height)

        plot_shape_graphics(self.building.rectangle)
        self.rows = calculate_vents_per_wall_length((
                self.width_height[1] + self.ventilated_area_radius), self.vertical_overlap_distance)
        self.odd_row_vents = calculate_vents_per_wall_length(
            self.width_height[0], self.horizontal_overlap_distance)
        self.even_row_vents = calculate_vents_per_wall_length((
                self.width_height[0] + self.horizontal_overlap_distance // 2), self.horizontal_overlap_distance)
        self.vents = 0
        self.non_vents = 0

    def increment_vents(self, coordinate_x, coordinate_y):
        if check_if_vent(self.building.rectangle, (coordinate_x, coordinate_y)):
            self.vents += 1
        else:
            self.non_vents += 1

    def distribute_vents(self):
        horizontal_offset = False
        for row in range(self.rows):
            horizontal_offset = not horizontal_offset
            if horizontal_offset:
                number_of_vents = self.odd_row_vents
                offset = self.horizontal_overlap_distance // 2
            else:
                number_of_vents = self.even_row_vents
                offset = 0
            for index in range(number_of_vents):
                coordinate_x = self.horizontal_overlap_distance * index + offset
                if coordinate_x > self.width_height[0]:
                    coordinate_x = self.width_height[0]
                coordinate_y = self.vertical_overlap_distance * row
                if coordinate_y > self.width_height[1]:
                    coordinate_y = self.width_height[1]
                create_and_plot_vent(coordinate_x, coordinate_y)
                self.increment_vents(coordinate_x, coordinate_y)


if __name__ == '__main__':
    x, y = user_input()
    calc = VentCalculator((x, y))
    calc.distribute_vents()
    print("There are " + str(calc.vents) + " ventilation openings, each equal to 40EUR.")
    print("There are " + str(calc.non_vents - 1) + " windows, each equal to 10EUR.")
    print("Assuming that there is only one door/gate/ in the building equal to 5EUR.")
    print("The total sum=", calc.vents * 40 + (calc.non_vents - 1) * 10 + 5, "EUR")
    plt.show()
