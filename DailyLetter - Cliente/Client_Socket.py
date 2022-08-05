import socket


def send_msg_to_server(msg):
    # Instancia o Socket
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((socket.gethostname(), 12345))
    c.sendall((msg.encode()))
