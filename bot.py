import requests

key = open('../token_telegram', 'r').read()
url = 'https://api.telegram.org/bot'+key.strip()
resp = requests.get(url+'/getMe')

print(resp.json())

# Integrar com esta api:

# https://www.songsterr.com/a/wa/api/