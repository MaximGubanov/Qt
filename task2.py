import ipaddress
from functools import reduce
from pprint import pprint


def split_ip(ip):
    """Ф-я разбивает ip-адрес на две части и возвращает кортеж из двух элементов: строки и целого числа.
    Пример: '192.168.1.12' -> ('192.168.1', 12) """
    try:
        ip, last_oktet = ip.split('.')[:3], ip.split('.').pop(-1)
        ip = reduce(lambda x, y: f'{x}.{y}', ip)
        return (ip, last_oktet)
    except ValueError:
        print('Неверный формат ip-фдреса')
        exit()


def host_range_ping(ip1, ip2, n=1):
    """Ф-я принимает двапараметра левого и правого диапозона ip-адресов и выводит их в конслоль в порядке очереди
    ip1 - левый параметр,
    ip2 - правый,
    n - счётчик итерраций, по умолчанию равен 1
    Пример:
        func('192.168.1.1', '192.168.1.4')
        Вывод в консоль:
        -> 192.168.1.1
        -> 192.168.1.2
        -> 192.168.1.3
        -> 192.168.1.4
    Присечание: ip1 должен быть меньше ip2
    """
    range_ip_list = []
    right_ip, start_oktet = split_ip(ip1)
    left_ip, end_oktet = split_ip(ip2)

    start = ipaddress.ip_address(f'{right_ip}.{start_oktet}')
    end = ipaddress.ip_address(f'{left_ip}.{end_oktet}')

    if start < end and right_ip == left_ip:
        while start <= end:
            # print(start)
            range_ip_list.append(start)
            start = start + n

        return range_ip_list

    else:
        print('Правый аргумент диапозона должен быть меньше левого.\n'
              'Задайте правильный порядок.')


if __name__ == '__main__':
    result = host_range_ping('192.168.1.10', '192.168.1.19')
    pprint(result)