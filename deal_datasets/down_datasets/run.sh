sudo apt install wget
wget --no-check-certificate \
  https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip \
  -O ./cats_and_dogs_filtered.zip

unzip cats_and_dogs_filtered.zip

# 迁移学习:预训练模型
wget https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
# install python pkg
pip install matplotlib tensorflow_datasets tensorflow-gpu==2.5 -i https://mirrors.aliyun.com/pypi/simple/

# wget --no-check-certificate \
#     https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 \
#     -O ./inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5

# 目标检测标注工具:https://zhuanlan.zhihu.com/p/51199150