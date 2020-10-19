'''
随机取一张图片,分割成9份,白块取决于getNum随机得到
'''
import os
import cv2
import base64
import random
import numpy as np
from PIL import Image
from createNum import getNum

def arrayToBase64(arr):
    retval, bu = cv2.imencode('.jpg', arr)
    return base64.b64encode(bu).decode()

def getImage():
    index = random.randint(0,34)
    # 存放36张图片的文件夹
    imgDir = "..\\data\\charImg\\"
    imgs = os.listdir(imgDir)
    arr = np.array(Image.open(imgDir+imgs[index]))
    # F特殊处理 两块黑的必须拿一块

    imgMap = {}
    num,pos = getNum()
    imgMap["pos"] = num
    imgMap["white"] = pos

    
    # 分为3*3
    for i in range(3):
        for j in range(3):
            subarray = arr[i*300:(i+1)*300,j*300:(j+1)*300]
            # np.array => base64
            imgMap[str(3*i+j)] = arrayToBase64(subarray)
            # if i*3+j==num.index(pos):
            #     arr[i*300:(i+1)*300,j*300:(j+1)*300]=np.full((300,300,3),255)

    whiteArray = np.array(Image.open("..\\data\\white.jpg"))
    imgMap["wImg"] = arrayToBase64(whiteArray)
    imgMap["newImg"] = arrayToBase64(arr)

    return imgMap
