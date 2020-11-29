# python_intern
---

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc

## Что сделано

- Реализована функция is_alive_host в приложении my_app.py.
- Написаны тесты для проверки релевантных адресов и несуществующих в my_tests.py
- Развернут вокруг функции веб сервис с помощью fastapi<br/>
  Запускаем сервер с помощью <br/>
  ``` >> uvicorn my_api:app --host 0.0.0.0 --port 8000 ```<br/>
  Вводим в командной строке <br/> 
  ``` >> curl your_service.loc:8000/healthz?hostname= ```<br/>
  где после "=" вставляем интересующий нас хостинг
- Завернуто приложение в докер, ссылка на репозиторий <br/>
 ``` >> https://hub.docker.com/repository/docker/andrewkar7/python-fastapi-app ```<br/>
  Загружаем контейнер <br/>
  ``` >> sudo docker pull andrewkar7/python-fastapi-app:0.1 ```<br/>
  Запускаем <br/>
  ``` >> sudo docker run -p 8000:8000 -d andrewkar7/python-fastapi-app:0.1 ```
  
P.S. Работа проделана на OC Linux. 
