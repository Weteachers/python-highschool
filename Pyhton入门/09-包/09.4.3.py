# datetime常见属性
# datetime.date：提供year, month, day属性
import datetime
dt = datetime.date(2018, 3, 26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)


# datetime.datetime：提供日期跟时间的组合
from datetime import datetime
import time
# 常用类方法：today、now、utcnow、fromtimestamp(从时间戳中返回本地时间)
dt = datetime(2018, 3, 26)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))

# datetime.timedelta：提供一个时间差，时间长度
from datetime import datetime, timedelta
t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))


