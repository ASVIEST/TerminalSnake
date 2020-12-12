from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from snake import Snake


class Field:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def to_text(self, snake: 'Snake', awards: list) -> str:
        """
        width: int, height: int,
        snake: [(x, y), (x, y), ...]
        fruits: [(x, y), (x, y), ...]
        """

        field = [[' ' for x in range(self.width)] for y in range(self.height)]
        for bonus in awards:
            field[bonus.y][bonus.x] = f'\033[31m{bonus}\033[0m'
        for x, y in snake:
            field[int(y)][int(x)] = f'\033[32m{snake.symbol}\033[0m'

        return '#' * (self.width + 2) + '\n' + '\n'.join(
            '#' + ''.join(line) + '#' for line in field
        ) + '\n' + '#' * (self.width + 2)
