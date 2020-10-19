import requests,json,base64
from PIL import Image
import numpy as np
from identifyImg import getNum
from minSteps import getMethod,change

url = "http://47.102.118.1:8089/api/challenge/start/dbc40db2-15f9-4e7e-a7b2-a64625c404d8" # 获取赛题的接口

teamdata = {
    "teamid": 23,
    "token": "5d083062-687f-4d42-afc0-e3c400fda8b2"
}

r = requests.post(url,json=teamdata)
# print(r.text)
datadir = json.loads(r.text)
data = datadir['data']
imgdata=base64.b64decode(data['img'])
chanceleft=datadir['chanceleft']
step=data['step']
swap=data['swap']
uuid=datadir['uuid']
# print(chanceleft,step,swap,uuid)

path = "C:\\software\\char.jpg"
file=open(path,'wb')
file.write(imgdata)
file.close() 

arrlist = []
f = Image.open('C:\\software\\char.jpg',"r")
array = np.array(f)
for i in range(3):
    for j in range(3):
        subarray = array[i*300:(i+1)*300,j*300:(j+1)*300]
        arrlist.append(subarray)

# nums为相应的序号,white为白色的索引
nums,white = getNum(arrlist)

# step = 1
# swap = [2,1]
# nums = "012435678"
# white = "4"
aa,bb = swap

ww = open("C:\\software\\flag\\"+white+".txt")
qq = ww.read()
pflag = qq.split("\n")
ww.close()

ww = open("C:\\software\\ans\\"+white+".txt")
qq = ww.read()
pans = qq.split("\n")
ww.close()

post_swap = None
post_ope = None
minsteps = 100

queue = []
flag = {}
flag2 = {}
flag3 = {}
# 也可以放前面
lis = [[i,j] for i in range(9) for j in range(9) if i<j]
# flag[nums]=1
queue.append(nums+"0 ")
while queue:
    p = queue[0]
    queue.remove(p)
    space = p.index(" ")
    # 步数
    step2 = int(p[9:space])
    # 空格+序列
    me = p[space:]
    # 字符串
    p=p[:9]
    # print(p,step2,me)
    if p=="012345678":
        if step2<=step:#----------------------------------------------------有改动
            post_swap = []
            post_ope = me[1:]
        break
    if step2 == step:
        s = change(p,aa-1,bb-1)
        if flag2.__contains__(s):
            continue
        else:
            flag2[s] = 1
        if s in pflag:
            ins = pflag.index(s)
            method = pans[ins]
            if len(me[1:]+method)<minsteps:
                post_swap = []
                post_ope = me[1:]+method
                minsteps = len(post_ope)
                # print("[]",post_ope,str(minsteps))
        else:
            for li in lis:
                # 优化2 已经出现过就不用再试了仅对需要交换的而言
                s2 = change(s,li[0],li[1])
                if flag3.__contains__(s2):
                    continue
                else:
                    flag3[s2] = 1
                if s2 in pflag:
                    ins = pflag.index(s2)
                    method = pans[ins]
                    if len(me[1:]+method)<minsteps:
                        post_swap = [li[0]+1,li[1]+1]
                        post_ope = me[1:]+method
                        minsteps = len(post_ope)
                        # print(post_swap,post_ope,str(minsteps))  
        # if minsteps == 24:
        #     break   
    if step2<step:
        pos = p.index(white)
        if(pos>=3):# 上
            s = change(p,pos-3,pos)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step2+1)+me+"w")
        if(pos<=5):# 下
            s = change(p,pos,pos+3)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step2+1)+me+"s")
        if(pos%3!=0):# 左
            s = change(p,pos-1,pos)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step2+1)+me+"a")
        if(pos%3!=2):# 右
            s = change(p,pos,pos+1)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step2+1)+me+"d")

url="http://47.102.118.1:8089/api/challenge/submit"
postdata = {
    "uuid": uuid,
    "teamid": 23,
    "token": "5d083062-687f-4d42-afc0-e3c400fda8b2",
    "answer": {
        "operations": post_ope,
        "swap": post_swap
    }
}

r = requests.post(url,json=postdata)

print(chanceleft,step,swap,uuid)
print(nums,white)
print(post_swap,post_ope)
print(r.text)