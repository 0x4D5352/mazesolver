from time import sleep
from random import seed, choice
from graphics import Window
from cell import Cell


class Maze:
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int | float,
        num_cols: int | float,
        cell_size_x: int,
        cell_size_y: int,
        window: Window | None = None,
        init_seed: int | None = None,
    ) -> None:
        if init_seed is not None:
            seed(init_seed)
        self._cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__window = window
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        # self._cells = [
        #     [Cell(self.__window) for _ in range(self.__num_rows)]
        #     for _ in range(self.__num_cols)
        # ]

        for i in range(self.__num_cols):
            col_cells = []
            for j in range(self.__num_rows):
                col_cells.append(Cell(self.__window))
            self._cells.append(col_cells)
        for i, row in enumerate(self._cells):
            for j in range(len(row)):
                self._draw_cell(i, j)

    def _draw_cell(self, i: int, j: int) -> None:
        if self.__window is None:
            return
        x1 = self.__x1 + i * self.__cell_size_x
        y1 = self.__y1 + j * self.__cell_size_y
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self, framerate: int = 300) -> None:
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(1 / framerate)

    def _break_entrance_and_exit(self) -> None:
        top_or_left = choice(["top", "left"])
        if top_or_left == "top":
            self._cells[0][0].has_top_wall = False
        else:
            self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        bottom_or_right = choice(["bottom", "right"])
        if bottom_or_right == "bottom":
            self._cells[self.__num_cols - 1][
                self.__num_rows - 1
            ].has_bottom_wall = False
        else:
            self._cells[self.__num_cols - 1][self.__num_rows - 1].has_right_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __find_valid_neighbors(self, i: int, j: int, solve: bool = False) -> list:
        cardinals = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        all_neighbors = [(i + coords[0], j + coords[1]) for coords in cardinals]
        valid_neighbors = []
        for neighbor in all_neighbors:
            if neighbor[0] >= 0 and neighbor[1] >= 0:
                if neighbor[0] < self.__num_cols and neighbor[1] < self.__num_rows:
                    if not self._cells[neighbor[0]][neighbor[1]].visited:
                        if not solve:
                            valid_neighbors.append(neighbor)
                        else:
                            if neighbor[0] < i and not self._cells[i][j].has_left_wall:
                                valid_neighbors.append(neighbor)
                            elif (
                                neighbor[0] > i and not self._cells[i][j].has_right_wall
                            ):
                                valid_neighbors.append(neighbor)
                            elif neighbor[1] < j and not self._cells[i][j].has_top_wall:
                                valid_neighbors.append(neighbor)
                            elif (
                                neighbor[1] > j
                                and not self._cells[i][j].has_bottom_wall
                            ):
                                valid_neighbors.append(neighbor)
        return valid_neighbors

    def _break_walls_r(self, i: int, j: int) -> None:
        self._cells[i][j].visited = True
        while True:
            valid_neighbors = self.__find_valid_neighbors(i, j)
            if len(valid_neighbors) == 0:
                self._draw_cell(i, j)
                return
            destination = choice((valid_neighbors))
            if destination[0] < i:
                self._cells[i][j].has_left_wall = False
                self._draw_cell(i, j)
                self._cells[destination[0]][destination[1]].has_right_wall = False
                self._draw_cell(destination[0], destination[1])
            elif destination[0] > i:
                self._cells[i][j].has_right_wall = False
                self._draw_cell(i, j)
                self._cells[destination[0]][destination[1]].has_left_wall = False
                self._draw_cell(destination[0], destination[1])
            elif destination[1] < j:
                self._cells[i][j].has_top_wall = False
                self._draw_cell(i, j)
                self._cells[destination[0]][destination[1]].has_bottom_wall = False
                self._draw_cell(destination[0], destination[1])
            else:
                self._cells[i][j].has_bottom_wall = False
                self._draw_cell(i, j)
                self._cells[destination[0]][destination[1]].has_top_wall = False
                self._draw_cell(destination[0], destination[1])
            self._break_walls_r(destination[0], destination[1])

    def _reset_cells_visited(self) -> None:
        for column in self._cells:
            for cell in column:
                cell.visited = False

    def solve(self) -> bool:
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int) -> bool:
        self._animate()
        # for index, column in enumerate(self._cells):
        #     for jndex, cell in enumerate(column):
        #         print(f"cell {index, jndex}")
        #         print(f"has left wall = {cell.has_left_wall}")
        #         print(f"has right wall = {cell.has_right_wall}")
        #         print(f"has top wall = {cell.has_top_wall}")
        #         print(f"has bottom wall = {cell.has_bottom_wall}")
        #         print("\n")
        self._cells[i][j].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            # print("found the exit")
            return True
        valid_neighbors = self.__find_valid_neighbors(i, j, True)
        # print(f"neighbors = {valid_neighbors}")
        for neighbor in valid_neighbors:
            self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]])
            # print(f"from {i, j} to {neighbor}")
            if self._solve_r(neighbor[0], neighbor[1]):
                return True
            self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)
        return False
