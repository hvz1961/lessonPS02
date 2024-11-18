import requests
import pprint

# params = {
#     'q' : 'html'
# }
#
# response = requests.get('https://api.github.com/search/repositories', params=params)
# response = requests.get('https://www.google.com')
# print(response.status_code)
# print(response.ok)
# if response.ok:
#     print('запрос успешно выполнен')
# else:
#     print('произошла ошибка')

# print(response.text) # для вывода текста
# print(response.content) # для вывода файла: ответ выводится в байтах
# response_json = response.json()
# pprint.pprint(response_json) # для удобного вывода словаря в столбец
# print(f'количество репозиториев с кодом HTML: {response_json['total_count']}') #
# img = 'https://m-files.cdnvideo.ru/lpfile/8/5/e/85e44d56c41a294466478550e1efdb78/-/crop/0x0x1920x2715/-/resize/356/-/resize/1920/f.png?41346651'
# response = requests.get(img)
#
# with open('test.jpg', 'wb') as file:
#     file.write(response.content)

url = 'https://jsonplaceholder.typicode.com/posts'

data = {
    'title' : 'foo'
}

response = requests.post(url, data=data)

print(response.status_code)

print(f'ответ - {response.json()}')

