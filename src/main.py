from socket import *

HOST = 'localhost'
PORT = 8080

def createServer():
    server_socket = socket(AF_INET, SOCK_STREAM)
    try:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)

        while True:
            pass

createServer()