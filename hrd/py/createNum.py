'''
随机生成一个偶逆序数列
'''
import random
from minSteps import getMethod

# def connectArr(arr):
#     s = ""
#     for i in arr:
#         s += str(i)
#     return s


# 生成30*9种有解的序列,玩到最后发现无解的话,很难受,
# 保存在文档,否则临时生成速度太慢

# arr = [1,2,3,4,5,6,7,8,0]
# f = open("C:\\software\\nums.txt","w")
# for i in range(9):
#     t = 30
#     while t>0:
#         random.shuffle(arr)
#         s = connectArr(arr)
#         k = getMethod(s,str(i))
#         if k and len(k)>10:
#             f.writelines(s+" "+str(i)+"\n")
#             t -= 1
#             print(t)
# f.close()

def getNum():
    f = open("..\\data\\nums.txt","r")
    t = f.read()
    f.close()
    a = t.split("\n")
    index = random.randint(0,len(a)-1)
    t = a[index]
    return t[:9],t[-1]