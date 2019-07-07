import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["stoma"]  # 人物检测


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    # if os.path.exists('E:/food-xml/%' % (image_id)):
        list_file_train = open('/media/sun_zach/H/git/project_stomata/data/train_list.txt', 'a+', encoding='utf-8')
        list_file_train.write('/media/sun_zach/H/git/project_stomata/data/images/%s.jpg\n' % (str(image_id)))
        list_file_train.close()


        in_file = open('/media/sun_zach/H/git/project_stomata/data/Annotations/%s.xml' % (image_id), encoding='utf-8')
        out_file = open('/media/sun_zach/H/git/project_stomata/data/Annotations/%s.txt' % (image_id), 'a', encoding='utf-8')  # 生成txt格式文件
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text)
        h = int(size.find('height').text)

        for obj in root.iter('object'):
            cls = obj.find('name').text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('ymax').text))
            bb = convert((w, h), b)
            out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')




#  list_file_val = open('boat_val.txt', 'w')

path1 = "/media/sun_zach/H/git/project_stomata/data/Annotations"
filelist = os.listdir(path1)
for files in filelist:
    filename0 = os.path.splitext(files)[0]  # 读取文件名
    convert_annotation(filename0)
  # 只生成训练集，自己根据自己情况决定

# for image_id in image_ids_val:

#    list_file_val.write('/home/*****/darknet/boat_detect/images/%s.jpg\n'%(image_id))
#    convert_annotation(image_id)
# list_file_val.close()
