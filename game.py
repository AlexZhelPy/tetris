# game.py
import pygame
import random
from typing import List, Tuple, Optional
from settings import (
    GRID_WIDTH, GRID_HEIGHT, CELL_SIZE,
    SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, BLACK, WHITE, GRAY, FONT, FPS
)
from tetrominoes import I, O, T, L, J, S, Z, Tetromino

class Tetris:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tetris")
        self.clock = pygame.time.Clock()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece: Optional[Tetromino] = self._new_piece()
        self.next_piece: Optional[Tetromino] = self._new_piece()
        self.game_over = False
        self.score = 0

    def _new_piece(self) -> Tetromino:
        """Создает новую случайную фигуру."""
        pieces = [I, O, T, L, J, S, Z]
        piece_class = random.choice(pieces)
        piece = piece_class()
        piece.x = GRID_WIDTH // 2 - len(piece.shape[0]) // 2
        piece.y = 0
        return piece

    def _draw_sidebar(self) -> None:
        """Отрисовывает боковую панель с информацией."""
        sidebar_x = GRID_WIDTH * CELL_SIZE + 20

        # Счёт
        score_text = FONT.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (sidebar_x, 30))

        # Следующая фигура
        next_text = FONT.render("Next:", True, WHITE)
        self.screen.blit(next_text, (sidebar_x, 80))

        if self.next_piece:
            # Отрисовка следующей фигуры в центре боковой панели
            for y, row in enumerate(self.next_piece.shape):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(
                            self.screen,
                            self.next_piece.color,
                            (
                                sidebar_x + x * CELL_SIZE,
                                120 + y * CELL_SIZE,
                                CELL_SIZE - 2, CELL_SIZE - 2
                            )
                        )

    def _valid_position(self) -> bool:
        """Проверяет, может ли фигура находиться в текущей позиции."""
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    if (self.current_piece.x + x < 0 or
                            self.current_piece.x + x >= GRID_WIDTH or
                            self.current_piece.y + y >= GRID_HEIGHT or
                            self.grid[self.current_piece.y + y][self.current_piece.x + x]):
                        return False
        return True

    def _merge_piece(self) -> None:
        """Фиксирует фигуру в сетке."""
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_piece.y + y][self.current_piece.x + x] = self.current_piece.color

    def _clear_lines(self) -> None:
        """Удаляет заполненные строки и обновляет счет."""
        lines_to_clear = []
        for y in range(GRID_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)

        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
            self.score += 100 * len(lines_to_clear)  # Бонус за несколько линий

    def _draw_grid(self) -> None:
        """Отрисовывает игровое поле."""
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(
                    self.screen,
                    self.grid[y][x] if self.grid[y][x] else GRAY,
                    (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    0 if self.grid[y][x] else 1
                )

    def _draw_piece(self) -> None:
        """Отрисовывает текущую фигуру."""
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        self.screen,
                        self.current_piece.color,
                        (
                            (self.current_piece.x + x) * CELL_SIZE,
                            (self.current_piece.y + y) * CELL_SIZE,
                            CELL_SIZE, CELL_SIZE
                        )
                    )

    def run(self) -> None:
        """Главный игровой цикл."""
        while not self.game_over:
            self.screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.current_piece.x -= 1
                        if not self._valid_position():
                            self.current_piece.x += 1
                    elif event.key == pygame.K_RIGHT:
                        self.current_piece.x += 1
                        if not self._valid_position():
                            self.current_piece.x -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_piece.y += 1
                        if not self._valid_position():
                            self.current_piece.y -= 1
                    elif event.key == pygame.K_UP:
                        self.current_piece.rotate()
                        if not self._valid_position():
                            self.current_piece.rotate()  # Откат, если нельзя повернуть

            # Движение фигуры вниз
            self.current_piece.y += 1
            if not self._valid_position():
                self.current_piece.y -= 1
                self._merge_piece()
                self._clear_lines()
                self.current_piece = self.next_piece
                self.next_piece = self._new_piece()
                if not self._valid_position():
                    self.game_over = True

            self._draw_grid()
            self._draw_piece()
            self._draw_sidebar()  # Отрисовка боковой панели
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Tetris()
    game.run()
