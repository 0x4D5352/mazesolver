import unittest
from window import Window


class TestWindow(unittest.TestCase):
    def test_creation(self):
        new_window = Window(800, 600)
        self.assertEqual(
            new_window, 'Window("800x600", "Boot.Dev Maze Solver", "Is Running: False")'
        )
