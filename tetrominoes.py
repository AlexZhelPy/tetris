# tetrominoes.py
from typing import List, Tuple
from settings import CELL_SIZE

class Tetromino:
    """Базовый класс для тетромино."""
    def __init__(self) -> None:
        self.shape: List[List[int]] = []
        self.color: Tuple[int, int, int] = (0, 0, 0)
        self.x: int = 0
        self.y: int = 0

    def rotate(self) -> None:
        """Поворот фигуры на 90 градусов."""
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

class I(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.color = (0, 255, 255)  # Cyan

class O(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [1, 1],
            [1, 1]
        ]
        self.color = (255, 255, 0)  # Yellow

class T(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.color = (128, 0, 128)  # Purple

class L(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.color = (255, 165, 0)  # Orange

class J(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [1, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.color = (0, 0, 255)  # Blue

class S(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [0, 1, 1],
            [1, 1, 0],
            [0, 0, 0]
        ]
        self.color = (0, 255, 0)  # Green

class Z(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.shape = [
            [1, 1, 0],
            [0, 1, 1],
            [0, 0, 0]
        ]
        self.color = (255, 0, 0)  # Red
