def getMethod(s,white,s2):#输入参数改为white
    # 存放未走过的情况
    queue = []
    a=s+"0 "
    # 标志走过的情况(优化)
    flag = {}
    queue.append(a)
    while queue:
        p = queue[0]
        queue.remove(p)
        space = p.index(" ")
        step = int(p[9:space])
        me = p[space:]
        p=p[:9]

        if p==s2:
            return me[1:]
        flag[p]=1
        
        pos = p.index(white)
        # 数组索引越界
        if(pos>=3):# 上
            s=p[0:pos-3]+p[pos]+p[pos-2:pos]+p[pos-3]+p[pos+1:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"w")
        if(pos<=5):# 下
            s=p[0:pos]+p[pos+3]+p[pos+1:pos+3]+p[pos]+p[pos+4:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"s")
        if(pos%3!=0):# 左
            s=p[0:pos-1]+p[pos]+p[pos-1]+p[pos+1:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"a")
        if(pos%3!=2):# 右
            s=p[0:pos]+p[pos+1]+p[pos]+p[pos+2:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"d")

# 交换字符串两个位置,i<j
def change(s,i,j):
    if i==j:
        return s
    a = min(i,j)
    b = max(i,j)
    return s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]

step = 15
swap = [2, 7]
nums = "062857431"
white = "8"
s = change("012345678",swap[0]-1,swap[1]-1)
# k = getMethod(nums,white,s)
# print(k,len(k))
lis = [[i,j] for i in range(9) for j in range(9) if i<j]
for li in lis:
    s2 = change(s,li[0],li[1])
    k = getMethod(nums,white,s2)
    if k:
        print(k,len(k))