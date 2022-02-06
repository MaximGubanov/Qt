import socket

from models.databases import Session, User


class CheckPort():

    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"Значение должно быть типа ")
        if not (1 <= value <= 9999):
            raise ValueError(f"Порт не может быть отрицательным числом")
        return setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Невозможно удалить атрибут")


class Socket(socket.socket):

    def __init__(self):
        super(Socket, self).__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.address = '127.0.0.1'
        self.port = 7770
        self.session = Session()

    def listen_socket(self, listened_socket=None):
        raise NotImplementedError

    def send_data(self, data, sock):
        raise NotImplementedError

    def set_connect(self):
        raise NotImplementedError

    def insert_bd(self, client_socket, address, passsword):
        user = User(client_socket, address, passsword)
        self.session.add(user)
        self.session.commit()
        self.session.close()