import socket


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('localhost', 8080)
    print('connecting to localhost on port 8080')

    try:
        sock.connect(server_address)
        print('Client is sending a message')
        sock.send('Hello, World!'.encode(encoding='UTF-8'))
    finally:
        print('Closing client connection')
        sock.close()
