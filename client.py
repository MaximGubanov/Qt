import sys
import threading

from main import Socket


class ClientVerifier(type):
    def __init__(self, clsname, base, clsdict):
        type.__init__(self, clsname, base, clsdict)


class BaseClient(metaclass=ClientVerifier):
    pass


class Client(BaseClient, Socket):
    def __init__(self):
        super(Client, self).__init__()

    def set_connect(self):
        self.connect((self.address, self.port))
        listen_thread = threading.Thread(target=self.listen_socket)
        listen_thread.start()
        self.start_client()

    def listen_socket(self, listened_socket=None, address=None):
        while True:
            data = self.recv(2048)
            print(data.decode('utf-8'))

    def send_data(self, data, sock=None):
        self.send(data.encode('utf-8'))

    def start_client(self):
        name = input('Введите имя: ')
        if name != '':
            self.send_data(f'{name} -> присоединился к чату')
            while True:
                data = input('::: ')
                if data == 'exit':
                    self.send(f'{name} -> покинул чат')
                    break
                else:
                    self.send_data(data)

                    send_thread = threading.Thread(target=self.send_data, args=(data,))
                    send_thread.start()
        else:
            print('Имя не должно быть пустым.')
            sys.exit()

        sys.exit()


if __name__ == '__main__':
    client = Client()
    client.set_connect()
    client.insert_bd('Nick', 'Perov', '123454321')