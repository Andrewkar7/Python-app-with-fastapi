"""
Проверить, что запрашиваемый хост возвращает http status 100<=x<400.
"""
import requests


def is_alive_host(hostname):
    if 'http://' not in hostname and 'https://' not in hostname:
        hostname = 'https://' + hostname
    try:
        response = requests.get(hostname).status_code
        # print(response)
    except:
        response = 0

    return True if 100 <= response < 400 else False
