from tkinter import Tk, BOTH, Canvas


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
