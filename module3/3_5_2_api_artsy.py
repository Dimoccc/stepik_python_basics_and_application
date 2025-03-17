# В этой задаче вам необходимо воспользоваться API сайта artsy.net

# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.


import requests
import json

credentials = {}

with open('client_id.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            credentials[key] = value

print(credentials)

client_id = credentials.get('Client_Id')
client_secret = credentials.get('Client_Secret')
print(client_id,client_secret)

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
r = requests.get("https://api.artsy.net/api/artists/4d8b92b34eb68a1b2c0003f4", headers=headers)

# разбираем ответ сервера
j = json.loads(r.text)


artist_info = {}

with open('1.txt', 'r') as f:
     for line in f:
         request_data = requests.get("https://api.artsy.net/api/artists/" + str(line.strip()),headers=headers)
        #  print(api_url)
         request_data.encoding = 'utf-8'
        #  print(request_data.text)
        #  print(10*"*")
         res_j = json.loads(request_data.text)
        #  print(res_j)
        #  print(10*"*")
         artist_info[res_j['sortable_name']] = res_j['birthday']
         print(artist_info)
         sorted_by_year = dict(sorted(artist_info.items(), key=lambda x: int(x[1])))
         print(sorted_by_year)
for k in sorted_by_year:
    print(k)
         