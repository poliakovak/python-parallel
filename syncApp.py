import time 
import requests


URL = 'https://jsonplaceholder.typicode.com/posts'

def fetch_single(url: str) -> None:
	print('Отправка запроса')
	requests.get(url)
	print('Ответ получен!')


time_start = time.time()
for _ in range(1000):
	fetch_single(URL)

time_end = time.time()
print(f'\nРабота завершеня. Время: {round(time_end - time_start, 2)} секунд')
input()
