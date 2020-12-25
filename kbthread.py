from threading import Thread
import signal
import sys
import termios
import atexit

keys = []


def kb():
    while True:
        c = sys.stdin.read(1)
        keys.append(c)


def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)


fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# New terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)
termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

# Support normal-terminal reset at exit
atexit.register(set_normal_term)

t = Thread(target=kb)
t.start()

while True:
    if keys:
        if keys == ['\033']:
            signal.raise_signal(signal.SIGTERM)
            break
        print(keys)
        keys.clear()
