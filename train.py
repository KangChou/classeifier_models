from tensorflow.keras.preprocessing.image import ImageDataGenerator
from deal_datasets.rets import rundatases
import matplotlib.pyplot as plt
from models import *
# 把每个数据都放缩到0到1范围内
train_datagen = ImageDataGenerator( rescale = 1.0/255. )
test_datagen  = ImageDataGenerator( rescale = 1.0/255. )
"""
ck:https://keras.io/zh/preprocessing/image/
"""
print("train_datagen=:{},test_datagen=:{}".format(train_datagen,test_datagen))
_,_,_,_,train_dir,validation_dir = rundatases()
# 生成训练集的带标签的数据
train_generator = train_datagen.flow_from_directory(train_dir,  # 训练图片的位置
                                                    batch_size=20, # 每一个投入多少张图片训练
                                                    class_mode='binary', # 设置我们需要的标签类型
                                                    target_size=(150, 150))  # 将图片统一大小
# 生成验证集带标签的数据
validation_generator =  test_datagen.flow_from_directory(validation_dir,  # 验证图片的位置
                                                         batch_size=20, # 每一个投入多少张图片训练
                                                         class_mode  = 'binary', # 设置我们需要的标签类型
                                                         target_size = (150, 150))  # 将图片统一大小


# print("train_generator=:{},validation_generator=:{}".format(train_generator,validation_generator))
#
# save_func = tf.keras.callbacks.ModelCheckpoint(filepath='./checkpoint',save_weights = True)
#
# model.fit()

# 训练
"""
model.fit()适用于数据集比较小，一次性读入所有数据内存不会溢出；
model.fit_generator()适用于数据集大，内存容易溢出；
如果有数据增广，也采用fit_generator()。
"""
history = model.fit_generator(train_generator,
                              validation_data=validation_generator,
                              steps_per_epoch=100,
                              epochs=15,
                              validation_steps=50,
                              verbose=2)

# 得到精度和损失值
acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))  # 得到迭代次数

# 绘制精度曲线
plt.plot(epochs, acc)
plt.plot(epochs, val_acc)
plt.title('Training and validation accuracy')
plt.legend(('Training accuracy', 'validation accuracy'))
plt.savefig("./accuracy.png")
plt.figure()

# 绘制损失曲线
plt.plot(epochs, loss)
plt.plot(epochs, val_loss)
plt.legend(('Training loss', 'validation loss'))
plt.title('Training and validation loss')
plt.savefig("./loss.png")
plt.show()
#结束程序释放资源,signal模块可以在linux下正常使用
import os, signal
os.kill(os.getpid(), signal.SIGKILL)
