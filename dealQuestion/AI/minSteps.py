# 交换字符串两个位置,i<j
def change(s,i,j):
    if i==j:
        return s
    a = min(i,j)
    b = max(i,j)
    return s[:a]+s[b]+s[a+1:b]+s[a]+s[b+1:]

def getMethod(s,white,st=200):#输入参数改为white
    # 存放未走过的情况
    queue = []
    a=s+"0 "
    # 标志走过的情况(优化)
    flag = {}
    flag[s]=1
    queue.append(a)
    while queue:
        p = queue[0]
        queue.remove(p)
        space = p.index(" ")
        step = int(p[9:space])
        me = p[space:]
        p=p[:9]
        # print(p,step)
        if step==st:
            return None
        if p=="012345678":
            return me[1:]
        
        pos = p.index(white)
        # 数组索引越界
        if(pos>=3):# 上
            s = change(p,pos-3,pos)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"w")
        if(pos<=5):# 下
            s = change(p,pos,pos+3)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"s")
        if(pos%3!=0):# 左
            s = change(p,pos-1,pos)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"a")
        if(pos%3!=2):# 右
            s = change(p,pos,pos+1)
            if(not flag.__contains__(s)):
                flag[s]=1
                queue.append(s+str(step+1)+me+"d")

# a=getMethod("012345678","8")
# print(a,len(a))
