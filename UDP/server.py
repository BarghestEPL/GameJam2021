import socket
import threading
import pygame as pg
from const import *
from protocol import *
from GameObjects import *

srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv.bind(ADDRESS)
clients = {}
while True:
    data, addr = srv.recvfrom(DATA_LEN)
    player = clients.get(addr)
    if player:
        player.update(data)
    else:
        clients[addr] = Player()
    srv.sendto(get_state(), addr)
