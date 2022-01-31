from tabulate import tabulate
import subprocess
from task2 import host_range_ping


def ping(ip):
    """Ф-я проверяет доступность ip-адреса, взависимости от результата возвращает соответсвующее булевое значение"""
    result_ping = subprocess.run(f'ping {ip} -c 1', shell=True)
    if result_ping.returncode == 0:
        return True
    else:
        return False


def create_tuples_list():
    """Ф-я создает и два списка доступных и не доступных ip-адресов, затем создает и возвращает список кортежей.
     Кортеж состоит из двух эл-в. Первый доступный адресс, второй - нет"""
    reachable_list = []
    unreachable_list = []
    range_ip = host_range_ping('87.250.250.230', '87.250.250.254')

    for ip in range_ip:
        check_ip = ping(ip)
        if check_ip:
            reachable_list.append(ip)
            unreachable_list.append('----')
        else:
            unreachable_list.append(ip)

    zipped_list = list(zip(reachable_list, unreachable_list))
    return zipped_list


def host_range_ping_tab(tuples_list):
    columns = (['Reachable', 'Unreachable'])
    print(tabulate(tuples_list, headers=columns))


if __name__ == '__main__':
    tuples_list = create_tuples_list()
    host_range_ping_tab(tuples_list)

    """Результат:
    
        Reachable       Unreachable
        --------------  --------------
        87.250.250.230  ----
        87.250.250.231  ----
        87.250.250.232  ----
        87.250.250.233  ----
        87.250.250.235  87.250.250.234
        87.250.250.239  ----
        87.250.250.240  87.250.250.236
        87.250.250.242  87.250.250.237
        87.250.250.243  87.250.250.238
        87.250.250.244  ----
        87.250.250.245  ----
        87.250.250.246  87.250.250.241
        87.250.250.247  ----
        87.250.250.248  ----
        87.250.250.249  ----
        87.250.250.250  ----
        87.250.250.251  ----
        87.250.250.252  ----
        87.250.250.254  ----
    """