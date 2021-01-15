from random import randint
import time
import sys

from bonus import Bonus
from field import Field
# from kbhit import KBHit
from kbthread import keys
from snake import Snake
from Cursor import hide_cursor, show_cursor

WIDTH = 60
HEIGHT = 20

directions_codes = {
    'left': (-1, 0),
    'right': (1, 0),
    'up': (0, -1),
    'down': (0, 1),
    's': (0, 1),
    'w': (0, -1),
    'a': (-1, 0),
    'd': (1, 0),
}

if len(sys.argv) > 1 and sys.argv[1] == 'dev':
    developer_mode = True
else:
    developer_mode = False


def create_snake():
    return Snake(randint(0, WIDTH // 2), randint(0, HEIGHT - 2), field)


def create_apple():
    apple = randint(0, WIDTH - 2), randint(0, HEIGHT - 2)
    while apple in fruits or apple in snake:
        apple = randint(0, WIDTH - 2), randint(0, HEIGHT - 2)
    return Bonus('o', *apple)


def game_over():
    # TODO
    pass


def update_screen():
    global time_delta
    for i in range(len(fruits)):
        apple = fruits[i]
        if snake.check_bonus(apple):
            fruits[i] = create_apple()
            if not developer_mode:
                time_delta *= 0.9
            break
    snake.move()
    if snake.check_lose():
        return False
    print(f'\033[{HEIGHT + 3}A' + field.to_text(snake, fruits))
    print(f'Your score is {len(snake)}.')
    return True


field = Field(WIDTH, HEIGHT)
fruits = []
snake = create_snake()
fruits.append(create_apple())

print(field.to_text(snake, fruits) + '\n')

time_delta = 0.001 if developer_mode else 0.1
p = time.time()
hide_cursor()

try:
    while True:
        c = time.time()
        if c - p < time_delta:
            pause = time_delta - (c - p)
            time.sleep(pause if snake.direction[1] == 0 else pause * 2)
        p = time.time()

        if keys:
            key = keys.pop().lower()
            if key == '\033':
                break
            elif key in directions_codes:
                snake.direction = directions_codes[key]
                #print(tuple(keys))
            elif developer_mode:
                snake.direction = (0, 0)
            if not update_screen():
                break
        elif not developer_mode:
            if not update_screen():
                break

finally:  # except KeyboardInterrupt
    show_cursor()
