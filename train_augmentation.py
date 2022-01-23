
import os
import zipfile
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator

base = './deal_datasets/down_datasets/'
filename = 'golds_and_monkey'  #'cats_and_dogs_filtered'
class_name1 = 'gold'  #cats
class_name2 = 'monkey_king'  #dogs


local_zip = base+filename+'.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall(base + '/')
zip_ref.close()

base_dir = base + '/'+filename
train_dir = os.path.join(base_dir, 'train')
validation_dir = os.path.join(base_dir, 'validation')

train_cats_dir = os.path.join(train_dir, class_name1)

train_dogs_dir = os.path.join(train_dir, class_name2)

validation_cats_dir = os.path.join(validation_dir, class_name1)

validation_dogs_dir = os.path.join(validation_dir, class_name2)
"""
dropout 超参数的默认解释是在层中训练给定节点的概率，其中 1.0 表示没有 dropout，0.0 表示该层没有输出。
隐藏层中 dropout 的一个好的值在 0.5 到 0.8 之间。输入层使用较大的 dropout 率，例如 0.8

dropout自己虽然也很牛，但是dropout、max-normalization、large decaying learning rates and high momentum组合起来效果更好，
比如max-norm regularization就可以防止大的learning rate导致的参数blow up。
ck:https://blog.csdn.net/ningyanggege/article/details/83115811 
"""


model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(learning_rate=1e-4),
              metrics=['acc'])

# 进行归一化处理
train_datagen = ImageDataGenerator(rescale=1. / 255)
test_datagen = ImageDataGenerator(rescale=1. / 255)

# 利用ImageDataGenerator自动打上标签
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

history = model.fit_generator(
    train_generator,
    steps_per_epoch=100,
    epochs=100,
    validation_data=validation_generator,
    validation_steps=50,
    verbose=2)


acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.savefig("./accuracy2_gold.png")
plt.figure()

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()
plt.savefig("./loss2_gold.png")

plt.show()

model.save('./model_output/' + 'model_gold.h5')
