# settings.py
from typing import Tuple, List
import pygame

# Инициализация pygame для работы со шрифтами
pygame.init()

# Размеры игрового поля
GRID_WIDTH: int = 10
GRID_HEIGHT: int = 20
CELL_SIZE: int = 30

# Цвета
BLACK: Tuple[int, int, int] = (0, 0, 0)
WHITE: Tuple[int, int, int] = (255, 255, 255)
RED: Tuple[int, int, int] = (255, 0, 0)
GREEN: Tuple[int, int, int] = (0, 255, 0)
BLUE: Tuple[int, int, int] = (0, 0, 255)
CYAN: Tuple[int, int, int] = (0, 255, 255)
MAGENTA: Tuple[int, int, int] = (255, 0, 255)
YELLOW: Tuple[int, int, int] = (255, 255, 0)
ORANGE: Tuple[int, int, int] = (255, 165, 0)
GRAY: Tuple[int, int, int] = (128, 128, 128)
PURPLE: Tuple[int, int, int] = (128, 0, 128)

# Цвета фигур
COLORS: List[Tuple[int, int, int]] = [CYAN, YELLOW, PURPLE, ORANGE, BLUE, GREEN, RED]

# Настройки окна
SCREEN_WIDTH: int = GRID_WIDTH * CELL_SIZE + 200  # + боковая панель
SCREEN_HEIGHT: int = GRID_HEIGHT * CELL_SIZE
FPS: int = 5

# Шрифт
FONT = pygame.font.SysFont('Arial', 24)
