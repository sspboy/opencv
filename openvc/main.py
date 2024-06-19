import numpy as np
import cv2,os
# 2D图片处理库
from matplotlib import pyplot as plt

# 需求描述：：：：
# 读取图片
# 匹配识别图片位置
# 截取图片
# 保留截取图片




img1 = cv2.imread('img/template/detaile_page.jpg')
#将图片转换为灰度图
img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

template1 = cv2.imread('img/template/shop.jpg') # 代入图片模板高度、宽度

# 获取模版图片的高度、宽度（单位PX）===========开始
template = cv2.cvtColor(template1,cv2.COLOR_BGR2GRAY)
th, tw = template.shape[::]
heiht = str(th)
width = str(tw)
print('高度：%s' % heiht)
print('宽度：%s' % width)
# 获取模版图片的高度、宽度（单位PX）===========结束

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

cv2.rectangle(img,topLeft, bottomRight, (255, 255, 0), 1)

# print(topLeft)
# 33, 2041
# print(bottomRight)
# 282, 2115

# [h,w]根据自己图片中目标的位置修改
img1 = img1[2058:2110,36:282]
# [A:B,C:D]
# A:顶部到底部得定位==》上边距(0=顶部，值越大越靠近底部)
# B:

save_path = r'./img'
save_path_file = os.path.join(save_path, 'heheda.jpg')
cv2.imwrite(save_path_file, img1)


