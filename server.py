import time
import socket
from proto import *
from GameObjects.GameObject import *

HP = HOST, PORT = "", 45632
srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv.bind(HP)
srv.listen(5)


blue_sock, _ = srv.accept()
red_sock, _ = srv.accept()

playerBlue = Player(blue_sock)
playerRed = Player(red_sock)
while True:
    blue_data = recv_msg(blue_sock)
    playerBlue.update()

    data = {
        'blue': playerBlue.get_state()
    }

    send_msg(playerRed.sock, data)
    send_msg(playerBlue.sock, data)
