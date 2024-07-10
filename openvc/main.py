import numpy as np
import cv2,os,time
import numpy as np

# 2D图片处理库
from matplotlib import pyplot as plt


# 匹配模版图片方法；返回截图
class Selectimg():

    def __init__(self,img_url,template_img_url):
        self.detaile_img = cv2.imread(img_url)                  # 截图图片地址
        self.Template_img = cv2.imread(template_img_url)    # 模版目标图片地址

    def get_W_H(self):  # 模板-图片长、宽

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

    def get_one(self):  # 匹配单张图片===目标图片坐标

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
        print('上边%s' % tt)
        tb = bottomRight[1] # 顶部到模版图片下边的距离
        print('下边%s' % tb)
        ll = topLeft[0] # 左边到模版图片左边的距离
        print('左边%s' % tb)
        lr = bottomRight[0] # 左边到模版图片右边的距离
        print('右边%s' % lr)

        # 按边距剪切图片
        # img1 = self.detaile_img[tt:tb,ll:lr]    # 根据边距剪切匹配的
        # cv2.imshow('image', img1)
        # cv2.waitKey(0)
        # cv2.destroyWindow('image')

        # 把找到的匹配模版画圈圈出来
        cv2.rectangle(self.detaile_img, topLeft, bottomRight, (0, 0, 255), 2)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)     # 设置窗口可缩放
        cv2.imshow('image', self.detaile_img)

        cv2.waitKey(0)  # 按0阻塞

        cv2.destroyWindow('image')


    # 多个匹配模版
    def get_more(self):
        img_rgb = cv2.imread('img/pinjie/weixin_4.jpg')  # sku图片
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)  #
        template = cv2.imread('img/pinjie/read_left.png', 0)  # sku模版图片
        threshold = 0.9
        dets = s.template(img_gray, template, threshold)
        for i in dets:
            print(int(i[0]), int(i[1]), int(i[2]), int(i[3]))
            cv2.rectangle(img_rgb, (int(i[0]), int(i[1])), (int(i[2]), int(i[3])), (0, 0, 255), 2)
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 设置窗口可缩放
        cv2.imshow('image', img_rgb)
        cv2.waitKey(0)  # 按0阻塞
        cv2.destroyWindow('image')

    def py_nms(self, dets, thresh):
        """Pure Python NMS baseline."""
        # x1、y1、x2、y2、以及score赋值
        # （x1、y1）（x2、y2）为box的左上和右下角标
        x1 = dets[:, 0]
        y1 = dets[:, 1]
        x2 = dets[:, 2]
        y2 = dets[:, 3]
        scores = dets[:, 4]

        # 每一个候选框的面积
        areas = (x2 - x1 + 1) * (y2 - y1 + 1)
        # order是按照score降序排序的
        order = scores.argsort()[::-1]
        # print("order:",order)

        keep = []
        while order.size > 0:
            i = order[0]
            keep.append(i)
            # 计算当前概率最大矩形框与其他矩形框的相交框的坐标，会用到numpy的broadcast机制，得到的是向量
            xx1 = np.maximum(x1[i], x1[order[1:]])
            yy1 = np.maximum(y1[i], y1[order[1:]])
            xx2 = np.minimum(x2[i], x2[order[1:]])
            yy2 = np.minimum(y2[i], y2[order[1:]])

            # 计算相交框的面积,注意矩形框不相交时w或h算出来会是负数，用0代替
            w = np.maximum(0.0, xx2 - xx1 + 1)
            h = np.maximum(0.0, yy2 - yy1 + 1)
            inter = w * h
            # 计算重叠度IOU：重叠面积/（面积1+面积2-重叠面积）
            ovr = inter / (areas[i] + areas[order[1:]] - inter)

            # 找到重叠度不高于阈值的矩形框索引
            inds = np.where(ovr <= thresh)[0]
            # print("inds:",inds)
            # 将order序列更新，由于前面得到的矩形框索引要比矩形框在原order序列中的索引小1，所以要把这个1加回来
            order = order[inds + 1]
        return keep

    def template(self, img_gray, template_img, template_threshold):
        '''
        img_gray:待检测的灰度图片格式
        template_img:模板小图，也是灰度化了
        template_threshold:模板匹配的置信度
        '''

        h, w = template_img.shape[:2]
        res = cv2.matchTemplate(img_gray, template_img, cv2.TM_CCOEFF_NORMED)
        start_time = time.time()
        loc = np.where(res >= template_threshold)  # 大于模板阈值的目标坐标
        score = res[res >= template_threshold]  # 大于模板阈值的目标置信度
        # 将模板数据坐标进行处理成左上角、右下角的格式
        xmin = np.array(loc[1])
        ymin = np.array(loc[0])
        xmax = xmin + w
        ymax = ymin + h
        xmin = xmin.reshape(-1, 1)  # 变成n行1列维度
        xmax = xmax.reshape(-1, 1)  # 变成n行1列维度
        ymax = ymax.reshape(-1, 1)  # 变成n行1列维度
        ymin = ymin.reshape(-1, 1)  # 变成n行1列维度
        score = score.reshape(-1, 1)  # 变成n行1列维度
        data_hlist = []
        data_hlist.append(xmin)
        data_hlist.append(ymin)
        data_hlist.append(xmax)
        data_hlist.append(ymax)
        data_hlist.append(score)
        data_hstack = np.hstack(data_hlist)  # 将xmin、ymin、xmax、yamx、scores按照列进行拼接
        thresh = 0.3  # NMS里面的IOU交互比阈值

        keep_dets = self.py_nms(data_hstack, thresh)
        print("nms time:", time.time() - start_time)  # 打印数据处理到nms运行时间
        dets = data_hstack[keep_dets]  # 最终的nms获得的矩形框
        return dets


    # 保存图片到本地
    def save_img(self, img, name):
        save_path = r'./img'                                      # 存储路径配置
        save_path_file = os.path.join(save_path, name)            # 存储图片到本地文件夹
        cv2.imwrite(save_path_file, img)                          # 存储

    # 垂直拼接图片
    def pinjie(self):

        # 第一张底部剪切出模版图
        one_img_url = 'img/template/weixin_1.jpg'
        two_img_url = 'img/template/weixin_2.jpg'

        # 匹配第二张图中坐标位置

        # 第二张图剪切最顶部

        # 第一张图 + 剪切后的第二张图合成

        pass


