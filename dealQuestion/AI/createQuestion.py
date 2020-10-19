import requests

url = "http://47.102.118.1:8089/api/challenge/create"

data = {
    "teamid": 23,
    "data": {
        "letter": "q",
        "exclude": 3,
        "challenge": [
            [1, 2, 8],
            [4, 5, 6],
            [7, 0, 9]
        ],
        "step": 2,
        "swap": [3,8]
    },
    "token": "5d083062-687f-4d42-afc0-e3c400fda8b2"
}

r = requests.post(url,json=data)
print(r.text)