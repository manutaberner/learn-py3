import requests
import json

url = 'https://cutt.ly/api/api.php'
payload = {'longurl':'http://example.com'}

r = requests.post(url,json=payload)