if __name__ == '__main__':

    img_url = 'img/template/detaile_page.jpg'   # 原图

    template_img_url = 'img/template/shop.jpg'  # 模版

    s = Selectimg(img_url,template_img_url)

    # s.get_one()     # 当个匹配
    # s.get_more()    # 多个匹配

    # 最高位置坐标
    # 最低位置坐标
    # 向上滑多少距离

    # SKU是否全部采集完毕









# airtest==1.3.4
# cached-property==1.5.2
# certifi==2024.6.2
# charset-normalizer==3.3.2
# colorama==0.4.6
# colored==2.2.4
# comtypes==1.4.4
# contourpy==1.2.1
# cycler==0.12.1
# decorator==5.1.1
# Deprecated==1.2.14
# deprecation==2.1.0
# facebook-wda==1.4.7
# ffmpeg-python==0.2.0
# filelock==3.15.1
# fonttools==4.53.0
# future==1.0.0
# hrpc==1.0.9
# idna==3.7
# Jinja2==3.1.4
# kiwisolver==1.4.5
# logzero==1.7.0
# MarkupSafe==2.1.5
# matplotlib==3.9.0
# mss==6.1.0
# numpy==1.26.4
# opencv-contrib-python==4.6.0.66
# opencv-python==4.10.0.82
# packaging==24.1
# pillow==10.3.0
# pip==24.1.2
# pocoui==1.0.94
# psutil==5.9.8
# py==1.11.0
# pyparsing==3.1.2
# pypiwin32==223
# python-dateutil==2.9.0.post0
# pywin32==306
# pywinauto==0.6.3
# requests==2.32.3
# retry==0.9.2
# setuptools==69.5.1
# simple-tornado==0.2.2
# simplejson==3.19.2
# six==1.16.0
# tabulate==0.9.0
# tidevice==0.12.10
# tornado==6.4.1
# urllib3==2.2.2
# websocket-client==0.48.0
# wheel==0.43.0
# wrapt==1.16.0




