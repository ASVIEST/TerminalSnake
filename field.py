from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from snake import Snake


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.bg_color = '47' #'46'
        self.edges_color = '30' #'35'
        self.edges = [
            f'\033[{self.edges_color}m┌\033[0m\033[{self.bg_color}m',
            f'\033[{self.edges_color}m┐\033[0m\033[{self.bg_color}m',
            f'\033[{self.edges_color}m└\033[0m\033[{self.bg_color}m',
            f'\033[{self.edges_color}m┘\033[0m\033[{self.bg_color}m'
        ]

    def get_colored_symbol(self, symbol):
    	return f'\033[{self.edges_color}m{symbol}\033[0m\033[{self.bg_color}m'

    def to_text(self, snake: 'Snake', awards: list) -> str:
        """
        width: int, height: int,
        snake: [(x, y), (x, y), ...]
        fruits: [(x, y), (x, y), ...]
        """

        field = [[' ' for x in range(self.width)] for y in range(self.height)]
        for bonus in awards:
            field[bonus.y][bonus.x] = f'\033[31m{bonus}\033[0m\033[{self.bg_color}m'
        for x, y in snake:
            field[int(y)][int(x)] = f'\033[32m{snake.symbol}\033[0m\033[{self.bg_color}m'

        return f'\033[{self.edges_color}m\033[{self.bg_color}m' + self.edges[0] + self.get_colored_symbol('─') * (self.width) + self.edges[1] + '\n' + '\n'.join(
            self.get_colored_symbol('│\033[0m') + ''.join(line) + self.get_colored_symbol('│\033[0m') for line in field
        ) + '\n' +self.edges[2] + self.get_colored_symbol('─') * (self.width) + self.edges[3] + '\033[0m'