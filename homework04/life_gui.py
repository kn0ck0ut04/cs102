import sys

import pygame

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)
        self.cell_size = cell_size
        screen = pygame.display.set_mode([self.life.cell_height, self.life.cell_width])
        self.screen = screen
        self.speed = speed

    def draw_lines(self) -> None:
        x_start, x_end = 0, self.life.cell_width * self.cell_size
        y_start, y_end = 0, self.life.cell_height * self.cell_size

        for x in range(x_start, x_end, self.cell_size):
            pygame.draw.line(
                self.screen,
                pygame.Color("black"),
                (x, 0),
                (x, y_end),
            )

        for y in range(y_start, y_end, self.cell_size):
            pygame.draw.line(
                self.screen,
                pygame.Color("black"),
                (0, y),
                (x_end, y),
            )

    def draw_grid(self) -> None:
        for y in range(self.life.cell_height):
            for x in range(self.life.cell_width):
                rect = pygame.Rect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                if self.life.curr_generation[y][x]:
                    pygame.draw.rect(self.screen, pygame.Color("green"), rect)
                else:
                    pygame.draw.rect(self.screen, pygame.Color("white"), rect)

    def run(self) -> None:
        pygame.init()
        screen = pygame.display.set_mode([self.life.cell_height, self.life.cell_width])
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        screen.fill(pygame.Color("white"))
        running = True
        start = False
        can_add = True
        while running and not self.life.is_max_generations_exceeded and self.life.is_changing:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if can_add:
                        x, y = event.pos
                        self.life.curr_generation[y // self.cell_size][x // self.cell_size] = (
                            self.life.curr_generation[y // self.cell_size][x // self.cell_size] + 1
                        ) % 2
                if event.type == 769:
                    start = not start
                    can_add = False

            if start:
                self.life.step()
            self.draw_grid()
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.display.quit()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = GameOfLife((400, 400))
    ui = GUI(game)
    ui.run()
