"""
先用 下面 matlab 脚本将归一化矩阵转化为RGB矩阵

a = load('human_colormap.mat')
b = a.colormap * 255
c = fix(b) %取整
"""

import numpy, scipy.io 

mat = scipy.io.loadmat('CIHP_colormap')

print('type(mat){}\n\nmat:\n{}'.format(type(mat),mat))


"""
打印出来：
 array([[  0,   0,   0],
       [127,   0,   0],
       [254,   0,   0],
       [  0,  84,   0],
       [169,   0,  50],
       [254,  84,   0],
       [  0,   0,  84],
       [  0, 118, 220],
       [ 84,  84,   0],
       [  0,  84,  84],
       [ 84,  50,   0],
       [ 51,  85, 127],
       [  0, 127,   0],
       [  0,   0, 254],
       [ 50, 169, 220],
       [  0, 254, 254],
       [ 84, 254, 169],
       [169, 254,  84],
       [254, 254,   0],
       [254, 169,   0]], dtype=uint8)

"""
