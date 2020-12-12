from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from field import Field


class Snake:
    def __init__(self, init_x, init_y, field: 'Field'):
        self.field = field
        self._elements = [(init_x, init_y)]
        self.symbol = '●'
        self.direction = (1, 0)
        self.enlarge = False

    def __iter__(self):
        return self._elements.__iter__()

    def __contains__(self, item):
        return item in self._elements

    def __len__(self):
        return len(self._elements)

    def move(self):
        """
        direction = (0, 1)
        """
        head = self._elements[0]
        if not self.enlarge:
            self._elements.pop()
        self._elements.insert(0, (head[0] + self.direction[0], head[1] + self.direction[1]))
        self.enlarge = False

    def check_lose(self):
        return self._check_bounds() or self._check_self()

    def _check_bounds(self):
        return not (0 <= self.head[0] < self.field.width and 0 <= self.head[1] < self.field.height)

    def _check_self(self):
        return self._elements[0] in self._elements[1:]

    @property
    def head(self):
        return self._elements[0]

    def check_bonus(self, bonus):
        x, y = map(int, self._elements[0])
        if (x, y) == (bonus.x, bonus.y):
            self.enlarge = True
        return self.enlarge
