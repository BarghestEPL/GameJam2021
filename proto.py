import json


def recv_msg(sock, h=512, f="utf-8"):
    try:
        msg_len = int(sock.recv(h).decode(f))
        data = sock.recv(msg_len).decode(f)
        return json.loads(data)
    except OSError:
        return None
    except ValueError:
        return None


def send_msg(sock, data, h=512, f="utf-8"):
    msg = json.dumps(data).encode(f)
    msg_len = str(len(msg)).encode(f)
    print(msg_len)
    try:
        sock.sendall(msg_len + (h - len(msg_len)) * b' ')
        sock.sendall(msg)
    except OSError:
        return False
    return True
