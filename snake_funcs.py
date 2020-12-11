from random import randint
import time
import sys

from kbhit import KBHit





def create_snake(width, height):
    return [(randint(0, width // 2), randint(0, height - 2))]


def create_apple(width, height, fruits, self):
    apple = randint(0, width - 2), randint(0, height - 2)
    while apple in fruits or apple in snake:
        apple = randint(0, width - 2), randint(0, height - 2)
    fruits.append(apple)


def game_over():
    pass


def update_screen(width, height, self, fruits, direction):
    enlarge = False
    for i in range(len(fruits)):
        apple = fruits[i]
        if check_food(snake, apple):
            enlarge = True
            fruits.pop(i)
            create_apple(width, height, fruits, snake)
            break
    move_snake(snake, direction, enlarge)
    if check_lose(width, height, snake):
        return False
    print(f'\033[{height + 3}A' + field_to_text(width, height, snake, fruits))
    print(f'Your score is {len(snake)}.')
    return True


width = 60
height = 20

directions_codes = {
    97: (-1, 0),
    100: (1, 0),
    119: (0, -1),
    115: (0, 1),
}

if len(sys.argv) > 1 and sys.argv[1] == 'dev':
    developer_mode = True
else:
    developer_mode = False

fruits = []
snake = create_snake(width, height)
create_apple(width, height, fruits, snake)
direction = (1, 0)
print(field_to_text(width, height, snake, fruits) + '\n')

p = time.time()
kb = KBHit()
while True:
    c = time.time()
    time_delta = 0.001 if developer_mode else 0.1
    if c - p < time_delta:
        time.sleep(time_delta - (c - p))
    p = time.time()

    if kb.kbhit():
        c = kb.getch()
        if ord(c) == 27:  # ESC
            break
        elif ord(c) in directions_codes:
            direction = directions_codes[ord(c)]
        elif developer_mode:
            direction = (0, 0)
        if not update_screen(width, height, snake, fruits, direction):
            break
    elif not developer_mode:
        if not update_screen(width, height, snake, fruits, direction):
            break
