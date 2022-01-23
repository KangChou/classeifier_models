import os


def rundatases():
    # base_dir = './deal_datasets/down_datasets/cats_and_dogs_filtered'
    base_dir = './deal_datasets/down_datasets/golds_and_monkey'
    # 指定每一种数据的位置
    train_dir = os.path.join(base_dir, 'train')
    validation_dir = os.path.join(base_dir, 'validation')
    # 'gold', 'monkey_king'
    # Directory with our training cat/dog pictures
    train_cats_dir = os.path.join(train_dir, 'gold')
    train_dogs_dir = os.path.join(train_dir, 'monkey_king')

    # Directory with our validation cat/dog pictures
    validation_cats_dir = os.path.join(validation_dir, 'gold')
    validation_dogs_dir = os.path.join(validation_dir, 'monkey_king')

    # 打印数据名
    # os.listdir返回所给路径下的所有文件名的列表
    train_cat_fnames = os.listdir( train_cats_dir )
    train_dog_fnames = os.listdir( train_dogs_dir )

    print(train_cat_fnames[:10])
    print(train_dog_fnames[:10])
    # 获取每种数据的数量
    print('total training cat images :', len(os.listdir(      train_cats_dir ) ))
    print('total training dog images :', len(os.listdir(      train_dogs_dir ) ))

    print('total validation cat images :', len(os.listdir( validation_cats_dir ) ))
    print('total validation dog images :', len(os.listdir( validation_dogs_dir ) ))

    return train_cats_dir,train_dogs_dir,train_cat_fnames,train_dog_fnames,train_dir,validation_dir

# if __name__ == '__main__':
#     base_dir = './down_datasets/cats_and_dogs_filtered'
#     rundatases(base_dir)