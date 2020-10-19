def getMethod(s,white_pos):#输入参数改为white
    # 存放未走过的情况
    queue = []
    a=s+"0 "
    # 标志走过的情况(优化)
    flag = {}
    white = white_pos
    queue.append(a)
    while queue:
        p = queue[0]
        queue.remove(p)
        space = p.index(" ")
        step = int(p[9:space])
        me = p[space:]
        p=p[:9]
        # print(p+"\t"+str(step)+"\t"+me)
        #012345678
        if p=="012345678":
            return me[1:]
        flag[p]=1
        
        pos = p.index(white)
        # 数组索引越界
        if(pos>=3):# 上
            s=p[0:pos-3]+p[pos]+p[pos-2:pos]+p[pos-3]+p[pos+1:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+str(pos-3))
        if(pos<=5):# 下
            s=p[0:pos]+p[pos+3]+p[pos+1:pos+3]+p[pos]+p[pos+4:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+str(pos+3))
        if(pos%3!=0):# 左
            s=p[0:pos-1]+p[pos]+p[pos-1]+p[pos+1:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+str(pos-1))
        if(pos%3!=2):# 右
            s=p[0:pos]+p[pos+1]+p[pos]+p[pos+2:]
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+str(pos+1))

# 交换字符串两个位置,i<j
def change(s,i,j):
    if i==j:
        return s
    a = min(i,j)
    b = max(i,j)
    return s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]