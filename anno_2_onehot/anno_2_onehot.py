#author:HuangEnbo
#是对LiuSi所用数据集的处理
import os
import numpy as np 

from tqdm import tqdm
from PIL import Image


if __name__ == '__main__':

	phase_num = 2 # 1：train phase, 2: valition phase

	class_num = 20

	path1 = './datasets/Lip/train_segmentations'
	path2 = './datasets/Lip/val_segmentations'
	path3 = './datasets/Lip/train_onehot'
	path4 = './datasets/Lip/val_onehot'

	path_all = [path1,path2,path3,path4]

	path_org = path_all[phase_num-1]#label path
	path_oh = path_all[phase_num+1]#onehot path

	for image in tqdm(os.listdir(path_org)):#image本身就是name
		img = Image.open(os.path.join(path_org,image))#注意这里的文件路径
		pix_array = np.array(img)
		rows,cols = pix_array.shape
		#print(pix_array.shape)

		array_size = (class_num,rows,cols)
		#img.size和pix_array.shape是行列相反的,如果用img.size要注意
		#print(array_size)
		pix_array_oh = np.zeros(array_size,dtype=np.uint8)
		#print(pix_array_oh)

		for i in range(rows):
			for j in range(cols):
				pix = pix_array[i,j]
				if pix > 0:
					#print('pix is :',pix)
					pix_array_oh[pix,i,j] = 1

		for k in range(class_num):
			img_oh = Image.fromarray(pix_array_oh[k])
			img_oh.save(r''+path_oh+'/'+image.split('.')[0]+'.'+str(k)+'.png')




