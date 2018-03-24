import requests
response = requests.get('https://httpbin.org/ip')
print('Your IP is {0}'.format(reponse.json()['origin']))
