import tensorflow as tf

# inception_pretrain_model_url = 'https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop'
# # inception_pretrain_model_url = 'http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz'
# # ck:https://blog.csdn.net/u014264373/article/details/79763812
# # 创建文件夹的名字及路径（当前路径下）
# # 创建存放模型的文件夹
# inception_pretrain_model_dir = "./deal_datasets/"
# # 如果inception_pretrain_model_dir的文件夹不存在，则创建
# if not os.path.exists(inception_pretrain_model_dir):
#     # os.path.exists()函数用来检验给出的路径是否真地存在 返回bool
#     os.makedirs(inception_pretrain_model_dir)
#     # makedir(path):创建文件夹，注：创建已存在的文件夹将异常
#
# filename = inception_pretrain_model_url.split('/')[-1]
# # inception_pretrain_model_url的字符串是http://download.tensorflow.org/models/image/imagenet/inception-2015-12-05.tgz
# # filename取以/分开的最后一个字符串即inception-2015-12-05.tgz
# filepath = os.path.join(inception_pretrain_model_dir, filename)
# # 将两个路径连接起来：inception_pretrain\inception-2015-12-05.tgz
#
# # 查看路径下是否有文件，若无就下载
# # 如果路径名不存在（这里指的是路径下的内容）的话，就开始下载文件
# if not os.path.exists(filepath):
#     print("开始下载: ", filename)
#     r = requests.get(inception_pretrain_model_url, stream=True)
#     # requests.get从指定http网站上下载内容
#     with open(filepath, 'wb') as f:
#         for chunk in r.iter_content(chunk_size=1024):
#             if chunk:
#                 f.write(chunk)
#     #用with语句来打开文件，就包含关闭的功能。wb是写二进制文件，由于文件过大，批量写（这里是压缩包）
# # 解压文件，解压前先打印开始解压提示语
# print("下载完成, 开始解压: ", filename)
# #解压出来的文件其中的classify_image_graph_def.pb 文件就是训练好的Inception-v3模型。
# #imagenet_synset_to_human_label_map.txt是类别文件。
# tarfile.open(filepath, 'r:gz').extractall(inception_pretrain_model_dir)
# # tarfile解压文件
#
# #创建TensorBoard log目录
# log_dir = 'inception_log'  # 目录地址
# if not os.path.exists(log_dir):
#     os.makedirs(log_dir)
#
# # 加载inception graph
# inception_graph_def_file = os.path.join(inception_pretrain_model_dir, 'classify_image_graph_def.pb')
# with tf.compat.v1.Session() as sess:
#     with tf.compat.v1.io.gfile.FastGFile(inception_graph_def_file, 'rb') as f:  # 以二进制读取文件
#         graph_def = tf.compat.v1.GraphDef()
#         # 绘图
#         graph_def.ParseFromString(f.read())
#         tf.import_graph_def(graph_def, name='')
#     writer = tf.compat.v1.summary.FileWriter(log_dir, sess.graph)
#     # AttributeError: module 'tensorflow.python.training.training' has no attribute 'SummaryWriter'所以用tf.summary.FileWriter
#     writer.close()