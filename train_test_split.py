# importing required packages
from pathlib import Path
import shutil
import os
import re
 
# defining source and destination
# paths
src = './orig_datasets/CHV_dataset/images/'
src_a = './orig_datasets/CHV_dataset/annotations/'
trg = './yolov7/data/PPEData/{folder}/images/'
trg_a = './yolov7/data/PPEData/{folder}/labels/'
 
# files=os.listdir(src)
 
# iterating over all the files in
# the source directory

f_train = open('./orig_datasets/CHV_dataset/data_split/train.txt')
train_imgs = f_train.read().splitlines()
f_train.close()

f_val = open('./orig_datasets/CHV_dataset/data_split/valid.txt')
val_imgs = f_val.read().splitlines()
f_val.close()

f_test = open('./orig_datasets/CHV_dataset/data_split/test.txt')
test_imgs = f_test.read().splitlines()
f_test.close()

# print(train_imgs)

for fname in train_imgs:
    print(fname)
    annotation_name = re.search(r"(ppe\_\d+)", fname).group(0)
    print('------')
    print(annotation_name)
    shutil.copy2(fname, trg.format(folder='train'))
    shutil.copy2(os.path.join(src_a,annotation_name+'.txt'), trg_a.format(folder='train'))

for fname in val_imgs:
    print(fname)
    annotation_name = re.search(r"(ppe\_\d+)", fname).group(0)
    print('------')
    print(annotation_name)
    shutil.copy2(fname, trg.format(folder='valid'))
    shutil.copy2(os.path.join(src_a,annotation_name+'.txt'), trg_a.format(folder='valid'))

for fname in test_imgs:
    print(fname)
    annotation_name = re.search(r"(ppe\_\d+)", fname).group(0)
    print('------')
    print(annotation_name)
    shutil.copy2(fname, trg.format(folder='test'))
    shutil.copy2(os.path.join(src_a,annotation_name+'.txt'), trg_a.format(folder='test'))
