import requests,json

url = "http://47.102.118.1:8089/api/challenge/start/e8aaf981-7ba1-4d36-b80e-a6a16debe587" # 获取赛题的接口

teamdata = {
    "teamid": 23,
    "token": "5d083062-687f-4d42-afc0-e3c400fda8b2"
}

r = requests.post(url,json=teamdata)
datadir = json.loads(r.text)

url2 = "http://47.102.118.1:8089/api/challenge/submit"
postdata = {
    "uuid": datadir['uuid'],
    "teamid": 23,
    "token": "5d083062-687f-4d42-afc0-e3c400fda8b2",
    "answer": {
        "operations": "d",
        "swap": []
    }
}

r = requests.post(url2,json=postdata)
print(r.text)