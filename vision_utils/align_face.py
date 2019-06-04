from mtcnn.mtcnn import MTCNN
import cv2
import argparse
from utils_all.fileutils import *
import glob

parser = argparse.ArgumentParser(description='Detect and align face')
parser.add_argument('--data_set', default='/home/milton/PycharmProjects/facelock_app/facenet_mtcnn_to_mobile/custom_faces', type=str,help='Dataset Path, each class must in its own dir')
parser.add_argument('--output',default='/home/milton/PycharmProjects/facelock_app/facenet_mtcnn_to_mobile/custom_face_aligned', type=str,help='Out save dir')

if __name__=="__main__":
    args = parser.parse_args()
    data_set=args.data_set
    output=args.output
    create_dir_if_not_exists(output)
    file_paths=glob.glob(join(data_set,"**","**"))
    detector = MTCNN()
    for file_path in file_paths:
        img=cv2.imread(file_path)
        if img is None:
            print("Invalid Image: {}".format(file_path))
            continue
        output_data=detector.detect_faces(img)
        if len(output_data) == 0:
            continue

        print(output_data)
        box_ = output_data[0]['box']
        print(box_)
        x,y,w,h= box_
        img=img[x:x+w,y:y+h,:]
        class_name = file_path.split('/')[-2].replace(' ','_')
        class_dir=join(output,class_name)
        create_dir_if_not_exists(class_dir)
        output_path=join(class_dir,basename(file_path))
        cv2.imwrite(output_path,img)