#coding=utf-8
import os
# 用来生成val2017.txt train2017.txt
image_path = '/home/jia/anktechDrive/09_dataset/basketball/images/train'  # 修改为自己的路径
file = open('/home/jia/anktechDrive/09_dataset/basketball/train.txt', 'w')  # 修改为自己的路径
count = 0
for filename in os.listdir(image_path):
    if (filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png') or filename.endswith('.bmp')):
        print(filename)
        file.write(image_path + filename)
        file.write('\n')
        count += 1
print(count)

