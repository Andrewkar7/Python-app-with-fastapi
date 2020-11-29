"""
Разворачиваем вокруг функции is_alive_host веб сервис c помощью fastapi
"""
from fastapi import FastAPI
from my_app import is_alive_host

app = FastAPI()


@app.get("/healthz")
def root(hostname):
    response_code = is_alive_host(hostname)
    return {"status": "up"} if response_code else {"status": "down"}

# Для запуска используем ссылку типа: your_service.loc:8001/healthz?hostname=
# где после "=" вставляем интересующий нас хостинг
