import socket


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 8080)
    print('connecting to localhost on port 8080')

    try:
        sock.connect(server_address)
        print('Client is sending a message')
        sock.send('GET / HTTP/1.1'.encode(encoding='UTF-8'))

        data = sock.recv(4096)
        data = data.decode(encoding='UTF-8')
        print('Recv: ' + data)

    finally:
        print('Closing client connection')
        sock.close()
