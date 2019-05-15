import shutil
import os
from tqdm import tqdm
import glob

def train_val_split(all_path,train_dir='train', val_dir='val'):
    if not os.path.isdir(train_dir):
        os.makedirs(train_dir)
    if not os.path.isdir(val_dir):
        os.makedirs(val_dir)

    for i in tqdm(range(len(all_path))):
        path = all_path[i]
        if i%3==0:
            shutil.copy(path, os.path.join(val_dir,os.path.basename(path)))
        else:
            shutil.copy(path, os.path.join(train_dir,os.path.basename(path)))



if __name__=="__main__":
    all_dir='/home/research/competitions/aic_2019/aic19-track2-reid/detected/'
    all_img_dir=os.path.join(all_dir,"image_train")
    train_dir=os.path.join(all_dir,"train")
    val_dir=os.path.join(all_dir,"val")
    all_paths = glob.glob(os.path.join(all_img_dir,'**'))
    train_val_split(all_paths, train_dir, val_dir)