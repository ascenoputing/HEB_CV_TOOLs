# author:HuangEnbo
# 是对LiuSi所用数据集的处理，使用LIP配色方案
# LIP给出的segmentation直接就是L模式
import os
import numpy as np 

from tqdm import tqdm
from PIL import Image


if __name__ == '__main__':

	magic_num = 2  # 1：atr， 2：lip， 3：cihp

	class_num = 20

	# source
	path1 = './atr_results'
	path2 = './lip_results'
	path3 = './cihp_results'

	# pcolor
	path4 = './atr_pcolor'
	path5 = './lip_pcolor'
	path6 = './cihp_pcolor'

	path_all = [path1,path2,path3,path4,path5,path6]

	path_org = path_all[magic_num-1] # label path
	
	path_p = path_all[magic_num+3] # p_label path

	#LIP配色方案
	palette=[] 
	for i in range(256): 
		palette.extend((i,i,i)) 

	palette[:3*21]=np.array([[0, 0, 0], #bkg
                            [125, 20, 20],#hat
                            [255, 0, 0],#hair
                            [28, 85, 42],#glove
                            [218, 38, 78],#s-gls
                            [252, 81, 4],#u-cloth
                            [0, 0, 109],#dress
                            [40, 118, 186],#coat
                            [84, 86, 36],#socks
                            [0, 102, 102],#pants
                            [84, 54, 20],#jumpsuits
                            [51, 88, 128],#scarf
                            [12, 128, 64],#skirt
                            [3, 33, 253],#face
                            [42, 170, 222],#l-arm
                            [110, 205, 221],#r-arm
                            [167, 244, 114],#l-leg
                            [204, 255, 51],#r-leg
                            [243, 236, 11],#l-shoe
                            [251, 169, 25],#r-shoe
                            ], dtype='uint8').flatten()


	for _, image in tqdm(zip(range(100000),os.listdir(path_org))):#image本身就是name
	
		img = Image.open(os.path.join(path_org,image)) #注意这里要用绝对路径
		img.putpalette(palette)
		img.save(r''+path_p+'/'+image.split('.')[0]+'.png')




