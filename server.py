import time
import socket
import threading
from proto import *

HP = HOST, PORT = "", 45632
srv = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
srv.bind(HP)
srv.listen(5)


blue, _ = srv.accept()
red, _ = srv.accept()

while True:
    blue_data = recv_msg(blue)
    print('blue', blue_data)

    red_data = recv_msg(red)
    print('red', red_data)
