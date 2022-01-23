import os
import numpy as np
from keras.preprocessing import image
from models import *
filePath = './test_data/'
keys = os.listdir(filePath)
# 获取所有文件名
# for i,j,k in os.walk(filePath):
#     keys = k
for fn in keys:
    # 对图片进行预测
    # 读取图片
    path = './test_data/' + fn
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    # 在第0维添加维度变为1x150x150x3，和我们模型的输入数据一样
    x = np.expand_dims(x, axis=0)
    # np.vstack:按垂直方向（行顺序）堆叠数组构成一个新的数组，我们一次只有一个数据所以不这样也可以
    images = np.vstack([x])
    # batch_size批量大小，程序会分批次地预测测试数据，这样比每次预测一个样本会快。因为我们也只有一个测试所以不用也可以
    classes = model.predict(images, batch_size=10)
    print(classes[0])

    if classes[0] > 0:
        print(fn + " is a dog")

    else:
        print(fn + " is a cat")


