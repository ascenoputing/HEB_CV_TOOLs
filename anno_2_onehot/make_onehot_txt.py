#author: HuangEnbo
import os
from tqdm import tqdm

magic_num = 1

path1 = './datasets/Lip/train_onehot'
path2 = './datasets/Lip/val_onehot'
path_all = [path1,path2]

path = path_all[magic_num-1]

fn1 = 'train_onehot'
fn2 = 'val_onehot'
fn_all = [fn1,fn2]

fn = fn_all[magic_num-1]

f = open(r''+fn+'.txt','w')

for image_name in tqdm(os.listdir(path)):
	f.write(image_name+'\n')

f.close()
	
