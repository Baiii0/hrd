import os
import numpy as np
from PIL import Image
from sklearn.neighbors import KNeighborsClassifier
from sklearn.externals import joblib


path = 'C:\\software\\char2\\'
dirs = os.listdir(path)
length = len(dirs)

X_train=[]
y_train=[]
for j in range(length):
    dirpath = path + dirs[j] + "\\"
    names = os.listdir(dirpath)
    for i in range(len(names)):
        f = Image.open(dirpath+names[i],"r")
        # 灰度模式判断是不是纯黑
        extrema = f.convert("L").getextrema()
        if extrema == (0, 0):
            continue

        image = np.array(f)
        image = image[:,:,0]
        image = image.reshape(1,-1)
        
        X_train.append(image)
        y_train.append(j*10+i)

X_train = np.array(X_train)
y_train = np.array(y_train)

X_train = X_train.reshape(X_train.shape[0],-1)

clf = KNeighborsClassifier(1)
clf.fit(X_train,y_train)

#save model
joblib.dump(clf, 'clf.pkl')