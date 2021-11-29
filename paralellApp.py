import time 
import requests
import concurrent.futures

URL = 'https://jsonplaceholder.typicode.com/posts'

def fetch_single(url: str):
	print('Отправка запроса\n')
	requests.get(url)
	return 'Ответ получен!\n'

time_start = time.time()

with concurrent.futures.ThreadPoolExecutor() as tpe:
	results = [tpe.submit(fetch_single, URL) for _ in range(1000)]
	for f in concurrent.futures.as_completed(results):
		print(f.result())

time_end = time.time()
print(f'\nРабота завершеня (параллельное выполнение). Время: {round(time_end - time_start, 2)} секунд')
input()