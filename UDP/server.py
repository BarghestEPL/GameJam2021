import socket
import threading
import pygame as pg
from const import *
from protocol import *
from GameObjects import *

dt = 0
clock = pg.time.Clock()
srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv.bind(ADDRESS)

try:
    while True:
        data, addr = srv.recvfrom(DATA_LEN)
        player = clients.get(addr)
        if player:
            player.set_inputs(data)
        else:
            clients[addr] = Player(addr, data)

        srv.sendto(get_state(dt), addr)
        dt = clock.tick(144)
except KeyboardInterrupt:
    print("bye")
finally:
    srv.close()
