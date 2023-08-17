import time

import pygame

from life import GameOfLife
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        super().__init__(life)

    def draw_lines(self) -> None:
        x_start, x_end = 0, self.width * self.cell_size
        y_start, y_end = 0, self.height * self.cell_size

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
        for y in range(self.cell_height):
            for x in range(self.cell_width):
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
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))
        running = True
        start = False  # игра началась
        can_add = True  # можно ли еще закрашивать на поле клетки
        while running and not self.life.is_max_generations_exceeded and self.life.is_changing:
            for event in pygame.event.get():  # получаем события с клавиатуры или мышки
                if event.type == pygame.QUIT:  # если игру закрыли, то выходим из цикла
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:  # проверяем была ли нажата кнопка мыши
                    if can_add:  # проверяем можно ли добавлять
                        x, y = event.pos  # считываем координаты нажатой мышки
                        self.life.curr_generation[y // self.cell_size][x // self.cell_size] = (
                            self.life.curr_generation[y // self.cell_size][x // self.cell_size] + 1
                        ) % 2  # в текущем
                        # состоянии меняем значение нажатой клетки (клетка либо белая, либо зеленая)
                if event.type == 769:  # код пробела
                    start = not start  # меняем состояние игры (пауза/плей)
                    can_add = False  # как только запускаем игру, менять клетки уже нельзя

            if start:  # если игра запущена, то делаем след. шаг
                self.life.step()
            self.draw_grid()  # отрисовываем поле и линии
            self.draw_lines()
            pygame.display.flip()
            clock.tick(self.speed)
        time.sleep(10)
        pygame.quit()
