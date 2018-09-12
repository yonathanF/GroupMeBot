''' interfaces with the groupme api '''

import requests

url = "https://api.groupme.com/v3/groups?token=L0a0LxWESXGXSHvug2FAxZcx00VfkEX5mZWCnNWX"
url = "https://api.groupme.com/v3/bots/post?bot_id=8103e25ed9d4d3193892f2518a&text=Hello+world"
test_request = requests.post(url)

print(test_request)
