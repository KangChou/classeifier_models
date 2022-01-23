import os
import zipfile
from model_inception_v3 import *
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
"""
ImageNet 上亿参数，数据量百万，是不是参数多的模型都需要大量数据？当然不是啦，我们可以用别人训练好的模型(基础模型)，在训练好的部分参数基础上进行训练。
"""

# 读取数据
local_zip = "./deal_datasets/down_datasets/golds_and_monkey2.zip"
# './deal_datasets/down_datasets/cats_and_dogs_filtered.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall( '/')
zip_ref.close()

base_dir = '/golds_and_monkey' # '/cats_and_dogs_filtered'

train_dir = os.path.join( base_dir, 'train')
validation_dir = os.path.join( base_dir, 'validation')

class_name1 = 'gold'  #cats
class_name2 = 'monkey_king'  #dogs
train_cats_dir = os.path.join(train_dir, class_name1)
print(train_cats_dir)
train_dogs_dir = os.path.join(train_dir, class_name2)
validation_cats_dir = os.path.join(validation_dir, class_name1)
validation_dogs_dir = os.path.join(validation_dir, class_name2)

train_cat_fnames = os.listdir(train_cats_dir)
train_dog_fnames = os.listdir(train_dogs_dir)


#
# # 自动为数据打上标签并进行归一化处理和数据增强。
# train_datagen = ImageDataGenerator(rescale = 1./255.,  #归一化处理
#                                    rotation_range = 40,  # 旋转角度
#                                    width_shift_range = 0.2,  # 宽度变化范围
#                                    height_shift_range = 0.2,  # 高度变化范围
#                                    shear_range = 0.2,  # 剪切范围（类似于倾斜并拉伸）
#                                    zoom_range = 0.2,  # 缩放设置
#                                    horizontal_flip = True)  # 水平翻转
#
# # 对我们的测试集打上标签并进行归一化处理
# test_datagen = ImageDataGenerator( rescale = 1.0/255. )
#
# # 利用我们的ImageDataGenerator来读取数据
# train_generator = train_datagen.flow_from_directory(train_dir,
#                                                     batch_size = 20,  # 一批读多少个数据
#                                                     class_mode = 'binary',   # 分类方式
#                                                     target_size = (150, 150))  # 目标大小
#
# #
# validation_generator =  test_datagen.flow_from_directory( validation_dir,
#                                                           batch_size  = 20,
#                                                           class_mode  = 'binary',
#                                                           target_size = (150, 150))
#
# # 进行训练
# history = model.fit_generator(
#             train_generator,
#             validation_data = validation_generator,
#             steps_per_epoch = 100,  # 一次训练几批完成
#             epochs = 100,  # 所有数据训练几次
#             validation_steps = 50,
#             verbose = 2)
#
#
# acc = history.history['acc']
# val_acc = history.history['val_acc']
# loss = history.history['loss']
# val_loss = history.history['val_loss']
#
# epochs = range(len(acc))
#
# plt.plot(epochs, acc, 'r', label='Training accuracy')
# plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
# plt.title('Training and validation accuracy')
# plt.legend(loc=0)
# plt.figure()
# plt.savefig("./accuracy_v4.png")
#
# plt.plot(epochs, loss, 'bo', label='Training Loss')
# plt.plot(epochs, val_loss, 'b', label='Validation Loss')
# plt.title('Training and validation loss')
# plt.legend()
# plt.savefig("./loss_v4.png")
#
# plt.show()
#
#
#
# model.save('./model_output/' + 'model3_inception_v3.h5')
# import signal
# os.kill(os.getpid(), signal.SIGKILL)