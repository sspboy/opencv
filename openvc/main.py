import numpy as np
import cv2,os
# 2D图片处理库
from matplotlib import pyplot as plt

# 需求描述：：：：读取图片===匹配识别图片位置==截取图片====保留截取图片===在原图上框出模版图片
img1 = cv2.imread('img/template/detaile_page.jpg')
#将图片转换为灰度图
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('img/template/shop.jpg') # 代入图片模板高度、宽度

# 获取模版图片的高度、宽度（单位PX）===========开始
template = cv2.cvtColor(template1,cv2.COLOR_BGR2GRAY)
th, tw = template.shape[::]
heiht = str(th) # 74
width = str(tw) # 249
print('高度：%s' % heiht)
print('宽度：%s' % width)
# 获取模版图片的高度、宽度（单位PX）===========结束

# 匹配图片模版位置=====开始
rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
# min_val：数组或图像中的最小值。
# max_val：数组或图像中的最大值。
# min_loc：最小值的位置（坐标）。
# max_loc：最大值的位置（坐标）。
print(minVal)
print(maxVal)
print(minLoc)
print(maxLoc)

topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)

# 匹配图片模版位置=====结束

# 获取框线坐标

# 获取裁剪图片坐标



cv2.rectangle(img1, topLeft, bottomRight, (255, 0, 0), 4)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(topLeft)
# 33, 2041
# print(bottomRight)
# 282, 2115

# [h,w]根据自己图片中目标的位置修改
img1 = img1[2041:2115,33:282]
# img1 = img1[2028:2110,36:282]
# [A:B,C:D]
# A:【模版顶部】到图片顶部的距离
# B:【模版底部】到图片顶部的距离
# C:【模版左边】到图片左边的距离
# D:【模版底部】到图片顶部的距离

# save_path = r'./img'
# save_path_file = os.path.join(save_path, 'heheda.jpg')
# cv2.imwrite(save_path_file, img1)


# 预览截取的图片
# hehda = cv2.imread('img/heheda.jpg')
# cv2.imshow('image', hehda)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


