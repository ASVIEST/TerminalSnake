from random import randint
import time


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
    return snake


def create_snake(width, height):
    return [(randint(0, width - 1), randint(0, height - 1))]


def create_apple(width, height, fruits, snake):
    apple = randint(0, width - 1), randint(0, height - 1)
    while apple in fruits or apple in snake:
        apple = randint(0, width - 1), randint(0, height - 1)
    fruits.append(apple)


def check_lose(width, height, snake):
    return check_bounds(width, height, snake) or check_self(snake)


def check_bounds(width, height, snake):
    return False


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
        game_over()
        return
    for apple in fruits:
        if check_food(snake, apple):
            enlarge_snake(snake, direction)
            break




width = 60
height = 20

fruits = [create_apple(width, height)]
snake = create_snake(width, height)
print(field_to_text(width, height, snake, fruits))
