import csv
from vision_utils.fileutils import *
import matplotlib.pyplot as plt
import cv2

def get_csv_data(path):
    rows= read_csv_file (path)
    return rows


def get_csv_data_images_labels(path):
    rows= read_csv_file (path)
    x=[]
    y=[]
    for row in rows:
        x.append(row[0])
        y.append(row[1:5])
    return (x,y)

def scale_image_label(img, label, image_size=1280):
    h,w,_=img.shape
    h_scale=image_size/h
    w_scale=image_size/w
    x1,y1,x2,y2=label
    x1_new=int(x1*w_scale)
    x2_new=int(x2*w_scale)
    y1_new=int(y1*h_scale)
    y2_new =int(y2*h_scale)
    print("{},{},{},{}".format(x1_new, y1_new, x2_new, y2_new))
    img=cv2.resize(img, (image_size, image_size))
    return (img, (x1_new,y1_new,x2_new,y2_new))


if __name__=="__main__":
    data=get_csv_data('wider_face_train.csv')
    path=data[10][0]
    print(path)
    x1,y1,x2,y2=data[10][1:5]
    x1=int(x1)
    y1=int(y1)
    x2=int(x2)
    y2=int(y2)
    img=cv2.imread(path)
    img,(x1,y1,x2,y2)=scale_image_label(img,[x1,y1,x2,y2])
    img=cv2.rectangle(img, (x1,y1),(x2,y2),(255,255,255),2)
    plt.imshow(img)
    plt.show()