import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras
from matplotlib import pyplot as plt


def preprocess(img, label):
    return tf.image.resize(img, [HEIGHT, WIDTH]) / 255, tf.cast(label, tf.float32)


HEIGHT = 200
WIDTH = 200
classNames = ['cat', 'dog']
split = ['train[:70%]', 'train[70%:]']

trainDataset, testDataset = tfds.load(name='cats_vs_dogs', split=split, as_supervised=True)

testDataset = testDataset.map(preprocess).batch(1)

model = keras.models.load_model('./model_output/model2.h5')

predictions = model.predict(testDataset.take(8))

i = 0
fig, ax = plt.subplots(1, 8)
for image, _ in testDataset.take(8):
    predictedLabel = int(predictions[i] >= 0.5)

    ax[i].axis('off')
    ax[i].set_title(classNames[predictedLabel])
    ax[i].imshow(image[0])
    i += 1

plt.show()