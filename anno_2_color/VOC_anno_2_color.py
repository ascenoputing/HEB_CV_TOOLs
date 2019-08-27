#author:HuangEnbo
#是对LiuSi所用数据集的处理
#LIP给出的segmentation直接就是L模式
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

	# VOC 配色方案
	palette=[] 
	for i in range(256): 
		palette.extend((i,i,i)) 

	palette[:3*21]=np.array([[0, 0, 0],
                            [128, 0, 0],
                            [0, 128, 0],
                            [128, 128, 0],
                            [0, 0, 128],
                            [128, 0, 128],
                            [0, 128, 128],
                            [128, 128, 128],
                            [64, 0, 0],
                            [192, 0, 0],
                            [64, 128, 0],
                            [192, 128, 0],
                            [64, 0, 128],
                            [192, 0, 128],
                            [64, 128, 128],
                            [192, 128, 128],
                            [0, 64, 0],
                            [128, 64, 0],
                            [0, 192, 0],
                            [128, 192, 0],
                            [0, 64, 128]], dtype='uint8').flatten()


	for _, image in tqdm(zip(range(100000),os.listdir(path_org))):#image本身就是name
		img = Image.open(os.path.join(path_org,image))#注意这里的文件路径
		img.putpalette(palette)
		img.save(r''+path_p+'/'+image.split('.')[0]+'.png')




