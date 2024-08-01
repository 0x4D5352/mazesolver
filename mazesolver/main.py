from random import seed, randrange
from graphics import Window
from maze import Maze


def main() -> None:
    x = 800
    y = 600
    cofactor = 10
    num_rows = x // cofactor
    num_cols = y // cofactor
    margin = 50
    cell_size_x = int((x - 2 * margin) / num_cols)
    cell_size_y = int((y - 2 * margin) / num_rows)

    window = Window(x, y)
    print("generating maze")
    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        window,
        init_seed=145,
    )
    print("solving maze")
    res = maze.solve()
    if res:
        print("solved!")
    else:
        print("not solved...")
    window.wait_for_close()


if __name__ == "__main__":
    main()
