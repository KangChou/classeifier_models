# 导入必要的包
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
# pip install selenium
# 打开谷歌浏览器
# wget http://chromedriver.storage.googleapis.com/2.40/chromedriver_linux64.zip
# https://chromedriver.storage.googleapis.com/index.html?path=93.0.4577.63/
from bs4 import *
import requests
import os
# 谷歌图片爬取
#  https://blog.csdn.net/qq_34687559/article/details/106340929
#  https://blog.csdn.net/qq_34687559/article/details/106351487

# CREATE FOLDER
def folder_create(images):
    try:
        folder_name = input("Enter Folder Name:- ")
        # folder creation
        os.mkdir(folder_name)

    # if folder exists with that name, ask another name
    except:
        print("Folder Exist with that name!")
        folder_create()

    # image downloading start
    download_images(images, folder_name)


# DOWNLOAD ALL IMAGES FROM THAT URL
def download_images(images, folder_name):
    # initial count is zero
    count = 0

    # print total images found in URL
    print(f"Total {len(images)} Image Found!")

    # checking if images is not zero
    if len(images) != 0:
        for i, image in enumerate(images):
            # From image tag ,Fetch image Source URL

            # 1.data-srcset
            # 2.data-src
            # 3.data-fallback-src
            # 4.src

            # Here we will use exception handling

            # first we will search for "data-srcset" in img tag
            try:
                # In image tag ,searching for "data-srcset"
                image_link = image["data-srcset"]

            # then we will search for "data-src" in img
            # tag and so on..
            except:
                try:
                    # In image tag ,searching for "data-src"
                    image_link = image["data-src"]
                except:
                    try:
                        # In image tag ,searching for "data-fallback-src"
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            # In image tag ,searching for "src"
                            image_link = image["src"]

                        # if no Source URL found
                        except:
                            pass

            # After getting Image Source URL
            # We will try to get the content of image
            try:
                r = requests.get(image_link).content
                try:

                    # possibility of decode
                    r = str(r, 'utf-8')

                except UnicodeDecodeError:

                    # After checking above condition, Image Download start
                    with open(f"{folder_name}/images{i + 1}.jpg", "wb+") as f:
                        f.write(r)

                    # counting number of image downloaded
                    count += 1
            except:
                pass

        # There might be possible, that all
        # images not download
        # if all images download
        if count == len(images):
            print("All Images Downloaded!")

        # if all images not download
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")


# MAIN FUNCTION START
def main(url):
    # content of URL
    r = requests.get(url)

    # Parse HTML Code
    soup = BeautifulSoup(r.text, 'html.parser')

    # find all images in URL
    images = soup.findAll('img')

    # Call folder create function
    folder_create(images)


# take url
# url = "https://stocksnap.io"
url = input("Enter URL:- ")
# CALL MAIN FUNCTION  golds_sets
main(url)
"""
爬取爬取url:
http://www.99it.com.cn/news/jsz/2022/0119/49661.html
https://m.gmw.cn/baijia/2022-01/20/1302771846.html
https://news.duote.com/m/202201/253041.html
https://www.sohu.com/a/518318797_121106832
https://m.chazhengla.com/gl/2721.html
"""