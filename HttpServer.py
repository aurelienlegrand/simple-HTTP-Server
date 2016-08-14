import socket
import os


class HttpServer:
    """Simple HTTP server"""

    def __init__(self, port=8080):
        self.port = port

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', self.port))

        # Max 5 connection requests
        sock.listen(5)
        print('HTTP server started. Listening on port ' + str(self.port) + '.' + os.linesep)

        while True:
            try:
                connection, client_address = sock.accept()
                print('Connection established with ' + str(client_address) + '.' + os.linesep)
                data = connection.recv(4096)
                print('Data received: ' + str(data.decode(encoding='UTF-8')) + '.' + os.linesep)

            finally:
                connection.close()
                print('Connnection closed.' + os.linesep)


if __name__ == '__main__':
    server = HttpServer()
    server.start()
