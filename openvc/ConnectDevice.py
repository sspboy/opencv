# 使用 connect_device 来连接任意Android/iOS设备或者Windows窗口。
# 使用 模拟操作 的API来自动化你的游戏或者App。
# 千万 不要 忘记 声明断言 来验证测试结果。

import time,json
from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class Operationphoto():
    def __init__(self, uuid):
        self.uuid = uuid
        pass

    def connectdevice(self): # 链接指定设备
        a_url = "Android:///%s?cap_method=javacap&touch_method=adb" % self.uuid
        connect_device(a_url)
        res = start_app("com.xunmeng.pinduoduo")
        # res = start_app("com.netease.cloudmusic")
        return res

    def fun_name(self): # 设备截图
        pass


if __name__ == '__main__':

    uuid = '88Y5T19929041579'

    op = Operationphoto(uuid)

    res = op.connectdevice()

    print(res)

    # 等待
    sleep(5)

    # 点击 搜索框==>>进入搜索页面
    poco.click([0.4, 0.07])

    # 判断是否弹出框例如《百亿补贴》《其它弹出框》
    # 定位到搜索输入框，点击》》进入搜索页面
    sleep(2)

    # 点击 搜索框==>>点击一个链接到详情页面
    res = poco.click([0.225, 0.191])
    sleep(2)

    # 点击右下角 弹出SKU
    poco.click([0.75, 0.96])
    sleep(3)

    # 相对定位控件
    res = poco(name="com.xunmeng.pinduoduo:id/pdd", type="android.support.v7.widget.RecyclerView")

    print(res)


    # 定位到sku控件
    # 通过控件获取sku名称
    # frozen_poco = poco.freeze()
    # hierarchy_dict = frozen_poco.agent.hierarchy.dump()
    # print(dict(hierarchy_dict))





# 链接设备
# 设备uuid

# 设备链接地址
# a_url = "Android:///%s?cap_method=javacap&touch_method=adb" % uuid
# b_url = 'Android://127.0.0.1:5037/192.168.101.165:5555'

# print(a_url)

# 链接设备
# connect_device(a_url)

# 启动应用--对应的包名称
# start_app("com.netease.cloudmusic")


# 等待
# print('等待10秒...')
# time.sleep(3)

# 截图保存到本地
# snapshot(filename="./img/test.png", msg="test", quality=10)
# time.sleep(3)


# 在屏幕上找到匹配项并返回其坐标
# find_all(Template(r"tpl1607511235111.png"))


# 停止应用--对应的包名称(隐藏到)
# stop_app("com.netease.cloudmusic")