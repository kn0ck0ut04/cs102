import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        top_border = "+" + "-" * self.width + "+"
        screen.addstr(0, 0, top_border)
        side_border = "|" + " " * self.width + "|"
        for i in range(1, self.height + 1):
            screen.addstr(i, 0, side_border)
        bottom_border = top_border
        screen.addstr(self.height + 1, 0, bottom_border)


    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for i in range(self.width):  # идем по всем клеткам нашего поля
            for j in range(self.height):
                if self.life.curr_generation[j][i] == 1:  # если в текущем поколении клетка живая, то рисуем *
                    screen.addch(j + 1, i + 1, "*")

    def run(self) -> None:
        # открываем консоль
        screen = curses.initscr()
        while (
            not self.life.is_max_generations_exceeded and self.life.is_changing
        ):  # пока не достигнем заданного кол-ва шагов, либо изменился экран
            self.draw_borders(screen)  # границы
            self.draw_grid(screen)  # поле
            screen.refresh()  # обновл. консоли
            time.sleep(1)
            self.life.step()  # след. шаг игры
        screen.addstr(self.height + 2, self.width // 2 - 4, "Game Over")  # если игра закончилась пишет game over
        screen.refresh()
        time.sleep(1)
        curses.endwin()
