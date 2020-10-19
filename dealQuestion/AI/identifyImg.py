import os
import numpy as np
from PIL import Image
from sklearn.externals import joblib

# 获取图片对应编号
def getNum(arrs):
    # load model
    clf = joblib.load('clf.pkl')

    ans = []
    dirindex = 0

    # arr是np.array数组
    for arr in arrs:
        # s1==0 白  s2==0 黑
        s1 = np.count_nonzero(arr==0)
        s2 = np.count_nonzero(arr==255)
        if s1==0:
            ans.append("白")
        elif s2==0:
            ans.append("黑")
        else:
            arr = arr[:,:,0]
            arr = arr.reshape(1,-1)
            pre = int(clf.predict(arr))
            dirindex=pre//10
            ans.append(pre)

    path = 'C:\\software\\char2\\'
    dirs = os.listdir(path)

    white = ans.index("白")

    matchNums = [i%10 for i in ans if isinstance(i,int)]
    noMatchNums = [i for i in range(9) if i not in matchNums]

    if "黑" not in ans:
        ans[ans.index("白")] = noMatchNums[0]
    else:
        # print(dirs[dirindex])
        img1path = path + dirs[dirindex] + "\\"
        files = os.listdir(img1path)
        img1path += files[noMatchNums[0]]
        arr = np.array(Image.open(img1path,"r"))
        if np.count_nonzero(arr==255) == 0:
            ans[ans.index("黑")] = noMatchNums[0]
            ans[ans.index("白")] = noMatchNums[1]
        else:
            ans[ans.index("黑")] = noMatchNums[1]
            ans[ans.index("白")] = noMatchNums[0]

    ans = [i%10 for i in ans]
    s = ""
    for l in ans:
        s+=str(l)
    # return ans,white
    return s,str(ans[white])