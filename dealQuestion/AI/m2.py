import requests,json,base64
from PIL import Image
import numpy as np
from identifyImg import getNum
from minSteps import getMethod,change

step = 15
swap = [2,7]
nums = "062857431"
white = "8"
aa,bb = swap
# 最优解10

ww = open("C:\\software\\flag\\"+white+".txt")
qq = ww.read()
pflag = qq.split("\n")
ww.close()

ww = open("C:\\software\\ans\\"+white+".txt")
qq = ww.read()
pans = qq.split("\n")
ww.close()
# print(pans[1])

post_swap = None
post_ope = None
minsteps = 100

queue = []
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
    # 测试一下
    if p=="012345678":
        # <= ? =
        if step2<step:
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
                print("[]",post_ope,str(minsteps))
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
                        print(post_swap,post_ope,str(minsteps))  
        # if minsteps == 26:# 提交好像会少一步 step=15 这里要16
        #     break   
    if step2<step:
        pos = p.index(white)
        if(pos>=3):# 上
            s = change(p,pos-3,pos)
            queue.append(s+str(step2+1)+me+"w")
        if(pos<=5):# 下
            s = change(p,pos,pos+3)
            queue.append(s+str(step2+1)+me+"s")
        if(pos%3!=0):# 左
            s = change(p,pos-1,pos)
            queue.append(s+str(step2+1)+me+"a")
        if(pos%3!=2):# 右
            s = change(p,pos,pos+1)
            queue.append(s+str(step2+1)+me+"d")