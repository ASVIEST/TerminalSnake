from random import randint
import time

from kbhit import KBHit


def field_to_text(width: int, height: int, snake: list, fruits: list) -> str:
    '''
    width: int, height: int,
    snake: [(x, y), (x, y), ...]
    fruits: [(x, y), (x, y), ...]
    '''

    field = [[' ' for x in range(width)] for y in range(height)]
    for x, y in snake:
        field[y][x] = 's'
    for x, y in fruits:
        field[y][x] = 'o'

    return '#' * (width + 2) + '\n' + '\n'.join(
        '#' + ''.join(line) + '#' for line in field
    ) + '\n' + '#' * (width + 2)


def move_snake(snake, direction):
    '''
    direction = (0, 1)
    '''
    head = snake[0]
    snake.pop()
    snake.insert(0, (head[0] + direction[0], head[1] + direction[1]))


def create_snake(width, height):
    return [(randint(0, width // 2), randint(0, height - 2))]


def create_apple(width, height, fruits, snake):
    apple = randint(0, width - 2), randint(0, height - 2)
    while apple in fruits or apple in snake:
        apple = randint(0, width - 2), randint(0, height - 2)
    fruits.append(apple)


def check_lose(width, height, snake):
    return check_bounds(width, height, snake) or check_self(snake)


def check_bounds(width, height, snake):
    head = snake[0]
    return not (0 <= head[0] < width and 0 <= head[1] < height)


def check_self(snake):
    return False


def game_over():
    pass


def check_food(snake, apple):
    return snake[0] == apple


def enlarge_snake(snake, direction, amount=1):
    pass


def update_screen(width, height, snake, fruits, direction):
    move_snake(snake, direction)
    if check_lose(width, height, snake):
        return False
    for apple in fruits:
        if check_food(snake, apple):
            enlarge_snake(snake, direction)
            break
    print(f'\033[{height + 2}A' + field_to_text(width, height, snake, fruits))
    return True


width = 60
height = 20

directions_codes = {
    97:(-1, 0),
    100:(1, 0),
    119:(0, -1),
    115:(0, 1),

}

developer_mode = False
fruits = []
snake = create_snake(width, height)
create_apple(width, height, fruits, snake)
direction = (1, 0)
print('\n' * (height + 2))

p = time.time()
kb = KBHit()
while True:
    c = time.time()
    if c - p < 0.1:
        time.sleep(0.1 - (c - p))
    p = time.time()

    if developer_mode == True:
        if kb.kbhit():
            c = kb.getch()
            if ord(c) == 27: # ESC
                break
            direction = directions_codes[ord(c)]
            if not update_screen(width, height, snake, fruits, direction):
                break
    else:
        if True:
            if kb.kbhit():
                c = kb.getch()
                if ord(c) == 27: # ESC
                    break
                direction = directions_codes[ord(c)]
        if not update_screen(width, height, snake, fruits, direction):
            break
