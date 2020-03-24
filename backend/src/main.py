import socket

from config import HOST, PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    try:
        start_server()
    except KeyboardInterrupt:
       stop_server(130)

def stop_server(exit_code: int):
    try:
        print('KeyboardInterrupt event received\nShutting down gracefully.')
        server.close()
        exit(130)
    except Exception as e:
        print('could not shut down gracefully', e)

def start_server():
    global server

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


if __name__ == '__main__':
    main()