import tensorflow as tf
from tensorflow.keras.optimizers import RMSprop
model = tf.keras.models.Sequential([
    # 我们的数据是150x150而且是三通道的，所以我们的输入应该设置为这样的格式。
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    # Flatten the results to feed into a DNN
    tf.keras.layers.Flatten(),
    # 512 neuron hidden layer
    tf.keras.layers.Dense(512, activation='relu'),
    # 二分类只需要一个输出
    tf.keras.layers.Dense(1, activation='sigmoid')
])
model.summary()

# 优化方法选择\超参数设置
# 因为只有两个分类。所以用2分类的交叉熵，使用RMSprop，学习率为0.001.优化指标为accuracy
model.compile(optimizer=RMSprop(learning_rate=0.0001),
              loss='binary_crossentropy',
              metrics = ['acc'])
