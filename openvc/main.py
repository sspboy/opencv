import numpy as np
import cv2,os
# 2D图片处理库
from matplotlib import pyplot as plt

# 需求描述：：：：读取图片===匹配识别图片位置==截取图片====保留截取图片===在原图上框出模版图片
# img1 = cv2.imread('img/template/detaile_page.jpg')
#将图片转换为灰度图
# img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

# template1 = cv2.imread('img/template/shop.jpg') # 代入图片模板高度、宽度

# 获取模版图片的高度、宽度（单位PX）===========开始
# template = cv2.cvtColor(template1,cv2.COLOR_BGR2GRAY)
# th, tw = template.shape[::]
# heiht = str(th) # 74
# width = str(tw) # 249
# print('高度：%s' % heiht)
# print('宽度：%s' % width)
# 获取模版图片的高度、宽度（单位PX）===========结束

# 匹配图片模版位置=====开始
# rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
# minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
# min_val：数组或图像中的最小值。
# max_val：数组或图像中的最大值。
# min_loc：最小值的位置（坐标）。
# max_loc：最大值的位置（坐标）。
# print(minVal)
# print(maxVal)
# print(minLoc)
# print(maxLoc)
#
# topLeft = minLoc
# bottomRight = (topLeft[0] + tw, topLeft[1] + th)

# 匹配图片模版位置=====结束

# 获取框线坐标

# 获取裁剪图片坐标


