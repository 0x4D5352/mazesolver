from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x: int, y: int) -> None:
        if not x:
            self.x = 0
        else:
            self.x = x
        if not y:
            self.y = 0
        else:
            self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Line:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas: Canvas, fill_color: str = "black") -> None:
        (x1, y1) = self.p1.x, self.p1.y
        (x2, y2) = self.p2.x, self.p2.y
        canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)

    def str(self) -> str:
        return f"Line from {self.p1} to {self.p2}"


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        if not width and not height:
            print("no dimensions provided, using 1/8 of display...")
            self.__width = self.__root.winfo_screenwidth() / 8
            self.__height = self.__root.winfo_screenheight() / 8
        elif not width:
            self.__width = height
            self.__height = height
        elif not height:
            self.__width = width
            self.__height = width
        else:
            self.__width = width
            self.__height = height
        self.__root.title("Boot.Dev Maze Solver")
        self.__canvas = Canvas(
            self.__root, bg="white", height=self.__height, width=self.__width
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, fill_color: str = "black") -> None:
        line.draw(self.__canvas, fill_color)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")

    def close(self) -> None:
        self.__is_running = False
