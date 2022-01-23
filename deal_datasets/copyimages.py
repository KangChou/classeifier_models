import os
import cv2
import os
import shutil

def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)
    return Filelist


def run(org_img_folder):
    # 检索文件
    imglist = getFileList(org_img_folder, [], 'jpg')
    print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')
    for imgpath in imglist:
        imgname = os.path.splitext(os.path.basename(imgpath))[0]
        img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
        # 对每幅图像执行相关操作

def mkdir(outimages):
    if not os.path.exists(outimages):
        os.makedirs(outimages)

def movimages(org_img_folder):
    filelist = os.listdir(org_img_folder)
    # print(filelist)
    # print(len(filelist))
    fl = len(filelist)  #4:1===0.8:0.2
    trainlen = int(fl*0.8)
    trainlist = filelist[0:trainlen]
    # for i in trainlist:
    #     # print(i,trainlen)
    vallist = list(set(filelist) - set(trainlist))
    # for i in vallist:
    #     print(i, len(vallist))
    return trainlist,vallist

def train_val(org_img_folder,lists,label,outpath):
    filelist = os.listdir(org_img_folder)


    for i in ['gold','monkey_king']:
        mkdir(outpath+'train/'+i)
        mkdir(outpath + 'validation/' + i)

    for i in lists:
        print(i)
        # shutil.move(org_img_folder+'/'+i,outimages+i)
        if filelist[0][0:4] == 'gold':
            print(filelist)
            shutil.copy(org_img_folder + i, outpath + label + '/gold/' + i)
        else:
            print(filelist)
            shutil.copy(org_img_folder + i, outpath +label +'/monkey_king/'+ i)

def main(outpath,org_img_folder):
    TR,VA = movimages(org_img_folder)
    for i in [outpath+'train',outpath+'validation',outpath]:
        mkdir(i)
    train_val(org_img_folder,TR,"train",outpath)
    train_val(org_img_folder,VA, "validation",outpath)


if __name__ == '__main__':
    outpath = './golds_and_monkey2/'
    fs1 = './monkey/train/'
    fs2 = './golds/train/'
    filelist1 = os.listdir(fs1)
    filelist2 = os.listdir(fs2)


    input_images_path_list = [fs1,fs2]
    for i in input_images_path_list:
        main(outpath,i)