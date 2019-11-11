import json
import requests
# from .fanyi import parse_url



url = ""
response = requests.post(url)

html_str = response.parse_url(url)
rest1 = json.loads(html_str)
print(rest1)

