import copy
import typing as tp
from random import randint

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 10) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.grid = None

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Устанавливаем размер окна
        self.screen_size = self.width, self.height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Скорость протекания игры
        self.speed = speed

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        # Создание списка клеток

        self.grid = self.create_grid(randomize=True)  # type: ignore
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            self.draw_grid()
            self.draw_lines()
            self.grid = copy.deepcopy(self.get_next_generation())  # type: ignore

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """
        if randomize:
            return [[randint(0, 1) for _ in range(self.cell_width)] for __ in range(self.cell_height)]
        else:
            return [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """

        for i in range(len(self.grid)):  # type: ignore
            for j in range(len(self.grid[0])):  # type: ignore
                x = i * self.cell_size
                y = j * self.cell_size
                if self.grid[i][j]:  # type: ignore
                    pygame.draw.rect(self.screen, pygame.Color("green"), (x, y, self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color("white"), (x, y, self.cell_size, self.cell_size))

    def get_neighbours(self, cell: Cell) -> Cells:
        if self.grid is None:
            return []
        list_neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbour_cell = (cell[0] + i, cell[1] + j)
                if 0 <= neighbour_cell[0] < self.cell_height and 0 <= neighbour_cell[1] < self.cell_width:
                    list_neighbours.append(self.grid[neighbour_cell[0]][neighbour_cell[1]])
        return list_neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_grid = [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]
        if self.grid is None:
            return new_grid
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                alive_neighbors = sum(self.get_neighbours((i, j)))
                if alive_neighbors == 2 and self.grid[i][j] == 1 or alive_neighbors == 3:
                    new_grid[i][j] = 1
        return new_grid


if __name__ == "__main__":
    game = GameOfLife(320, 240, 40)
    game.run()
