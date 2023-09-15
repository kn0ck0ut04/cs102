import curses
import time

from life import GameOfLife
from ui import UI


class Console(UI):
    def __init__(self, life: GameOfLife) -> None:
        super().__init__(life)

    def draw_borders(self, screen) -> None:
        """Отобразить рамку."""
        top_border = "+" + "-" * self.life.cell_width + "+"
        screen.addstr(0, 0, top_border)
        side_border = "|" + " " * self.life.cell_height + "|"
        for i in range(1, self.life.cell_height + 1):
            screen.addstr(i, 0, side_border)
            screen.refresh()
            time.sleep(0.001)
        bottom_border = top_border
        screen.addstr(self.life.cell_height + 1, 0, bottom_border)
        screen.refresh()
        time.sleep(0.001)

    def draw_grid(self, screen) -> None:
        """Отобразить состояние клеток."""
        for i in range(self.life.cell_width):
            for j in range(self.life.cell_height):
                if self.life.curr_generation[j][i] == 1:
                    screen.addch(j + 1, i + 1, "*")

    def run(self) -> None:
        screen = curses.initscr()
        while not self.life.is_max_generations_exceeded and self.life.is_changing:
            self.draw_borders(screen)
            self.draw_grid(screen)
            screen.refresh()
            time.sleep(1)
            self.life.step()
        screen.addstr(self.life.cell_height + 2, self.life.cell_width // 2 - 4, "Game Over")
        screen.refresh()
        time.sleep(1)
        curses.endwin()

if __name__ == '__main__':
    game = GameOfLife((17, 150))
    ui = Console(game)
    ui.run()