import socket
import threading

from main import Socket


class Server(Socket):
    def __init__(self):
        super(Server, self).__init__()
        self.clients = []

    def set_connect(self):
        self.bind((self.address, self.port))
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen(5)

    def send_data(self, data, sock):
        for client in self.clients:
            if client != sock:
                client.send(data)

    def listen_socket(self, listened_socket=None):
        while True:
            data = listened_socket.recv(2048)
            self.send_data(data, sock=listened_socket)

    def start_server(self):
        print('[SERVER STARTED]')

        while True:
            client_socket, address = self.accept()
            print(f'User {address} connected to server')
            self.clients.append(client_socket)

            accepted_client = threading.Thread(
                target=self.listen_socket,
                args=(client_socket,)
            )

            accepted_client.start()


if __name__ == '__main__':
    server = Server()
    server.set_connect()
    server.start_server()