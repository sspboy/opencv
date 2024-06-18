import numpy as np
import cv2

# 读取图片
# 识别图片位置
# 截取图片
# 识别图片文字OCR

def print_hi():
    print(cv2.__version__)


if __name__ == '__main__':

    img = cv2.imread('img/one.jpg', 0)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)

    cv2.imshow('image', img)    # 显示图片

    cv2.waitKey(0)              # 绑定键盘

    cv2.destroyAllWindows()

    cv2.matchTemplate('')