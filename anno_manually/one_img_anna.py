# author:HuangEnbo
# 是对手工标注数据的处理
# 手工标注的结果是RGB模式，需要先转换，保存时也有技巧
# 本程序只负责对单张.png进行处理

import os
import numpy as np 

from tqdm import tqdm
from PIL import Image



if __name__ == '__main__':

        np.set_printoptions(threshold=np.inf) #打印时全部打印出来，不打省略号

        image = '01.png' # 此时的.png 其实是RGB模式

        #LIP配色方案
        palette=[] 
        for i in range(256): 
              palette.extend((i,i,i)) 

        palette[:3*21]=np.array([[0, 0, 0], #bkg    0
                            [125, 20, 20],#hat     1
                            [255, 0, 0],#hair      2
                            [28, 85, 42],#glove    3
                            [218, 38, 78],#s-gls   4
                            [252, 81, 4],#u-cloth  5
                            [0, 0, 109],#dress     6
                            [40, 118, 186],#coat   7
                            [84, 86, 36],#socks    8
                            [0, 102, 102],#pants   9
                            [84, 54, 20],#jumpsuits 10
                            [51, 88, 128],#scarf    11
                            [12, 128, 64],#skirt    12
                            [3, 33, 253],#face      13
                            [42, 170, 222],#l-arm   14
                            [110, 205, 221],#r-arm  15 
                            [167, 244, 114],#l-leg  16
                            [204, 255, 51],#r-leg   17 
                            [243, 236, 11],#l-shoe  18 
                            [251, 169, 25],#r-shoe  19
                            ], dtype='uint8').flatten()

                
        encoded = np.array(Image.open(image))

        annotation = np.bitwise_or(np.bitwise_or( # RGB 模式转换为单通道，每个像素等于label标签, 来自标注工具的readme文件
                encoded[:, :, 0].astype(np.uint32),
                encoded[:, :, 1].astype(np.uint32) << 8),
                encoded[:, :, 2].astype(np.uint32) << 16)

        #print("annotation:{}\n".format(annotation))
        #print("annotation.shape:{}".format(annotation.shape))
        #print(np.unique(annotation))

        anno = Image.fromarray(np.uint8(annotation)) #只有这种方法能够保证image的像素是numpy array的原值

        anno.putpalette(palette)
        anno.save(r'annatater'+image.split('.')[0]+'.png')




