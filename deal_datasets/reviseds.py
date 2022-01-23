import os
#批量修改文件名
class BatchRename():
    def __init__(self,path,save_path,label=None):
        if not os.path.exists(save_path):
            # os.path.exists()函数用来检验给出的路径是否真地存在 返回bool
            os.makedirs(save_path)
            # makedir(path):创建文件夹，注：创建已存在的文件夹将异常
        self.path = path  #表示需要命名处理的文件夹
        self.save_path = save_path #保存重命名后的图片地址
        self.label = label
    def rename(self):
        filelist = os.listdir(self.path) #获取文件路径
        total_num = len(filelist) #获取文件长度（个数）
        i = 0  #表示文件的命名是从1开始的
        for item in filelist:
            print(item)
            if item.endswith('.jpg') or item.endswith('.jpeg' or item.endswith('.png') or item.endswith('.gif')):  #初始的图片的格式为jpg格式的（或者源文件是png格式及其他格式，后面的转换格式就可以调整为自己需要的格式即可）
                src = os.path.join(os.path.abspath(self.path), item)#当前文件中图片的地址
                dst = os.path.join(os.path.abspath(self.save_path), self.label+'.'+str(i) + '.jpg')#处理后文件的地址和名称,可以自己按照自己的要求改进
                try:
                    os.rename(src, dst)
                    print ('converting %s to %s ...' % (src, dst))
                    i = i + 1
                except:
                    continue
        print ('total %d to rename & converted %d jpgs' % (total_num, i))

def images_sort(path,path_other):
    # path = "down_datasets/golds_and_monkey2/train/gold/"
    # path_other = "down_datasets/golds_and_monkey/train/gold/"
    filelist = os.listdir(path) #获取文件路径

    if not os.path.exists(path_other):
        os.makedirs(path_other)

    for i,ins in enumerate(filelist):
        oldname = os.path.splitext(path+ins)
        print(oldname[0],oldname[1])
        os.rename(oldname[0]+oldname[1],path_other+str(i)+".jpg")

if __name__ == '__main__':
    path1 = "down_datasets/golds_and_monkey2/train/gold/"
    path2 = "down_datasets/golds_and_monkey2/train/monkey_king/"
    path3 = "down_datasets/golds_and_monkey2/validation/gold/"
    path4 = "down_datasets/golds_and_monkey2/validation/monkey_king/"

    path_other1 = "down_datasets/golds_and_monkey/train/gold/"
    path_other2 = "down_datasets/golds_and_monkey/train/monkey_king/"
    path_other3 = "down_datasets/golds_and_monkey/validation/gold/"
    path_other4 = "down_datasets/golds_and_monkey/validation/monkey_king/"
    images_sort(path1, path_other1)
    images_sort(path2, path_other2)
    images_sort(path3, path_other3)
    images_sort(path4, path_other4)





# if __name__ == '__main__':
#     path = "./monkey_king"#'./golds_sets'
#     save_path = './monkey/train'
#     label = 'monkey_king'
#     demo = BatchRename(path,save_path,label)
#     demo.rename()

