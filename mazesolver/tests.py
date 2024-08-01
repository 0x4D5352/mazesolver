import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_2(self):
        num_cols = 13
        num_rows = 18
        m1 = Maze(10, 10, num_rows, num_cols, 20, 40)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit(self):
        num_cols = 20
        num_rows = 20
        m1 = Maze(0, 0, num_rows, num_cols, 20, 40)
        # m1._break_entrance_and_exit()
        self.assertEqual(
            (m1._cells[0][0].has_left_wall and not m1._cells[0][0].has_top_wall)
            or (not m1._cells[0][0].has_left_wall and m1._cells[0][0].has_top_wall),
            True,
        )
        self.assertEqual(
            (
                m1._cells[num_rows - 1][num_cols - 1].has_right_wall
                and not m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall
            )
            or (
                not m1._cells[num_rows - 1][num_cols - 1].has_right_wall
                and m1._cells[num_rows - 1][num_cols - 1].has_bottom_wall
            ),
            True,
        )

    def test_reset_visited(self):
        num_cols = 13
        num_rows = 18
        m1 = Maze(10, 10, num_rows, num_cols, 20, 40)
        res = True
        for col in m1._cells:
            for cell in col:
                if cell.visited:
                    res = False
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
