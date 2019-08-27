# author:HuangEnbo
# 是对CIHP所用数据集的处理，使用CIHP配色方案
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

	#CIHP配色方案
	palette=[] 
	for i in range(256): 
		palette.extend((i,i,i)) 

	palette[:3*21]=np.array([[  0,   0,   0],#bkg
					       [127,   0,   0],  #hat
					       [254,   0,   0],  #hair
					       [  0,  84,   0],  #glove
					       [169,   0,  50], #s-gls
					       [254,  84,   0], #u-cloth
					       [  0,   0,  84], #dress
					       [  0, 118, 220], #coat
					       [ 84,  84,   0], #socks
					       [  0,  84,  84], #pants
					       [ 84,  50,   0], #jumpsuits
					       [ 51,  85, 127], # scarf
					       [  0, 127,   0], #skirt
					       [  0,   0, 254], #face
					       [ 50, 169, 220], #l-arm
					       [  0, 254, 254], #r-arm
					       [ 84, 254, 169], #l-leg
					       [169, 254,  84], # r-leg
					       [254, 254,   0], #l-shoe
					       [254, 169,   0], #r-shoe
					       ], dtype=uint8).flatten()



	for _, image in tqdm(zip(range(100000),os.listdir(path_org))):#image本身就是name
	
		img = Image.open(os.path.join(path_org,image)) #注意这里要用绝对路径
		img.putpalette(palette)
		img.save(r''+path_p+'/'+image.split('.')[0]+'.png')




