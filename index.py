import requests
import json

headers = {"Authorization": "Token mytoken"}

response = requests.get('https://mysite.wancorarh.com.br/api/v1/vagas', headers=headers)
results = json.loads(response.text)

print(json.dumps(results, indent=4))