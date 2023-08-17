import copy
import pathlib
import typing as tp
from random import randint

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size[0], size[1]

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.cols
        self.cell_height = self.rows

        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        if randomize:
            return [[randint(0, 1) for _ in range(self.cell_width)] for __ in range(self.cell_height)]
        else:
            return [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]

    def get_neighbours(self, cell: Cell) -> Cells:
        if self.curr_generation is None:
            return []
        list_neighbours = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbour_cell = (cell[0] + i, cell[1] + j)
                if 0 <= neighbour_cell[0] < self.cell_height and 0 <= neighbour_cell[1] < self.cell_width:
                    list_neighbours.append(self.curr_generation[neighbour_cell[0]][neighbour_cell[1]])
        return list_neighbours

    def get_next_generation(self) -> Grid:
        # создаем новое поле из 0
        new_grid = [[0 for _ in range(self.cell_width)] for __ in range(self.cell_height)]
        if self.curr_generation is None:
            return new_grid
        # обходим все клетки поля
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                # получаем соседей заданной клетки
                alive_neighbors = sum(self.get_neighbours((i, j)))
                # если соседей 2 и существо живое или 3, то клетка выживает
                if alive_neighbors == 2 and self.curr_generation[i][j] == 1 or alive_neighbors == 3:
                    new_grid[i][j] = 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        # количество поколений увеличиваем на 1
        self.generations += 1
        # в предыдущее поколение записываем нынешнее поколение,
        # а в нынешнее поколение след. поколение
        self.prev_generation, self.curr_generation = copy.deepcopy(self.curr_generation), self.get_next_generation()

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.generations is not None and int(self.generations) >= self.max_generations:
            return True
        else:
            return False


    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation == self.prev_generation:
            return False
        else:
            return True

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        with open(filename, encoding="utf-8") as file:
            lines = file.read().split("\n")
        curr_generation = []
        for line in lines:
            cells = []
            for cell in line:
                cells.append(int(cell))
            curr_generation.append(cells)
        s = GameOfLife((len(curr_generation), len(curr_generation[0])))
        s.curr_generation = curr_generation
        return s

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w") as f:
            for line in self.curr_generation:
                f.write("".join(map(str, line)) + "\n")

