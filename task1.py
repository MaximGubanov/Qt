import ipaddress
import subprocess


def create_ip(ip, n, i=0):
    """Ф-я создает диапозон 'n' адресов
    ip - стартовый адресс
    n - кол-во адресов"""
    try:
        list_ipv4 = [ipaddress.ip_address(ip)]
        while len(list_ipv4) < n:
            ipv4 = ipaddress.ip_address(list_ipv4[0] + 1)
            list_ipv4.append(ipv4 + i)
            i += 1
        return list_ipv4
    except ValueError as err:
        print('Неверный формат ip-адресса')


def host_ping(ip_list):
    print(ip_list)
    for ip in ip_list:
        print(f'Проверка адреса {ip}...')
        result_ping = subprocess.run(f'ping {ip} -c 1', shell=True)
        print(f'{ip} - узел доступен') if result_ping.returncode == 0 else print(f'{ip} - узел недоступен')


if __name__ == '__main__':
    try:
        host_ping(create_ip('120.0.0.1', 2))
    except KeyboardInterrupt:
        print('Выход из программы')
        exit()

