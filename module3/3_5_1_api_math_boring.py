import requests, re

# api_url = "http://numbersapi.com/31/math?json=true"

params = {
    'json': "true"
}

url = 'http://numbersapi.com/'

with open('1.txt', 'r') as f:
     for line in f:
         api_url = url + '/' + str(line.strip()) + '/math'
        #  print(api_url)
         res = requests.get(api_url, params=params)
         data = res.json()
        #  print(data)
         if data['found'] == True:
             print('Interesting')
         else:
             print('Boring')