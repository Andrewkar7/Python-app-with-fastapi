"""
Тесты, проверяющие, возвращают ли запрашивающие существующие хосты http status 100<=x<400.
"""

from my_app import is_alive_host


def test_alive_host():
    print(is_alive_host('semrush.com')) #True
    print(is_alive_host('https://www.google.com/doodles')) #True
    print(is_alive_host('https://yandex.com')) #True
    print(is_alive_host('http://vk.com')) #True


def test_down_host():
    print(is_alive_host('semrush.con')) #False
    print(is_alive_host('/google.com')) #False
    print(is_alive_host('https://yandex')) #False
    print(is_alive_host('https://vk.ua')) #False


test_alive_host()
test_down_host()
