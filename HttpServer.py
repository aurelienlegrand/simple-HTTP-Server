import socket
import os
import re
import configparser

from setuptools.command.test import test


class HttpServer:
    """Simple HTTP server"""

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('httpserver.ini')

        default_config = config['DEFAULT']

        self.port = int(default_config.get('port', '8080'))
        self.hostname = default_config.get('hostname', 'localhost')

    # def __init__(self, port=8080):
    #     self.port = port

    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.hostname, self.port))

        # Max 5 connection requests
        sock.listen(5)
        print('HTTP server started. Listening on port ' + str(self.port) + ' and hostname ' + self.hostname + '.' + os.linesep)

        while True:
            try:
                self.connection, client_address = sock.accept()
                print('Connection established with ' + str(client_address) + '.' + os.linesep)
                data = self.connection.recv(4096)
                data = data.decode(encoding='UTF-8')
                print('Data received: ' + str(data) + '.' + os.linesep)

                req = re.match(r"(.*) (.*) (.*)", data)
                if req:
                    command = str.lower(req.group(1))

                    url = req.group(2)
                    if url == '/':
                        url = 'index.html'
                    if url.startswith('/'):
                        url = url[1:]

                    self.process_command(command, url)
                else:
                    print("Malformed request")

            finally:
                self.connection.close()
                print('Connnection closed.' + os.linesep)

    def get_request(self, url):
        print('get ' + url)

        if os.path.isfile(url):
            file = open(url, 'r')
            file_text = file.read()
            if len(file_text) < 4096:
                self.connection.send(('HTTP/1.1 200 OK' + os.linesep + os.linesep + file_text).encode(encoding='UTF-8'))
        else:
            page_not_found = '<html>' + os.linesep + '<head>' + os.linesep + '  <title>Page Not Found</title>' \
                       + os.linesep + '</head>' + os.linesep + '<body>' + os.linesep \
                       + '  <h1>Sorry, the page ' + url + ' was not found.</h1>' + os.linesep + '</body>' \
                       + os.linesep + '</html>'
            self.connection.send(
                ('HTTP/1.1 404 Not Found' + os.linesep + os.linesep + page_not_found).encode(encoding='UTF-8'))

    def head_request(self, url):
        print('head ' + url)

        if os.path.isfile(url):
            self.connection.send(('HTTP/1.1 200 OK' + os.linesep + os.linesep).encode(encoding='UTF-8'))
        else:
            self.connection.send(('HTTP/1.1 404 Not Found' + os.linesep + os.linesep).encode(encoding='UTF-8'))

    dispatch = {
        'get': get_request,
        'head': head_request
    }

    def process_command(self, command, url):
        if command in self.dispatch:
            self.dispatch[command](self, url)
        else:
            print('Unknown command ' + command)

if __name__ == '__main__':
    server = HttpServer()
    server.start()