#
# cv2.rectangle(img1, topLeft, bottomRight, (255, 0, 0), 4)
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('image', img1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print(topLeft)
# 33, 2041
# print(bottomRight)
# 282, 2115

# [h,w]根据自己图片中目标的位置修改
# img1 = img1[2041:2115,33:282]
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


model_a = {'children': [{'children': [{'children': [{'children': [{'children': [{'children': [{'children': [{
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 2},
                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.6583333333333333,
                                                                                                                                        0.02435897435897436],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.6583333333333333,
                                                                                                                                        0.02435897435897436],
                                                                                                                                    'pos': [
                                                                                                                                        0.49907407407407406,
                                                                                                                                        0.15683760683760684],
                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'text': '#全场包邮#七天退换#48小时发货',
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}}],
                                                                                                                        'name': 'android.view.ViewGroup',
                                                                                                                        'payload': {
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 2},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                1,
                                                                                                                                0.052564102564102565],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                1,
                                                                                                                                0.052564102564102565],
                                                                                                                            'pos': [
                                                                                                                                0.5,
                                                                                                                                0.15683760683760684],
                                                                                                                            'name': 'android.view.ViewGroup',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}}],
                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                'payload': {
                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'visible': True,
                                                                                                                    'zOrders': {
                                                                                                                        'global': 0,
                                                                                                                        'local': 1},
                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                    'anchorPoint': [
                                                                                                                        0.5,
                                                                                                                        0.5],
                                                                                                                    'dismissable': False,
                                                                                                                    'checkable': False,
                                                                                                                    'scale': [
                                                                                                                        1,
                                                                                                                        1],
                                                                                                                    'boundsInParent': [
                                                                                                                        1,
                                                                                                                        0.052564102564102565],
                                                                                                                    'focusable': True,
                                                                                                                    'type': 'android.widget.ViewSwitcher',
                                                                                                                    'touchable': True,
                                                                                                                    'enabled': True,
                                                                                                                    'longClickable': False,
                                                                                                                    'size': [
                                                                                                                        1,
                                                                                                                        0.052564102564102565],
                                                                                                                    'pos': [
                                                                                                                        0.5,
                                                                                                                        0.15683760683760684],
                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'focused': False,
                                                                                                                    'checked': False,
                                                                                                                    'editalbe': False,
                                                                                                                    'selected': False,
                                                                                                                    'scrollable': False}},
                                                                                                            {
                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                'payload': {
                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'visible': True,
                                                                                                                    'zOrders': {
                                                                                                                        'global': 0,
                                                                                                                        'local': 2},
                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                    'anchorPoint': [
                                                                                                                        0.5,
                                                                                                                        0.5],
                                                                                                                    'dismissable': False,
                                                                                                                    'checkable': False,
                                                                                                                    'scale': [
                                                                                                                        1,
                                                                                                                        1],
                                                                                                                    'boundsInParent': [
                                                                                                                        0.05555555555555555,
                                                                                                                        0.02564102564102564],
                                                                                                                    'focusable': True,
                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                    'touchable': True,
                                                                                                                    'enabled': True,
                                                                                                                    'longClickable': False,
                                                                                                                    'size': [
                                                                                                                        0.05555555555555555,
                                                                                                                        0.02564102564102564],
                                                                                                                    'pos': [
                                                                                                                        0.9388888888888889,
                                                                                                                        0.15512820512820513],
                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'focused': False,
                                                                                                                    'checked': False,
                                                                                                                    'editalbe': False,
                                                                                                                    'selected': False,
                                                                                                                    'scrollable': False,
                                                                                                                    'desc': '关闭'}}],
                                                                                               'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                               'payload': {
                                                                                                   'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                   'visible': True,
                                                                                                   'zOrders': {
                                                                                                       'global': 0,
                                                                                                       'local': 2},
                                                                                                   'package': 'com.xunmeng.pinduoduo',
                                                                                                   'anchorPoint': [0.5,
                                                                                                                   0.5],
                                                                                                   'dismissable': False,
                                                                                                   'checkable': False,
                                                                                                   'scale': [1, 1],
                                                                                                   'boundsInParent': [1,
                                                                                                                      0.052564102564102565],
                                                                                                   'focusable': False,
                                                                                                   'type': 'android.widget.FrameLayout',
                                                                                                   'touchable': False,
                                                                                                   'enabled': True,
                                                                                                   'longClickable': False,
                                                                                                   'size': [1,
                                                                                                            0.052564102564102565],
                                                                                                   'pos': [0.5,
                                                                                                           0.15683760683760684],
                                                                                                   'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                   'focused': False,
                                                                                                   'checked': False,
                                                                                                   'editalbe': False,
                                                                                                   'selected': False,
                                                                                                   'scrollable': False}},
                                                                                              {'children': [{
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'children': [
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 1},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.06111111111111111,
                                                                                                                                                                0.02905982905982906],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.06111111111111111,
                                                                                                                                                                0.02905982905982906],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.06388888888888888,
                                                                                                                                                                0.21452991452991452],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}},
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 3},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.7944444444444444,
                                                                                                                                                                0.02094017094017094],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.7944444444444444,
                                                                                                                                                                0.02094017094017094],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.5194444444444445,
                                                                                                                                                                0.2],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'text': '邵士鹏，18368831329，浙江省 杭州市 余杭区 ',
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}},
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 4},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.7944444444444444,
                                                                                                                                                                0.02435897435897436],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.7944444444444444,
                                                                                                                                                                0.02435897435897436],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.5194444444444445,
                                                                                                                                                                0.2264957264957265],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'text': '闲富北路西溪海星海苑1单元303室',
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}},
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 6},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.027777777777777776,
                                                                                                                                                                0.01282051282051282],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.027777777777777776,
                                                                                                                                                                0.01282051282051282],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.9611111111111111,
                                                                                                                                                                0.21452991452991452],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        1,
                                                                                                                                                        0.06965811965811966],
                                                                                                                                                    'focusable': True,
                                                                                                                                                    'type': 'android.view.ViewGroup',
                                                                                                                                                    'touchable': True,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        1,
                                                                                                                                                        0.06965811965811966],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.21794871794871795],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 1},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.06965811965811966],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.06965811965811966],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.21794871794871795],
                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 8},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.010256410256410256],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.view.View',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.010256410256410256],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.25811965811965815],
                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'children': [
                                                                                                                                                            {
                                                                                                                                                                'children': [
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.262037037037037,
                                                                                                                                                                                        0.02863247863247863],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.262037037037037,
                                                                                                                                                                                        0.02863247863247863],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.1638888888888889,
                                                                                                                                                                                        0.28888888888888886],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'text': '券后 ¥7.71 起',
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 2},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.2935185185185185,
                                                                                                                                                                                        0.02094017094017094],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.2935185185185185,
                                                                                                                                                                                        0.02094017094017094],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.4638888888888889,
                                                                                                                                                                                        0.29273504273504275],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'text': '券前¥8.71-24.45',
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 1},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.6805555555555556,
                                                                                                                                                                                0.02863247863247863],
                                                                                                                                                                            'focusable': False,
                                                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.6805555555555556,
                                                                                                                                                                                0.02863247863247863],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.3731481481481482,
                                                                                                                                                                                0.28888888888888886],
                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'android.widget.TextView',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.1638888888888889,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.1638888888888889,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.11481481481481481,
                                                                                                                                                                                        0.32051282051282054],
                                                                                                                                                                                    'name': 'android.widget.TextView',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'text': '2件9.5折',
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'android.widget.TextView',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 2},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.1638888888888889,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.1638888888888889,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.2898148148148148,
                                                                                                                                                                                        0.32051282051282054],
                                                                                                                                                                                    'name': 'android.widget.TextView',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'text': '3件9.4折',
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'android.widget.TextView',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.15555555555555556,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.15555555555555556,
                                                                                                                                                                                        0.02435897435897436],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.46111111111111114,
                                                                                                                                                                                        0.32051282051282054],
                                                                                                                                                                                    'name': 'android.widget.TextView',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'text': '满50减3',
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 3},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.6555555555555556,
                                                                                                                                                                                0.02435897435897436],
                                                                                                                                                                            'focusable': False,
                                                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.6555555555555556,
                                                                                                                                                                                0.02435897435897436],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.3611111111111111,
                                                                                                                                                                                0.32051282051282054],
                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False}},
                                                                                                                                                                    {
                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_select_sku',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_select_sku',
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 5},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.6555555555555556,
                                                                                                                                                                                0.023504273504273504],
                                                                                                                                                                            'focusable': False,
                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.6555555555555556,
                                                                                                                                                                                0.023504273504273504],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.3611111111111111,
                                                                                                                                                                                0.3547008547008547],
                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_select_sku',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'text': '请选择： 颜色 尺寸',
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 1},
                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.6805555555555556,
                                                                                                                                                                        0.09188034188034189],
                                                                                                                                                                    'focusable': False,
                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.6805555555555556,
                                                                                                                                                                        0.09188034188034189],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.3731481481481482,
                                                                                                                                                                        0.32051282051282054],
                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                            {
                                                                                                                                                                'children': [
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.08611111111111111,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.08611111111111111,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.7564814814814815,
                                                                                                                                                                                                0.29444444444444445],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                                            'desc': '减少数量'}},
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 4},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.07777777777777778,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.EditText',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': True,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.07777777777777778,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.8444444444444444,
                                                                                                                                                                                                0.29444444444444445],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '1',
                                                                                                                                                                                            'editalbe': True,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}},
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 6},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.08611111111111111,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.08611111111111111,
                                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.9314814814814815,
                                                                                                                                                                                                0.29444444444444445],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                                            'desc': '增加数量'}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.2611111111111111,
                                                                                                                                                                                        0.03205128205128205],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.2611111111111111,
                                                                                                                                                                                        0.03205128205128205],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8444444444444444,
                                                                                                                                                                                        0.29444444444444445],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/gnl',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/gnl',
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 1},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.2611111111111111,
                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.2611111111111111,
                                                                                                                                                                                0.03205128205128205],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.8444444444444444,
                                                                                                                                                                                0.29444444444444445],
                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/gnl',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 2},
                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.2611111111111111,
                                                                                                                                                                        0.03205128205128205],
                                                                                                                                                                    'focusable': False,
                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.2611111111111111,
                                                                                                                                                                        0.03205128205128205],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.8444444444444444,
                                                                                                                                                                        0.29444444444444445],
                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 3},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                1,
                                                                                                                                                                0.1188034188034188],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                1,
                                                                                                                                                                0.1188034188034188],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.32264957264957267],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        1,
                                                                                                                                                        0.1188034188034188],
                                                                                                                                                    'focusable': True,
                                                                                                                                                    'type': 'android.widget.RelativeLayout',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        1,
                                                                                                                                                        0.1188034188034188],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.32264957264957267],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 10},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.1188034188034188],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.1188034188034188],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.32264957264957267],
                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 11},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                0.9666666666666667,
                                                                                                                                                0.0008547008547008547],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.view.View',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                0.9666666666666667,
                                                                                                                                                0.0008547008547008547],
                                                                                                                                            'pos': [
                                                                                                                                                0.5166666666666667,
                                                                                                                                                0.38247863247863245],
                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 1},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.08333333333333333,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.08333333333333333,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.075,
                                                                                                                                                        0.4115384615384615],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'text': '优惠',
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}},
                                                                                                                                            {
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.8055555555555556,
                                                                                                                                                        0.026923076923076925],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.8055555555555556,
                                                                                                                                                        0.026923076923076925],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5638888888888889,
                                                                                                                                                        0.4115384615384615],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'text': '选择款式后查看优惠',
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}},
                                                                                                                                            {
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 5},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.9666666666666667,
                                                                                                                                                        0.0008547008547008547],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.view.View',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.9666666666666667,
                                                                                                                                                        0.0008547008547008547],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5166666666666667,
                                                                                                                                                        0.44017094017094016],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 12},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.057692307692307696],
                                                                                                                                            'focusable': True,
                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                            'touchable': True,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.057692307692307696],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.4115384615384615],
                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}}],
                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 1},
                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        1,
                                                                                                                                        0.25726495726495724],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        1,
                                                                                                                                        0.25726495726495724],
                                                                                                                                    'pos': [
                                                                                                                                        0.5,
                                                                                                                                        0.31196581196581197],
                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}},
                                                                                                                            {
                                                                                                                                'children': [
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 1},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.08333333333333333,
                                                                                                                                                                0.02606837606837607],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.08333333333333333,
                                                                                                                                                                0.02606837606837607],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.075,
                                                                                                                                                                0.4641025641025641],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'text': '颜色',
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 1},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        1,
                                                                                                                                                        0.047435897435897434],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        1,
                                                                                                                                                        0.047435897435897434],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.4641025641025641],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}},
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'children': [
                                                                                                                                                            {
                                                                                                                                                                'children': [
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.17777777777777778,
                                                                                                                                                                                        0.5547008547008547],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合一（白色+浅灰+卡其+绿色+蓝色）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.27037037037037037,
                                                                                                                                                                                        0.5115384615384615],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.17777777777777778,
                                                                                                                                                                                                0.6256410256410256],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合一（白色+浅灰+卡其+绿色+蓝色）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.17777777777777778,
                                                                                                                                                                                        0.6256410256410256],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合一（白色+浅灰+卡其+绿色+蓝色）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 1},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.17777777777777778,
                                                                                                                                                                                0.5662393162393162],
                                                                                                                                                                            'name': '组合一（白色+浅灰+卡其+绿色+蓝色）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合一（白色+浅灰+卡其+绿色+蓝色）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.4888888888888889,
                                                                                                                                                                                        0.5547008547008547],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合二（浅灰+卡其+军绿+姜黄+黑色）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.5814814814814815,
                                                                                                                                                                                        0.5115384615384615],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.4888888888888889,
                                                                                                                                                                                                0.6256410256410256],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合二（浅灰+卡其+军绿+姜黄+黑色）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.4888888888888889,
                                                                                                                                                                                        0.6256410256410256],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合二（浅灰+卡其+军绿+姜黄+黑色）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 3},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.4888888888888889,
                                                                                                                                                                                0.5662393162393162],
                                                                                                                                                                            'name': '组合二（浅灰+卡其+军绿+姜黄+黑色）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合二（浅灰+卡其+军绿+姜黄+黑色）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8,
                                                                                                                                                                                        0.5547008547008547],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合三（浅灰+卡其+军绿+蓝色+黑色）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8925925925925926,
                                                                                                                                                                                        0.5115384615384615],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.8,
                                                                                                                                                                                                0.6256410256410256],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合三（浅灰+卡其+军绿+蓝色+黑色）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8,
                                                                                                                                                                                        0.6256410256410256],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合三（浅灰+卡其+军绿+蓝色+黑色）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 5},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.8,
                                                                                                                                                                                0.5662393162393162],
                                                                                                                                                                            'name': '组合三（浅灰+卡其+军绿+蓝色+黑色）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合三（浅灰+卡其+军绿+蓝色+黑色）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.03333333333333333,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.9833333333333333,
                                                                                                                                                                                        0.5547008547008547],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合四（黑色装）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.03333333333333333,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.9833333333333333,
                                                                                                                                                                                                0.6256410256410256],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合四（黑色装）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.03333333333333333,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.9833333333333333,
                                                                                                                                                                                        0.6256410256410256],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合四（黑色装）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 7},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.03333333333333333,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.9833333333333333,
                                                                                                                                                                                0.5662393162393162],
                                                                                                                                                                            'name': '组合四（黑色装）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合四（黑色装）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.17777777777777778,
                                                                                                                                                                                        0.7239316239316239],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合五（白色装）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.27037037037037037,
                                                                                                                                                                                        0.6807692307692308],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.17777777777777778,
                                                                                                                                                                                                0.7948717948717948],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合五（白色装）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.17777777777777778,
                                                                                                                                                                                        0.7948717948717948],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合五（白色装）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 2},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.17777777777777778,
                                                                                                                                                                                0.7354700854700855],
                                                                                                                                                                            'name': '组合五（白色装）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合五（白色装）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.4888888888888889,
                                                                                                                                                                                        0.7239316239316239],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合六（黑白组合）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.5814814814814815,
                                                                                                                                                                                        0.6807692307692308],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.4888888888888889,
                                                                                                                                                                                                0.7948717948717948],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合六（黑白组合）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.4888888888888889,
                                                                                                                                                                                        0.7948717948717948],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合六（黑白组合）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 4},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.4888888888888889,
                                                                                                                                                                                0.7354700854700855],
                                                                                                                                                                            'name': '组合六（黑白组合）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合六（黑白组合）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8,
                                                                                                                                                                                        0.7239316239316239],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合七（黑色+深灰+蓝色）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 3},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.10277777777777777,
                                                                                                                                                                                        0.047435897435897434],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8925925925925926,
                                                                                                                                                                                        0.6807692307692308],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '打开大图'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.8,
                                                                                                                                                                                                0.7948717948717948],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合七（黑色+深灰+蓝色）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8,
                                                                                                                                                                                        0.7948717948717948],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合七（黑色+深灰+蓝色）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 6},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.8,
                                                                                                                                                                                0.7354700854700855],
                                                                                                                                                                            'name': '组合七（黑色+深灰+蓝色）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合七（黑色+深灰+蓝色）'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'focusable': True,
                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                    'touchable': True,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.03333333333333333,
                                                                                                                                                                                        0.13333333333333333],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.9833333333333333,
                                                                                                                                                                                        0.7239316239316239],
                                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False,
                                                                                                                                                                                    'desc': '组合八（自选颜色）'}},
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 1},
                                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'focusable': True,
                                                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                                                            'touchable': True,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.03333333333333333,
                                                                                                                                                                                                0.03717948717948718],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.9833333333333333,
                                                                                                                                                                                                0.7948717948717948],
                                                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/tv_content',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'text': '组合八（自选颜色）',
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'android.widget.LinearLayout',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 4},
                                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.28888888888888886,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.03333333333333333,
                                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.9833333333333333,
                                                                                                                                                                                        0.7948717948717948],
                                                                                                                                                                                    'name': 'android.widget.LinearLayout',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '组合八（自选颜色）',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 8},
                                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.28888888888888886,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'focusable': True,
                                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                                            'touchable': True,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.03333333333333333,
                                                                                                                                                                                0.1564102564102564],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.9833333333333333,
                                                                                                                                                                                0.7354700854700855],
                                                                                                                                                                            'name': '组合八（自选颜色）',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '组合八（自选颜色）'}}],
                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 1},
                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.9666666666666667,
                                                                                                                                                                        0.3384615384615385],
                                                                                                                                                                    'focusable': True,
                                                                                                                                                                    'type': 'android.support.v7.widget.RecyclerView',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.9666666666666667,
                                                                                                                                                                        0.3384615384615385],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.5166666666666667,
                                                                                                                                                                        0.6572649572649573],
                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': True}}],
                                                                                                                                                        'name': 'android.widget.FrameLayout',
                                                                                                                                                        'payload': {
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 1},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                1,
                                                                                                                                                                0.3384615384615385],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                1,
                                                                                                                                                                0.3384615384615385],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.6572649572649573],
                                                                                                                                                            'name': 'android.widget.FrameLayout',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}},
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 2},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.18055555555555555,
                                                                                                                                                                0.002564102564102564],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.18055555555555555,
                                                                                                                                                                0.002564102564102564],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.49907407407407406,
                                                                                                                                                                0.832905982905983],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        1,
                                                                                                                                                        0.35384615384615387],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        1,
                                                                                                                                                        0.35384615384615387],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.6649572649572649],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'android.widget.LinearLayout',
                                                                                                                                        'payload': {
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 1},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.4012820512820513],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.4012820512820513],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.6410256410256411],
                                                                                                                                            'name': 'android.widget.LinearLayout',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 1},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.08333333333333333,
                                                                                                                                                                0.02264957264957265],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.TextView',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.08333333333333333,
                                                                                                                                                                0.02264957264957265],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.075,
                                                                                                                                                                0.8606837606837607],
                                                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'text': '尺寸',
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 1},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.9333333333333333,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'focusable': True,
                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                    'touchable': True,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.9333333333333333,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.8606837606837607],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}},
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'children': [
                                                                                                                                                            {
                                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 1},
                                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.8962962962962963,
                                                                                                                                                                        0.03717948717948718],
                                                                                                                                                                    'focusable': True,
                                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                                    'touchable': True,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.8962962962962963,
                                                                                                                                                                        0.009829059829059829],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.48148148148148145,
                                                                                                                                                                        0.8897435897435897],
                                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'text': '帕兰朵-10双组合装（抗菌防臭/不掉跟） ¥23.45',
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                        'name': 'android.view.ViewGroup',
                                                                                                                                                        'payload': {
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 1},
                                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.8962962962962963,
                                                                                                                                                                0.03717948717948718],
                                                                                                                                                            'focusable': True,
                                                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                                                            'touchable': True,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.8962962962962963,
                                                                                                                                                                0.009829059829059829],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.48148148148148145,
                                                                                                                                                                0.8897435897435897],
                                                                                                                                                            'name': 'android.view.ViewGroup',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.9333333333333333,
                                                                                                                                                        0.1371794871794872],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.view.ViewGroup',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.9333333333333333,
                                                                                                                                                        0.009829059829059829],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.8897435897435897],
                                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'android.widget.LinearLayout',
                                                                                                                                        'payload': {
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 2},
                                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                1,
                                                                                                                                                0.19572649572649573],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                1,
                                                                                                                                                0.05299145299145299],
                                                                                                                                            'pos': [
                                                                                                                                                0.5,
                                                                                                                                                0.8683760683760684],
                                                                                                                                            'name': 'android.widget.LinearLayout',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}}],
                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 2},
                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        1,
                                                                                                                                        0.4829059829059829],
                                                                                                                                    'focusable': True,
                                                                                                                                    'type': 'android.support.v7.widget.RecyclerView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        1,
                                                                                                                                        0.45427350427350427],
                                                                                                                                    'pos': [
                                                                                                                                        0.5,
                                                                                                                                        0.6675213675213675],
                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': True}}],
                                                                                                                        'name': 'android.view.ViewGroup',
                                                                                                                        'payload': {
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 1},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                1,
                                                                                                                                0.7115384615384616],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.view.ViewGroup',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                1,
                                                                                                                                0.7115384615384616],
                                                                                                                            'pos': [
                                                                                                                                0.5,
                                                                                                                                0.5388888888888889],
                                                                                                                            'name': 'android.view.ViewGroup',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}}],
                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                'payload': {
                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'visible': True,
                                                                                                                    'zOrders': {
                                                                                                                        'global': 0,
                                                                                                                        'local': 3},
                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                    'anchorPoint': [
                                                                                                                        0.5,
                                                                                                                        0.5],
                                                                                                                    'dismissable': False,
                                                                                                                    'checkable': False,
                                                                                                                    'scale': [
                                                                                                                        1,
                                                                                                                        1],
                                                                                                                    'boundsInParent': [
                                                                                                                        1,
                                                                                                                        0.7115384615384616],
                                                                                                                    'focusable': False,
                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                    'touchable': False,
                                                                                                                    'enabled': True,
                                                                                                                    'longClickable': False,
                                                                                                                    'size': [
                                                                                                                        1,
                                                                                                                        0.7115384615384616],
                                                                                                                    'pos': [
                                                                                                                        0.5,
                                                                                                                        0.5388888888888889],
                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'focused': False,
                                                                                                                    'checked': False,
                                                                                                                    'editalbe': False,
                                                                                                                    'selected': False,
                                                                                                                    'scrollable': False}},
                                                                                                            {
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                        'payload': {
                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 1},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                1,
                                                                                                                                0.0008547008547008547],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.view.View',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                1,
                                                                                                                                0.0008547008547008547],
                                                                                                                            'pos': [
                                                                                                                                0.5,
                                                                                                                                0.8952991452991453],
                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}},
                                                                                                                    {
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 1},
                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.7777777777777778,
                                                                                                                                        0.02435897435897436],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.7777777777777778,
                                                                                                                                        0.02435897435897436],
                                                                                                                                    'pos': [
                                                                                                                                        0.4824074074074074,
                                                                                                                                        0.9158119658119658],
                                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'text': '使用#先用后付，更换多多支付最高减16元',
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}}],
                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                        'payload': {
                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 2},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                0.7944444444444444,
                                                                                                                                0.02435897435897436],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                0.7944444444444444,
                                                                                                                                0.02435897435897436],
                                                                                                                            'pos': [
                                                                                                                                0.4740740740740741,
                                                                                                                                0.9158119658119658],
                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}},
                                                                                                                    {
                                                                                                                        'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                        'payload': {
                                                                                                                            'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 3},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                0.027777777777777776,
                                                                                                                                0.01282051282051282],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.widget.ImageView',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                0.027777777777777776,
                                                                                                                                0.01282051282051282],
                                                                                                                            'pos': [
                                                                                                                                0.8935185185185185,
                                                                                                                                0.9158119658119658],
                                                                                                                            'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}}],
                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                'payload': {
                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'visible': True,
                                                                                                                    'zOrders': {
                                                                                                                        'global': 0,
                                                                                                                        'local': 6},
                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                    'anchorPoint': [
                                                                                                                        0.5,
                                                                                                                        0.5],
                                                                                                                    'dismissable': False,
                                                                                                                    'checkable': False,
                                                                                                                    'scale': [
                                                                                                                        1,
                                                                                                                        1],
                                                                                                                    'boundsInParent': [
                                                                                                                        1,
                                                                                                                        0.04230769230769231],
                                                                                                                    'focusable': True,
                                                                                                                    'type': 'android.view.ViewGroup',
                                                                                                                    'touchable': True,
                                                                                                                    'enabled': True,
                                                                                                                    'longClickable': False,
                                                                                                                    'size': [
                                                                                                                        1,
                                                                                                                        0.04230769230769231],
                                                                                                                    'pos': [
                                                                                                                        0.5,
                                                                                                                        0.9158119658119658],
                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'focused': False,
                                                                                                                    'checked': False,
                                                                                                                    'editalbe': False,
                                                                                                                    'selected': False,
                                                                                                                    'scrollable': False}},
                                                                                                            {
                                                                                                                'children': [
                                                                                                                    {
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'name': 'android.widget.TextView',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 1},
                                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.18888888888888888,
                                                                                                                                        0.02905982905982906],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.18888888888888888,
                                                                                                                                        0.02905982905982906],
                                                                                                                                    'pos': [
                                                                                                                                        0.5,
                                                                                                                                        0.9683760683760684],
                                                                                                                                    'name': 'android.widget.TextView',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'text': '立即支付',
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}}],
                                                                                                                        'name': 'android.widget.LinearLayout',
                                                                                                                        'payload': {
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 1},
                                                                                                                            'package': 'com.xunmeng.pinduoduo',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                0.18888888888888888,
                                                                                                                                0.06282051282051282],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                0.18888888888888888,
                                                                                                                                0.06282051282051282],
                                                                                                                            'pos': [
                                                                                                                                0.5,
                                                                                                                                0.9683760683760684],
                                                                                                                            'name': 'android.widget.LinearLayout',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}}],
                                                                                                                'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                'payload': {
                                                                                                                    'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'visible': True,
                                                                                                                    'zOrders': {
                                                                                                                        'global': 0,
                                                                                                                        'local': 9},
                                                                                                                    'package': 'com.xunmeng.pinduoduo',
                                                                                                                    'anchorPoint': [
                                                                                                                        0.5,
                                                                                                                        0.5],
                                                                                                                    'dismissable': False,
                                                                                                                    'checkable': False,
                                                                                                                    'scale': [
                                                                                                                        1,
                                                                                                                        1],
                                                                                                                    'boundsInParent': [
                                                                                                                        1,
                                                                                                                        0.06282051282051282],
                                                                                                                    'focusable': True,
                                                                                                                    'type': 'android.widget.FrameLayout',
                                                                                                                    'touchable': True,
                                                                                                                    'enabled': True,
                                                                                                                    'longClickable': False,
                                                                                                                    'size': [
                                                                                                                        1,
                                                                                                                        0.06282051282051282],
                                                                                                                    'pos': [
                                                                                                                        0.5,
                                                                                                                        0.9683760683760684],
                                                                                                                    'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                                    'focused': False,
                                                                                                                    'checked': False,
                                                                                                                    'editalbe': False,
                                                                                                                    'selected': False,
                                                                                                                    'scrollable': False}}],
                                                                                               'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                               'payload': {
                                                                                                   'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                   'visible': True,
                                                                                                   'zOrders': {
                                                                                                       'global': 0,
                                                                                                       'local': 3},
                                                                                                   'package': 'com.xunmeng.pinduoduo',
                                                                                                   'anchorPoint': [0.5,
                                                                                                                   0.5],
                                                                                                   'dismissable': False,
                                                                                                   'checkable': False,
                                                                                                   'scale': [1, 1],
                                                                                                   'boundsInParent': [1,
                                                                                                                      0.8166666666666667],
                                                                                                   'focusable': True,
                                                                                                   'type': 'android.view.ViewGroup',
                                                                                                   'touchable': True,
                                                                                                   'enabled': True,
                                                                                                   'longClickable': False,
                                                                                                   'size': [1,
                                                                                                            0.8166666666666667],
                                                                                                   'pos': [0.5,
                                                                                                           0.5914529914529915],
                                                                                                   'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                                   'focused': False,
                                                                                                   'checked': False,
                                                                                                   'editalbe': False,
                                                                                                   'selected': False,
                                                                                                   'scrollable': False}}],
                                                                                 'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                 'payload': {
                                                                                     'resourceId': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                     'visible': True,
                                                                                     'zOrders': {'global': 0,
                                                                                                 'local': 1},
                                                                                     'package': 'com.xunmeng.pinduoduo',
                                                                                     'anchorPoint': [0.5, 0.5],
                                                                                     'dismissable': False,
                                                                                     'checkable': False,
                                                                                     'scale': [1, 1],
                                                                                     'boundsInParent': [1,
                                                                                                        0.9551282051282052],
                                                                                     'focusable': True,
                                                                                     'type': 'android.widget.LinearLayout',
                                                                                     'touchable': True, 'enabled': True,
                                                                                     'longClickable': False,
                                                                                     'size': [1, 0.9551282051282052],
                                                                                     'pos': [0.5, 0.5222222222222223],
                                                                                     'name': 'com.xunmeng.pinduoduo:id/pdd',
                                                                                     'focused': False, 'checked': False,
                                                                                     'editalbe': False,
                                                                                     'selected': False,
                                                                                     'scrollable': False}}],
                                                                   'name': 'com.xunmeng.pinduoduo:id/pdd', 'payload': {
        'resourceId': 'com.xunmeng.pinduoduo:id/pdd', 'visible': True, 'zOrders': {'global': 0, 'local': 1},
        'package': 'com.xunmeng.pinduoduo', 'anchorPoint': [0.5, 0.5], 'dismissable': False, 'checkable': False,
        'scale': [1, 1], 'boundsInParent': [1, 0.9551282051282052], 'focusable': False,
        'type': 'android.widget.FrameLayout', 'touchable': False, 'enabled': True, 'longClickable': False,
        'size': [1, 0.9551282051282052], 'pos': [0.5, 0.5222222222222223], 'name': 'com.xunmeng.pinduoduo:id/pdd',
        'focused': False, 'checked': False, 'editalbe': False, 'selected': False, 'scrollable': False}}],
                                                     'name': 'android:id/content',
                                                     'payload': {'resourceId': 'android:id/content', 'visible': True,
                                                                 'zOrders': {'global': 0, 'local': 2},
                                                                 'package': 'com.xunmeng.pinduoduo',
                                                                 'anchorPoint': [0.5, 0.5], 'dismissable': False,
                                                                 'checkable': False, 'scale': [1, 1],
                                                                 'boundsInParent': [1, 0.9551282051282052],
                                                                 'focusable': False,
                                                                 'type': 'android.widget.FrameLayout',
                                                                 'touchable': False, 'enabled': True,
                                                                 'longClickable': False,
                                                                 'size': [1, 0.9551282051282052],
                                                                 'pos': [0.5, 0.5222222222222223],
                                                                 'name': 'android:id/content', 'focused': False,
                                                                 'checked': False, 'editalbe': False, 'selected': False,
                                                                 'scrollable': False}}],
                                       'name': 'android.widget.LinearLayout',
                                       'payload': {'visible': True, 'zOrders': {'global': 0, 'local': 1},
                                                   'package': 'com.xunmeng.pinduoduo', 'anchorPoint': [0.5, 0.5],
                                                   'dismissable': False, 'checkable': False, 'scale': [1, 1],
                                                   'boundsInParent': [1, 1], 'focusable': False,
                                                   'type': 'android.widget.LinearLayout', 'touchable': False,
                                                   'enabled': True, 'longClickable': False, 'size': [1, 1],
                                                   'pos': [0.5, 0.5], 'name': 'android.widget.LinearLayout',
                                                   'focused': False, 'checked': False, 'editalbe': False,
                                                   'selected': False, 'scrollable': False}}],
                         'name': 'android.widget.FrameLayout',
                         'payload': {'visible': True, 'zOrders': {'global': 0, 'local': 0},
                                     'package': 'com.xunmeng.pinduoduo', 'anchorPoint': [0.5, 0.5],
                                     'dismissable': False, 'checkable': False, 'scale': [1, 1],
                                     'boundsInParent': [1, 1], 'focusable': False, 'type': 'android.widget.FrameLayout',
                                     'touchable': False, 'enabled': True, 'longClickable': False, 'size': [1, 1],
                                     'pos': [0.5, 0.5], 'name': 'android.widget.FrameLayout', 'focused': False,
                                     'checked': False, 'editalbe': False, 'selected': False, 'scrollable': False}},
                        {'name': 'android.view.View',
                         'payload': {'visible': True, 'zOrders': {'global': 0, 'local': 0}, 'package': 'android',
                                     'anchorPoint': [0.5, 0.5], 'dismissable': False, 'checkable': False,
                                     'scale': [1, 1], 'boundsInParent': [0.044444444444444446, 0.75],
                                     'focusable': False, 'type': 'android.view.View', 'touchable': False,
                                     'enabled': True, 'longClickable': False, 'size': [0.044444444444444446, 0.75],
                                     'pos': [0.022222222222222223, 0.6247863247863248], 'name': 'android.view.View',
                                     'focused': False, 'checked': False, 'editalbe': False, 'selected': False,
                                     'scrollable': False}}, {'children': [{'children': [{'children': [{'children': [{
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'name': 'com.android.systemui:id/clock',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.android.systemui:id/clock',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 3},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.07685185185185185,
                                                                                                                                        0.024786324786324785],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.07685185185185185,
                                                                                                                                        0.024786324786324785],
                                                                                                                                    'pos': [
                                                                                                                                        0.09074074074074075,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': 'com.android.systemui:id/clock',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'text': '2:45',
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}}],
                                                                                                                        'name': 'com.android.systemui:id/status_bar_start',
                                                                                                                        'payload': {
                                                                                                                            'resourceId': 'com.android.systemui:id/status_bar_start',
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 3},
                                                                                                                            'package': 'com.android.systemui',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                0.08055555555555556,
                                                                                                                                0.04401709401709402],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                0.08055555555555556,
                                                                                                                                0.04401709401709402],
                                                                                                                            'pos': [
                                                                                                                                0.09259259259259259,
                                                                                                                                0.02264957264957265],
                                                                                                                            'name': 'com.android.systemui:id/status_bar_start',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}},
                                                                                                                    {
                                                                                                                        'children': [
                                                                                                                            {
                                                                                                                                'name': '流量节省程序已开启',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 3},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.03888888888888889,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.03888888888888889,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'pos': [
                                                                                                                                        0.1527777777777778,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': '流量节省程序已开启',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False,
                                                                                                                                    'desc': '流量节省程序已开启'}},
                                                                                                                            {
                                                                                                                                'name': '开启性能模式',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 8},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.04351851851851852,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.04351851851851852,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'pos': [
                                                                                                                                        0.19722222222222222,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': '开启性能模式',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False,
                                                                                                                                    'desc': '开启性能模式'}},
                                                                                                                            {
                                                                                                                                'name': '已设置闹钟。',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 12},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.040740740740740744,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.040740740740740744,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'pos': [
                                                                                                                                        0.24351851851851852,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': '已设置闹钟。',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False,
                                                                                                                                    'desc': '已设置闹钟。'}},
                                                                                                                            {
                                                                                                                                'name': '已连接到蓝牙耳机，电量：50%',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 13},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.05092592592592592,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.05092592592592592,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'pos': [
                                                                                                                                        0.29259259259259257,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': '已连接到蓝牙耳机，电量：50%',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False,
                                                                                                                                    'desc': '已连接到蓝牙耳机，电量：50%'}},
                                                                                                                            {
                                                                                                                                'name': '振铃器静音。',
                                                                                                                                'payload': {
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 17},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.03518518518518519,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.03518518518518519,
                                                                                                                                        0.026495726495726495],
                                                                                                                                    'pos': [
                                                                                                                                        0.6638888888888889,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': '振铃器静音。',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False,
                                                                                                                                    'desc': '振铃器静音。'}},
                                                                                                                            {
                                                                                                                                'children': [
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'children': [
                                                                                                                                                    {
                                                                                                                                                        'children': [
                                                                                                                                                            {
                                                                                                                                                                'name': 'com.android.systemui:id/wifi_signal_dark',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.android.systemui:id/wifi_signal_dark',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 2},
                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.04814814814814815,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'focusable': False,
                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.04814814814814815,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.7092592592592593,
                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                    'name': 'com.android.systemui:id/wifi_signal_dark',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                            {
                                                                                                                                                                'name': 'com.android.systemui:id/wifi_inout',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.android.systemui:id/wifi_inout',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 3},
                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.04814814814814815,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'focusable': False,
                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.04814814814814815,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.7092592592592593,
                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                    'name': 'com.android.systemui:id/wifi_inout',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                        'name': 'com.android.systemui:id/wifi_combo',
                                                                                                                                                        'payload': {
                                                                                                                                                            'resourceId': 'com.android.systemui:id/wifi_combo',
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 2},
                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.04814814814814815,
                                                                                                                                                                0.019230769230769232],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.04814814814814815,
                                                                                                                                                                0.019230769230769232],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.7092592592592593,
                                                                                                                                                                0.02264957264957265],
                                                                                                                                                            'name': 'com.android.systemui:id/wifi_combo',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False,
                                                                                                                                                            'desc': 'WLAN 信号强度满格。'}},
                                                                                                                                                    {
                                                                                                                                                        'children': [
                                                                                                                                                            {
                                                                                                                                                                'children': [
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'children': [
                                                                                                                                                                                            {
                                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                'payload': {
                                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                                        0.5,
                                                                                                                                                                                                        0.5],
                                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                                    'scale': [
                                                                                                                                                                                                        1,
                                                                                                                                                                                                        1],
                                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                                    'size': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'pos': [
                                                                                                                                                                                                        0.7638888888888888,
                                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                                                            {
                                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                'payload': {
                                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                                        'local': 2},
                                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                                        0.5,
                                                                                                                                                                                                        0.5],
                                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                                    'scale': [
                                                                                                                                                                                                        1,
                                                                                                                                                                                                        1],
                                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                                    'size': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'pos': [
                                                                                                                                                                                                        0.7638888888888888,
                                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                                        'name': 'android.widget.FrameLayout',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 3},
                                                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.053703703703703705,
                                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                                            'focusable': False,
                                                                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                                                                            'touchable': False,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.053703703703703705,
                                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.7638888888888888,
                                                                                                                                                                                                0.02264957264957265],
                                                                                                                                                                                            'name': 'android.widget.FrameLayout',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.FrameLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.7638888888888888,
                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '4G 手机信号满格。',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 1},
                                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.05740740740740741,
                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                            'focusable': False,
                                                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.05740740740740741,
                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.7638888888888888,
                                                                                                                                                                                0.02264957264957265],
                                                                                                                                                                            'name': '4G 手机信号满格。',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '4G 手机信号满格。'}},
                                                                                                                                                                    {
                                                                                                                                                                        'children': [
                                                                                                                                                                            {
                                                                                                                                                                                'children': [
                                                                                                                                                                                    {
                                                                                                                                                                                        'children': [
                                                                                                                                                                                            {
                                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                'payload': {
                                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                                        0.5,
                                                                                                                                                                                                        0.5],
                                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                                    'scale': [
                                                                                                                                                                                                        1,
                                                                                                                                                                                                        1],
                                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                                    'size': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'pos': [
                                                                                                                                                                                                        0.8212962962962963,
                                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_signal',
                                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                                    'scrollable': False}},
                                                                                                                                                                                            {
                                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                'payload': {
                                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                                        'local': 2},
                                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                                        0.5,
                                                                                                                                                                                                        0.5],
                                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                                    'scale': [
                                                                                                                                                                                                        1,
                                                                                                                                                                                                        1],
                                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                                    'size': [
                                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                                    'pos': [
                                                                                                                                                                                                        0.8212962962962963,
                                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_signal_type',
                                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                                        'name': 'android.widget.FrameLayout',
                                                                                                                                                                                        'payload': {
                                                                                                                                                                                            'visible': True,
                                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                                'global': 0,
                                                                                                                                                                                                'local': 3},
                                                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                                0.5,
                                                                                                                                                                                                0.5],
                                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                                            'checkable': False,
                                                                                                                                                                                            'scale': [
                                                                                                                                                                                                1,
                                                                                                                                                                                                1],
                                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                                0.053703703703703705,
                                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                                            'focusable': False,
                                                                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                                                                            'touchable': False,
                                                                                                                                                                                            'enabled': True,
                                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                                            'size': [
                                                                                                                                                                                                0.053703703703703705,
                                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                                            'pos': [
                                                                                                                                                                                                0.8212962962962963,
                                                                                                                                                                                                0.02264957264957265],
                                                                                                                                                                                            'name': 'android.widget.FrameLayout',
                                                                                                                                                                                            'focused': False,
                                                                                                                                                                                            'checked': False,
                                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                                            'selected': False,
                                                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                                                'name': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                'payload': {
                                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                    'visible': True,
                                                                                                                                                                                    'zOrders': {
                                                                                                                                                                                        'global': 0,
                                                                                                                                                                                        'local': 1},
                                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                                        0.5,
                                                                                                                                                                                        0.5],
                                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                                    'checkable': False,
                                                                                                                                                                                    'scale': [
                                                                                                                                                                                        1,
                                                                                                                                                                                        1],
                                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                    'focusable': False,
                                                                                                                                                                                    'type': 'android.widget.FrameLayout',
                                                                                                                                                                                    'touchable': False,
                                                                                                                                                                                    'enabled': True,
                                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                                    'size': [
                                                                                                                                                                                        0.053703703703703705,
                                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                                    'pos': [
                                                                                                                                                                                        0.8212962962962963,
                                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_group',
                                                                                                                                                                                    'focused': False,
                                                                                                                                                                                    'checked': False,
                                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                                    'selected': False,
                                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                                        'name': '4G 手机信号满格。',
                                                                                                                                                                        'payload': {
                                                                                                                                                                            'visible': True,
                                                                                                                                                                            'zOrders': {
                                                                                                                                                                                'global': 0,
                                                                                                                                                                                'local': 2},
                                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                                0.5,
                                                                                                                                                                                0.5],
                                                                                                                                                                            'dismissable': False,
                                                                                                                                                                            'checkable': False,
                                                                                                                                                                            'scale': [
                                                                                                                                                                                1,
                                                                                                                                                                                1],
                                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                                0.05740740740740741,
                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                            'focusable': False,
                                                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                                                            'touchable': False,
                                                                                                                                                                            'enabled': True,
                                                                                                                                                                            'longClickable': False,
                                                                                                                                                                            'size': [
                                                                                                                                                                                0.05740740740740741,
                                                                                                                                                                                0.019230769230769232],
                                                                                                                                                                            'pos': [
                                                                                                                                                                                0.8212962962962963,
                                                                                                                                                                                0.02264957264957265],
                                                                                                                                                                            'name': '4G 手机信号满格。',
                                                                                                                                                                            'focused': False,
                                                                                                                                                                            'checked': False,
                                                                                                                                                                            'editalbe': False,
                                                                                                                                                                            'selected': False,
                                                                                                                                                                            'scrollable': False,
                                                                                                                                                                            'desc': '4G 手机信号满格。'}}],
                                                                                                                                                                'name': 'com.android.systemui:id/mobile_combo',
                                                                                                                                                                'payload': {
                                                                                                                                                                    'resourceId': 'com.android.systemui:id/mobile_combo',
                                                                                                                                                                    'visible': True,
                                                                                                                                                                    'zOrders': {
                                                                                                                                                                        'global': 0,
                                                                                                                                                                        'local': 2},
                                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                                    'anchorPoint': [
                                                                                                                                                                        0.5,
                                                                                                                                                                        0.5],
                                                                                                                                                                    'dismissable': False,
                                                                                                                                                                    'checkable': False,
                                                                                                                                                                    'scale': [
                                                                                                                                                                        1,
                                                                                                                                                                        1],
                                                                                                                                                                    'boundsInParent': [
                                                                                                                                                                        0.11481481481481481,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'focusable': False,
                                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                                    'touchable': False,
                                                                                                                                                                    'enabled': True,
                                                                                                                                                                    'longClickable': False,
                                                                                                                                                                    'size': [
                                                                                                                                                                        0.11481481481481481,
                                                                                                                                                                        0.019230769230769232],
                                                                                                                                                                    'pos': [
                                                                                                                                                                        0.7925925925925926,
                                                                                                                                                                        0.02264957264957265],
                                                                                                                                                                    'name': 'com.android.systemui:id/mobile_combo',
                                                                                                                                                                    'focused': False,
                                                                                                                                                                    'checked': False,
                                                                                                                                                                    'editalbe': False,
                                                                                                                                                                    'selected': False,
                                                                                                                                                                    'scrollable': False}}],
                                                                                                                                                        'name': 'android.widget.FrameLayout',
                                                                                                                                                        'payload': {
                                                                                                                                                            'visible': True,
                                                                                                                                                            'zOrders': {
                                                                                                                                                                'global': 0,
                                                                                                                                                                'local': 7},
                                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                                            'anchorPoint': [
                                                                                                                                                                0.5,
                                                                                                                                                                0.5],
                                                                                                                                                            'dismissable': False,
                                                                                                                                                            'checkable': False,
                                                                                                                                                            'scale': [
                                                                                                                                                                1,
                                                                                                                                                                1],
                                                                                                                                                            'boundsInParent': [
                                                                                                                                                                0.11481481481481481,
                                                                                                                                                                0.019230769230769232],
                                                                                                                                                            'focusable': False,
                                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                                            'touchable': False,
                                                                                                                                                            'enabled': True,
                                                                                                                                                            'longClickable': False,
                                                                                                                                                            'size': [
                                                                                                                                                                0.11481481481481481,
                                                                                                                                                                0.019230769230769232],
                                                                                                                                                            'pos': [
                                                                                                                                                                0.7925925925925926,
                                                                                                                                                                0.02264957264957265],
                                                                                                                                                            'name': 'android.widget.FrameLayout',
                                                                                                                                                            'focused': False,
                                                                                                                                                            'checked': False,
                                                                                                                                                            'editalbe': False,
                                                                                                                                                            'selected': False,
                                                                                                                                                            'scrollable': False}}],
                                                                                                                                                'name': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 2},
                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.16666666666666666,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.16666666666666666,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.7666666666666667,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'name': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'com.android.systemui:id/signal_cluster',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.android.systemui:id/signal_cluster',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 1},
                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                0.16666666666666666,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                0.16666666666666666,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'pos': [
                                                                                                                                                0.7666666666666667,
                                                                                                                                                0.02264957264957265],
                                                                                                                                            'name': 'com.android.systemui:id/signal_cluster',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}}],
                                                                                                                                'name': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 22},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.16666666666666666,
                                                                                                                                        0.019230769230769232],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.FrameLayout',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.16666666666666666,
                                                                                                                                        0.019230769230769232],
                                                                                                                                    'pos': [
                                                                                                                                        0.7666666666666667,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': 'com.android.systemui:id/signal_cluster_container',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}},
                                                                                                                            {
                                                                                                                                'children': [
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'name': 'com.android.systemui:id/battery_border',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.android.systemui:id/battery_border',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 1},
                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.075,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.075,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.8888888888888888,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'name': 'com.android.systemui:id/battery_border',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False,
                                                                                                                                                    'desc': '正在充电，已完成百分之50。'}},
                                                                                                                                            {
                                                                                                                                                'name': 'com.android.systemui:id/battery_inside_percent',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.android.systemui:id/battery_inside_percent',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 5},
                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.040740740740740744,
                                                                                                                                                        0.018803418803418803],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.TextView',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.040740740740740744,
                                                                                                                                                        0.018376068376068377],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.8888888888888888,
                                                                                                                                                        0.022222222222222223],
                                                                                                                                                    'name': 'com.android.systemui:id/battery_inside_percent',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'text': '50',
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'com.android.systemui:id/battery_inside',
                                                                                                                                        'payload': {
                                                                                                                                            'resourceId': 'com.android.systemui:id/battery_inside',
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 2},
                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                0.075,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                0.075,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'pos': [
                                                                                                                                                0.8888888888888888,
                                                                                                                                                0.02264957264957265],
                                                                                                                                            'name': 'com.android.systemui:id/battery_inside',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}},
                                                                                                                                    {
                                                                                                                                        'children': [
                                                                                                                                            {
                                                                                                                                                'name': 'com.android.systemui:id/battery_outside_charge',
                                                                                                                                                'payload': {
                                                                                                                                                    'resourceId': 'com.android.systemui:id/battery_outside_charge',
                                                                                                                                                    'visible': True,
                                                                                                                                                    'zOrders': {
                                                                                                                                                        'global': 0,
                                                                                                                                                        'local': 1},
                                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                                    'anchorPoint': [
                                                                                                                                                        0.5,
                                                                                                                                                        0.5],
                                                                                                                                                    'dismissable': False,
                                                                                                                                                    'checkable': False,
                                                                                                                                                    'scale': [
                                                                                                                                                        1,
                                                                                                                                                        1],
                                                                                                                                                    'boundsInParent': [
                                                                                                                                                        0.019444444444444445,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'focusable': False,
                                                                                                                                                    'type': 'android.widget.ImageView',
                                                                                                                                                    'touchable': False,
                                                                                                                                                    'enabled': True,
                                                                                                                                                    'longClickable': False,
                                                                                                                                                    'size': [
                                                                                                                                                        0.019444444444444445,
                                                                                                                                                        0.019230769230769232],
                                                                                                                                                    'pos': [
                                                                                                                                                        0.937037037037037,
                                                                                                                                                        0.02264957264957265],
                                                                                                                                                    'name': 'com.android.systemui:id/battery_outside_charge',
                                                                                                                                                    'focused': False,
                                                                                                                                                    'checked': False,
                                                                                                                                                    'editalbe': False,
                                                                                                                                                    'selected': False,
                                                                                                                                                    'scrollable': False}}],
                                                                                                                                        'name': 'android.widget.FrameLayout',
                                                                                                                                        'payload': {
                                                                                                                                            'visible': True,
                                                                                                                                            'zOrders': {
                                                                                                                                                'global': 0,
                                                                                                                                                'local': 4},
                                                                                                                                            'package': 'com.android.systemui',
                                                                                                                                            'anchorPoint': [
                                                                                                                                                0.5,
                                                                                                                                                0.5],
                                                                                                                                            'dismissable': False,
                                                                                                                                            'checkable': False,
                                                                                                                                            'scale': [
                                                                                                                                                1,
                                                                                                                                                1],
                                                                                                                                            'boundsInParent': [
                                                                                                                                                0.019444444444444445,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'focusable': False,
                                                                                                                                            'type': 'android.widget.FrameLayout',
                                                                                                                                            'touchable': False,
                                                                                                                                            'enabled': True,
                                                                                                                                            'longClickable': False,
                                                                                                                                            'size': [
                                                                                                                                                0.019444444444444445,
                                                                                                                                                0.019230769230769232],
                                                                                                                                            'pos': [
                                                                                                                                                0.937037037037037,
                                                                                                                                                0.02264957264957265],
                                                                                                                                            'name': 'android.widget.FrameLayout',
                                                                                                                                            'focused': False,
                                                                                                                                            'checked': False,
                                                                                                                                            'editalbe': False,
                                                                                                                                            'selected': False,
                                                                                                                                            'scrollable': False}}],
                                                                                                                                'name': 'com.android.systemui:id/battery',
                                                                                                                                'payload': {
                                                                                                                                    'resourceId': 'com.android.systemui:id/battery',
                                                                                                                                    'visible': True,
                                                                                                                                    'zOrders': {
                                                                                                                                        'global': 0,
                                                                                                                                        'local': 23},
                                                                                                                                    'package': 'com.android.systemui',
                                                                                                                                    'anchorPoint': [
                                                                                                                                        0.5,
                                                                                                                                        0.5],
                                                                                                                                    'dismissable': False,
                                                                                                                                    'checkable': False,
                                                                                                                                    'scale': [
                                                                                                                                        1,
                                                                                                                                        1],
                                                                                                                                    'boundsInParent': [
                                                                                                                                        0.09537037037037037,
                                                                                                                                        0.019230769230769232],
                                                                                                                                    'focusable': False,
                                                                                                                                    'type': 'android.widget.LinearLayout',
                                                                                                                                    'touchable': False,
                                                                                                                                    'enabled': True,
                                                                                                                                    'longClickable': False,
                                                                                                                                    'size': [
                                                                                                                                        0.09537037037037037,
                                                                                                                                        0.019230769230769232],
                                                                                                                                    'pos': [
                                                                                                                                        0.899074074074074,
                                                                                                                                        0.02264957264957265],
                                                                                                                                    'name': 'com.android.systemui:id/battery',
                                                                                                                                    'focused': False,
                                                                                                                                    'checked': False,
                                                                                                                                    'editalbe': False,
                                                                                                                                    'selected': False,
                                                                                                                                    'scrollable': False}}],
                                                                                                                        'name': 'com.android.systemui:id/status_bar_end',
                                                                                                                        'payload': {
                                                                                                                            'resourceId': 'com.android.systemui:id/status_bar_end',
                                                                                                                            'visible': True,
                                                                                                                            'zOrders': {
                                                                                                                                'global': 0,
                                                                                                                                'local': 4},
                                                                                                                            'package': 'com.android.systemui',
                                                                                                                            'anchorPoint': [
                                                                                                                                0.5,
                                                                                                                                0.5],
                                                                                                                            'dismissable': False,
                                                                                                                            'checkable': False,
                                                                                                                            'scale': [
                                                                                                                                1,
                                                                                                                                1],
                                                                                                                            'boundsInParent': [
                                                                                                                                0.8138888888888889,
                                                                                                                                0.04401709401709402],
                                                                                                                            'focusable': False,
                                                                                                                            'type': 'android.widget.LinearLayout',
                                                                                                                            'touchable': False,
                                                                                                                            'enabled': True,
                                                                                                                            'longClickable': False,
                                                                                                                            'size': [
                                                                                                                                0.8138888888888889,
                                                                                                                                0.04401709401709402],
                                                                                                                            'pos': [
                                                                                                                                0.5398148148148149,
                                                                                                                                0.02264957264957265],
                                                                                                                            'name': 'com.android.systemui:id/status_bar_end',
                                                                                                                            'focused': False,
                                                                                                                            'checked': False,
                                                                                                                            'editalbe': False,
                                                                                                                            'selected': False,
                                                                                                                            'scrollable': False}}],
                                                                                                       'name': 'com.android.systemui:id/status_bar_contents',
                                                                                                       'payload': {
                                                                                                           'resourceId': 'com.android.systemui:id/status_bar_contents',
                                                                                                           'visible': True,
                                                                                                           'zOrders': {
                                                                                                               'global': 0,
                                                                                                               'local': 2},
                                                                                                           'package': 'com.android.systemui',
                                                                                                           'anchorPoint': [
                                                                                                               0.5,
                                                                                                               0.5],
                                                                                                           'dismissable': False,
                                                                                                           'checkable': False,
                                                                                                           'scale': [1,
                                                                                                                     1],
                                                                                                           'boundsInParent': [
                                                                                                               1,
                                                                                                               0.04487179487179487],
                                                                                                           'focusable': False,
                                                                                                           'type': 'android.widget.FrameLayout',
                                                                                                           'touchable': False,
                                                                                                           'enabled': True,
                                                                                                           'longClickable': False,
                                                                                                           'size': [1,
                                                                                                                    0.04487179487179487],
                                                                                                           'pos': [0.5,
                                                                                                                   0.022222222222222223],
                                                                                                           'name': 'com.android.systemui:id/status_bar_contents',
                                                                                                           'focused': False,
                                                                                                           'checked': False,
                                                                                                           'editalbe': False,
                                                                                                           'selected': False,
                                                                                                           'scrollable': False}}],
                                                                                         'name': 'com.android.systemui:id/status_bar',
                                                                                         'payload': {
                                                                                             'resourceId': 'com.android.systemui:id/status_bar',
                                                                                             'visible': True,
                                                                                             'zOrders': {'global': 0,
                                                                                                         'local': 1},
                                                                                             'package': 'com.android.systemui',
                                                                                             'anchorPoint': [0.5, 0.5],
                                                                                             'dismissable': False,
                                                                                             'checkable': False,
                                                                                             'scale': [1, 1],
                                                                                             'boundsInParent': [1,
                                                                                                                0.04487179487179487],
                                                                                             'focusable': False,
                                                                                             'type': 'android.widget.FrameLayout',
                                                                                             'touchable': False,
                                                                                             'enabled': True,
                                                                                             'longClickable': False,
                                                                                             'size': [1,
                                                                                                      0.04487179487179487],
                                                                                             'pos': [0.5,
                                                                                                     0.022222222222222223],
                                                                                             'name': 'com.android.systemui:id/status_bar',
                                                                                             'focused': False,
                                                                                             'checked': False,
                                                                                             'editalbe': False,
                                                                                             'selected': False,
                                                                                             'scrollable': False}}],
                                                                           'name': 'com.android.systemui:id/status_bar_container',
                                                                           'payload': {
                                                                               'resourceId': 'com.android.systemui:id/status_bar_container',
                                                                               'visible': True,
                                                                               'zOrders': {'global': 0, 'local': 1},
                                                                               'package': 'com.android.systemui',
                                                                               'anchorPoint': [0.5, 0.5],
                                                                               'dismissable': False, 'checkable': False,
                                                                               'scale': [1, 1], 'boundsInParent': [1,
                                                                                                                   0.04487179487179487],
                                                                               'focusable': False,
                                                                               'type': 'android.widget.FrameLayout',
                                                                               'touchable': False, 'enabled': True,
                                                                               'longClickable': False,
                                                                               'size': [1, 0.04487179487179487],
                                                                               'pos': [0.5, 0.022222222222222223],
                                                                               'name': 'com.android.systemui:id/status_bar_container',
                                                                               'focused': False, 'checked': False,
                                                                               'editalbe': False, 'selected': False,
                                                                               'scrollable': False}}],
                                                             'name': 'android.widget.FrameLayout',
                                                             'payload': {'visible': True,
                                                                         'zOrders': {'global': 0, 'local': 0},
                                                                         'package': 'com.android.systemui',
                                                                         'anchorPoint': [0.5, 0.5],
                                                                         'dismissable': False, 'checkable': False,
                                                                         'scale': [1, 1],
                                                                         'boundsInParent': [1, 0.10256410256410256],
                                                                         'focusable': False,
                                                                         'type': 'android.widget.FrameLayout',
                                                                         'touchable': False, 'enabled': True,
                                                                         'longClickable': False,
                                                                         'size': [1, 0.10256410256410256],
                                                                         'pos': [0.5, 0.05128205128205128],
                                                                         'name': 'android.widget.FrameLayout',
                                                                         'focused': False, 'checked': False,
                                                                         'editalbe': False, 'selected': False,
                                                                         'scrollable': False}},
                        {'name': 'android.view.View',
                         'payload': {'visible': True, 'zOrders': {'global': 0, 'local': 0}, 'package': 'android',
                                     'anchorPoint': [0.5, 0.5], 'dismissable': False, 'checkable': False,
                                     'scale': [1, 1], 'boundsInParent': [0.044444444444444446, 0.75],
                                     'focusable': False, 'type': 'android.view.View', 'touchable': False,
                                     'enabled': True, 'longClickable': False, 'size': [0.044444444444444446, 0.75],
                                     'pos': [0.9777777777777777, 0.6247863247863248], 'name': 'android.view.View',
                                     'focused': False, 'checked': False, 'editalbe': False, 'selected': False,
                                     'scrollable': False}}, {'name': 'android.view.View', 'payload': {'visible': True,
                                                                                                      'zOrders': {
                                                                                                          'global': 0,
                                                                                                          'local': 0},
                                                                                                      'package': 'android',
                                                                                                      'anchorPoint': [
                                                                                                          0.5, 0.5],
                                                                                                      'dismissable': False,
                                                                                                      'checkable': False,
                                                                                                      'scale': [1, 1],
                                                                                                      'boundsInParent': [
                                                                                                          1,
                                                                                                          0.05128205128205128],
                                                                                                      'focusable': False,
                                                                                                      'type': 'android.view.View',
                                                                                                      'touchable': False,
                                                                                                      'enabled': True,
                                                                                                      'longClickable': False,
                                                                                                      'size': [1,
                                                                                                               0.05128205128205128],
                                                                                                      'pos': [0.5,
                                                                                                              0.9743589743589743],
                                                                                                      'name': 'android.view.View',
                                                                                                      'focused': False,
                                                                                                      'checked': False,
                                                                                                      'editalbe': False,
                                                                                                      'selected': False,
                                                                                                      'scrollable': False}}],
           'name': '<Root>',
           'payload': {'visible': True, 'zOrders': {'global': 0, 'local': 0}, 'size': [0, 0], 'anchorPoint': [0.5, 0.5],
                       'pos': [0, 0], 'name': '<Root>', 'scale': [0, 0], 'type': 'Root'}}



# print(model_a.get('children'))
list_data = model_a.get('children')
list = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0]
w = list_data[0]
# print(w)
y = w.get('children')[0].get('children')[0].get('children')[0].get('children')[0].get('children')[1].get('children')[0].get('children')[0].get('children')[1].get('children')[0]
print(y.get('children')[0])
sku_list= y.get('children')[1].get('children')
for z in sku_list:
    print(z)

