from __future__ import annotations
from graphics import Window, Line, Point


class Cell:
    def __init__(self, window: Window | None = None) -> None:
        # TODO: see if this could work as a 0b1111 or 0xF instead. four bits and one value feels cozy. maybe for a diff language rewrite
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.__window = window
        self.visited = False

    def update_corners(self) -> None:
        # TODO: refactor to calculate different polgyon that work within the box
        self.__top_left = (self.__x1, self.__y1)
        self.__top_right = (self.__x2, self.__y1)
        self.__bottom_left = (self.__x1, self.__y2)
        self.__bottom_right = (self.__x2, self.__y2)

    def draw(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.update_corners()

        def draw_if_exists(
            wall_exists: bool, first_coords: tuple, second_coords: tuple
        ) -> None:
            line = Line(
                Point(first_coords[0], first_coords[1]),
                Point(second_coords[0], second_coords[1]),
            )
            if wall_exists:
                self.__window.draw_line(line)
            else:
                self.__window.draw_line(line, fill_color="white")

        draw_if_exists(self.has_left_wall, self.__top_left, self.__bottom_left)
        draw_if_exists(self.has_top_wall, self.__top_left, self.__top_right)
        draw_if_exists(self.has_right_wall, self.__top_right, self.__bottom_right)
        draw_if_exists(self.has_bottom_wall, self.__bottom_left, self.__bottom_right)

    def draw_move(self, to_cell: Cell, undo: bool = False) -> None:
        # print("are we hitting here???")
        if any([self.__x1, self.__y1, self.__x2, self.__y2]) is None:
            raise AttributeError("cell lacks coordinates")

        # def get_middle(first_coord: int, second_coord: int) -> int:
        #     return abs(second_coord - first_coord) // 2
        #
        # def get_center(cell: Cell) -> Point:
        #     middle_x = get_middle(cell.__x1, cell.__x2)
        #     middle_y = get_middle(cell.__y1, cell.__y2)
        #     return Point(middle_x, middle_y)

        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1
        # self_center = get_center(self)
        # destination_center = get_center(to_cell)
        # print(f"from {self_center} to {destination_center}")
        fill_color = "red" if not undo else "gray"
        # print(fill_color)
        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__window.draw_line(line, fill_color)
        # self.__window.draw_line(Line(self_center, destination_center), fill_color)
