import numpy as np
import cv2,os
import numpy as np
# 2D图片处理库
from matplotlib import pyplot as plt

# 匹配模版图片方法；返回截图
class Selectimg():

    def __init__(self,img_url,template_img_url):
        self.detaile_img = cv2.imread(img_url)                  # 截图图片地址
        self.Template_img = cv2.imread(template_img_url)    # 模版目标图片地址

    def get_W_H(self):  # 图片长、宽

        # 获取模版图片的高度、宽度（单位PX）===========开始
        template = cv2.cvtColor(self.Template_img,cv2.COLOR_BGR2GRAY)

        obj = {}

        th, tw = template.shape[::]

        # heiht = str(th) # 高度
        # width = str(tw) # 宽度
        # print('高度：%s' % heiht)
        # print('宽度：%s' % width)

        obj['heiht'] = th # 74
        obj['width'] = tw # 249
        # 获取模版图片的高度、宽度（单位PX）===========结束
        return obj

    def get_X_Y(self):  # 目标图片坐标

        img = cv2.cvtColor(self.detaile_img,cv2.COLOR_BGR2GRAY)         # 将图片转换为灰度图

        template = cv2.cvtColor(self.Template_img,cv2.COLOR_BGR2GRAY)   # 将图片转换为灰度图

        # 匹配图片模版位置=====开始
        rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)  # 匹配位置
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
        # min_val：数组或图像中的最小值。
        # max_val：数组或图像中的最大值。
        # min_loc：最小值的位置（坐标）。
        # max_loc：最大值的位置（坐标）。
        # print(minVal)
        # print(maxVal)
        # print(minLoc)
        # print(maxLoc)
        obj = self.get_W_H()
        tw = obj.get('width')
        th = obj.get('heiht')

        topLeft = minLoc
        bottomRight = (topLeft[0] + tw, topLeft[1] + th)

        tt = topLeft[1] # 顶部到模版图片上边的距离

        tb = bottomRight[1] # 顶部到模版图片下边的距离

        ll = topLeft[0] # 左边到模版图片左边的距离

        lr = bottomRight[0] # 左边到模版图片右边的距离

        img1 = self.detaile_img[tt:tb,ll:lr]    # 根据边距剪切匹配的

        cv2.imshow('image', img1)
        cv2.waitKey(0)
        cv2.destroyWindow('image')

    # 保存图片到本地
    def save_img(self, img, name):
        save_path = r'./img'                                      # 存储路径配置
        save_path_file = os.path.join(save_path, name)    # 存储图片到本地文件夹
        cv2.imwrite(save_path_file, img)                          # 存储

    # 垂直拼接图片
    def pinjie(self):
        # 第一张底部剪切出模版图
        # 匹配第二张图中坐标位置
        # 第二张图剪切最顶部
        # 第一张图 + 剪切后的第二张图合成
        pass


if __name__ == '__main__':

    img_url = 'img/template/detaile_page.jpg'   # 原图

    template_img_url = 'img/template/shop.jpg'  # 模版

    s = Selectimg(img_url,template_img_url)

    print(s.get_X_Y())


