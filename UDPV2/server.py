import json
import socket
import threading
from GameObjects import *


dt = 0
run = 1
safe_lock = threading.Lock()
clock = pg.time.Clock()
srv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
srv.bind(("", SRV_PORT))


def handle_clients():
    while run:
        data, addr = srv.recvfrom(256)
        with safe_lock:
            player = clients.get(addr)
            if player:
                player.set_inputs(json.loads(data.decode("utf-8")))
            else:
                clients[addr] = Player(addr, json.loads(data.decode("utf-8")))


threading.Thread(target=handle_clients, daemon=True).start()
try:
    while True:
        for obj in gameObjects:
            obj.update(dt)

        b = json.dumps([obj.get_state() for obj in gameObjects]).encode("utf-8")

        with safe_lock:
            for client in clients.keys():
                srv.sendto(b, client)
        dt = clock.tick(128)
except KeyboardInterrupt:
    run = False
    srv.close()
