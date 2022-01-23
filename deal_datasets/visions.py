# utf-8
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from rets import rundatases
# 设置我们要画的图的参数
nrows = 4
ncols = 4
# 我们要选择进行可视化的数据集的起始位置
pic_index = 8

# 设置图片为4行4列，图片大小为16x16
rows = 4
cols = 4

fig, ax = plt.subplots(nrows=rows, ncols=cols, figsize=(4 * nrows, 4 * ncols))

pic_index+=8


train_cats_dir,train_dogs_dir,train_cat_fnames,train_dog_fnames,_,_ = rundatases()
next_cat_pix = [os.path.join(train_cats_dir, fname)
                for fname in train_cat_fnames[ pic_index-8:pic_index]
               ]

next_dog_pix = [os.path.join(train_dogs_dir, fname)
                for fname in train_dog_fnames[ pic_index-8:pic_index]
               ]

for i, img_path in enumerate(next_cat_pix+next_dog_pix):
  # 这里注意图片是4x4的。画图时不能用ax[1].imshow
  img = mpimg.imread(img_path)
  ax[int(i/4),i%4].imshow(img)
  ax[int(i/4),i%4].axis('Off')

plt.show()

