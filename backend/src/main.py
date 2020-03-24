import socket

from config import HOST, PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST,PORT))
server.listen(1)

print(f'server listening on {HOST}:{PORT}')

while True:
    client, address = server.accept()
    print(f'connection from {address}')

    request_data = client.recv(1024)

    # print(f'\treceived: {request_data.decode("utf-8")}')

    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client.sendall(http_response)
    client.close()
