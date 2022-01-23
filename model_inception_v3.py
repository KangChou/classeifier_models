import os
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import layers
from tensorflow.keras import Model


from tensorflow.keras.applications.inception_v3 import InceptionV3

# 读取权重信息
local_weights_file ='./deal_datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
# 对我们的预训练模型进行修改，输入改成我们要输入的数据的形状，不包括最上面一层因为我们要进行重新训练。
pre_trained_model = InceptionV3(input_shape=(150, 150, 3),
                                include_top=False,
                                weights=None)
# 加载我们需要的权重。
pre_trained_model.load_weights(local_weights_file)

# 因为我们的数据量比较小所以我们不训练之前的网络。
for layer in pre_trained_model.layers:
    layer.trainable = False
# 打印inception网络的结果
pre_trained_model.summary()

# 从中选取一层打印相关信息。
last_layer = pre_trained_model.get_layer('mixed7')
print('last layer output shape: ', last_layer.output_shape)
last_output = last_layer.output
print(last_output)

#为模型添加新的层
# 对我们的输出进行平铺操作
x = layers.Flatten()(last_output)
# 增加一个全连接层，并使用relu作为激活函数
x = layers.Dense(1024, activation='relu')(x)
# 添加随机失活，抑制过拟合
x = layers.Dropout(0.2)(x)
# 把输出设置成sigmoid函数
x = layers.Dense  (1, activation='sigmoid')(x)
# 初始化我们自己的模型
model = Model( pre_trained_model.input, x)

model.compile(optimizer = RMSprop(learning_rate=0.0001),
              loss = 'binary_crossentropy',
              metrics = ['acc'])
