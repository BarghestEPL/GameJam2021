import threading


def game_loop():
    while True:
        print('here')


x = threading.Thread(target=game_loop)
x.start()

try:
    while True:
        print("hello")
except KeyboardInterrupt:
    x.join()
    print("bye")
