import socket


class Socket(socket.socket):

    def __init__(self):
        super(Socket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.address = '127.0.0.1'
        self.port = 7770

    def listen_socket(self, listened_socket=None):
        raise NotImplementedError

    def send_data(self, data, sock):
        raise NotImplementedError

    def set_connect(self):
        raise NotImplementedError