import requests

url = "https://www.baidu.com"

response = requests.get(url)

assert response.status_code == 200
