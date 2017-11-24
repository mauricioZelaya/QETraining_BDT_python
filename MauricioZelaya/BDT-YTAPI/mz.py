import requests

r = requests.get('https://api.github.com/events')
dict = r.json()

print("values \n", dict)
# print("CODe \n", r.status_code)
