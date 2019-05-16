import shutil
import os
from tqdm import tqdm
import glob
import argparse

parser = argparse.ArgumentParser(description='Training')
parser.add_argument('--data_set', default='/home/milton/PycharmProjects/facelock_app/facenet_mtcnn_to_mobile/custom_faces', type=str,help='Dataset Path, each class must in its own dir')
parser.add_argument('--output',default='/home/milton/PycharmProjects/facelock_app/facenet_mtcnn_to_mobile/face_data_set', type=str,help='Out save dir')
parser.add_argument('--val_amount', default=0.4, type=float, help='How much should be train vs val. if test enabled it will half val+ half test')
parser.add_argument('--test_enable', default=True, type=bool, help='will make test set or not')

def train_val_split(args):
    data_set=args.data_set
    output=args.output
    if not os.path.isdir(output):
        os.makedirs(output)
    test_enable=args.test_enable
    train_dir=os.path.join(output,"train")
    val_dir=os.path.join(output,"val")
    test_dir=os.path.join(output,"test")
    val_amount=args.val_amount
    all_paths = glob.glob(os.path.join(data_set,"**","**"))

    if not os.path.isdir(train_dir):
        os.makedirs(train_dir)
    if not os.path.isdir(val_dir):
        os.makedirs(val_dir)
    if test_enable==True:
        val_amount=val_amount*0.5
        if not os.path.isdir(test_dir):
            os.makedirs(test_dir)
    val_amount=int(val_amount*len(all_paths)*0.5)
    for i in tqdm(range(len(all_paths))):
        path = all_paths[i]
        class_name = path.split('/')[-2]
        class_name=class_name.strip().replace(' ','_')
        if i%val_amount==0:
            class_dir = os.path.join(val_dir, class_name)
            if not os.path.isdir(class_dir):
                os.makedirs(class_dir)
            shutil.copy(path, os.path.join(class_dir,os.path.basename(path)))
        elif i%val_amount==1:
            class_dir = os.path.join(test_dir, class_name)
            if not os.path.isdir(class_dir):
                os.makedirs(class_dir)
            shutil.copy(path, os.path.join(class_dir,os.path.basename(path)))
        else:
            class_dir = os.path.join(train_dir, class_name)
            if not os.path.isdir(class_dir):
                os.makedirs(class_dir)
            shutil.copy(path, os.path.join(class_dir,os.path.basename(path)))

if __name__=="__main__":
    args = parser.parse_args()
    train_val_split(args)