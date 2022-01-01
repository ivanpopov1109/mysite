import requests

url = 'http://localhost:8000/api/'  # Полный адрес эндпоинта
response = requests.get(url)  # Делаем GET-запрос
# Поскольку данные пришли в формате json, переведем их в python
response_on_python = response.json()
# Запишем полученные данные в файл news.txt
with open('news.txt', 'w') as file:
    for news in response_on_python:
        file.write(f'{news}')
