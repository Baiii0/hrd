import os

path1 = "..\\data\\rank1.txt"
path2 = "..\\data\\rank2.txt"

def getMsg(path):
    f = open(path,"r")
    data = f.read()
    f.close()
    return data

def getRank():
    msg = {}
    d1 = getMsg(path1)
    d2 = getMsg(path2)
    msg['step']=d1
    msg['time']=d2
    return msg

def dealDate(date):
    d = date.split(" ")
    return d[3]+"-"+d[1]+"-"+d[2]+"-"+d[4]

def msgToString(rank,step,date,isDeal=True):
    if isDeal:
        date = dealDate(date)
    return "rank:{} step:{} date:{}<br/>\n".format(rank,step,date)

def msgToString2(rank,time,date,isDeal=True):
    if isDeal:
        date = dealDate(date)
    return "rank:{} time:{} date:{}<br/>\n".format(rank,time,date)

#path1是步数 path2是时间
def writedata(value1,value2,date):
    f = open(path1,"r")
    data = f.readlines()
    f.close()
    f2 = open(path2,"r")
    data2 = f2.readlines()
    f2.close()

    f = open(path1,"w")
    f2 = open(path2,"w")
    flag = 1
    flag2 = 1
    if not len(data):
        f.writelines(msgToString(1,value1,date))
        f2.writelines(msgToString2(1,value2,date))
    else:
        for i in range(len(data)):
            step = int(data[i].split(" ")[1][5:])
            time = int(data2[i].split(" ")[1][5:])
            oridate = data[i].split(" ")[2][5:-6]
            oridate2 = data2[i].split(" ")[2][5:-6]
            if value1<step and flag:
                f.writelines(msgToString(i+1,value1,date))
                flag = 0
            if flag:
                f.writelines(msgToString(i+1,step,oridate,False))
            else:
                f.writelines(msgToString(i+2,step,oridate,False))

            if value2<time and flag2:
                f2.writelines(msgToString2(i+1,value2,date))
                flag2 = 0
            if flag2:
                f2.writelines(msgToString2(i+1,time,oridate2,False))
            else:
                f2.writelines(msgToString2(i+2,time,oridate2,False))
        if flag:
            f.writelines(msgToString(len(data)+1,value1,date))
        if flag2:
            f2.writelines(msgToString2(len(data)+1,value2,date))
    f.close()
    f2.close()