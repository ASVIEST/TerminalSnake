from threading import Thread
import signal
import sys
import os

if os.name == 'nt':
    import msvcrt

else:
    import termios
    import atexit

keys = []


def kb():
    while True:
        if os.name == 'nt':
            key = msvcrt.getch()
            key = repr(key)[2:-1]
            #print(key)
        else:
            key = sys.stdin.read(1)
        keys.append(key)


def set_normal_term():
    if not os.name == 'nt':
        termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

if not os.name == 'nt':
    fd = sys.stdin.fileno()
    new_term = termios.tcgetattr(fd)
    old_term = termios.tcgetattr(fd)

    # New terminal setting unbuffered
    new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

    # Support normal-terminal reset at exit
    atexit.register(set_normal_term)


t = Thread(target=kb, daemon=True)
t.start()

if __name__ == '__main__':
    #StartKB()
    pyversion = sys.version_info.major + sys.version_info.minor /10 + sys.version_info.micro / 100
    while True:
        if keys:
            if keys == ['\033'] or keys == ['\\x1b']:
                if pyversion > 3.7 and os.name != 'nt':
                    signal.raise_signal(signal.SIGTERM)
                else: sys.exit()
                break
            print(tuple(keys))
            keys.clear()
