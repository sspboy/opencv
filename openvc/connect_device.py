# 使用 connect_device 来连接任意Android/iOS设备或者Windows窗口。
#
# 使用 模拟操作 的API来自动化你的游戏或者App。
#
# 千万 不要 忘记 声明断言 来验证测试结果。

import time
from airtest.core.api import *

# 链接设备
# 设备uuid
uuid = '88Y5T19929041579'

# 设备链接地址
a_url = "Android:///%s?cap_method=javacap&touch_method=adb" % uuid
b_url = 'Android://127.0.0.1:5037/192.168.101.165:5555'

print(a_url)

# 链接设备
connect_device(a_url)

# 启动应用--对应的包名称
start_app("com.netease.cloudmusic")


# 等待
print('等待10秒...')
time.sleep(3)

# 截图保存到本地
snapshot(filename="./img/test.png", msg="test", quality=10)
time.sleep(3)


# 在屏幕上找到匹配项并返回其坐标
find_all(Template(r"tpl1607511235111.png"))


# 停止应用--对应的包名称(隐藏到)
stop_app("com.netease.cloudmusic")