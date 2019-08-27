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
					       [  0,  84,   0],  #s-gls 
					       [169,   0,  50],  #u-cloth
					       [254,  84,   0],  #dress
					       [  0,   0,  84],  #coat
					       [  0, 118, 220],  #socks
					       [ 84,  84,   0],  #pants
					       [  0,  84,  84],  #glove
					       [ 84,  50,   0],  #scarf
					       [ 51,  85, 127],  #skirt 
					       [  0, 127,   0],  #torso-skin
					       [  0,   0, 254],  #face
					       [ 50, 169, 220],  #r-arm
					       [  0, 254, 254],  #l-arm
					       [ 84, 254, 169],  #r-leg
					       [169, 254,  84],  #l-leg
					       [254, 254,   0],  #r-shoe
					       [254, 169,   0],  #l-shoe
					       ], dtype=uint8).flatten()



	for _, image in tqdm(zip(range(100000),os.listdir(path_org))):#image本身就是name
	
		img = Image.open(os.path.join(path_org,image)) #注意这里要用绝对路径
		img.putpalette(palette)
		img.save(r''+path_p+'/'+image.split('.')[0]+'.png')




