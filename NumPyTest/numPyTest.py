import numpy as np

arr = np.random.rand(4,4)
randMat = np.mat(arr)               #生成矩阵

print(randMat)

invRandMat = randMat.I              #矩阵求逆
print(invRandMat)

myEye = randMat*invRandMat          #矩阵相乘
print(myEye)

eye = np.eye(4)                           #创建4*4单位矩阵
print(myEye - eye)