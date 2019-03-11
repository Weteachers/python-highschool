import calendar
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
cal = calendar.calendar(2019)
print(type(cal))
print(cal)

print("*" * 20)

cal = calendar.calendar(2018, l=0, c=15)
print(cal)

# isleap: 判断某一年是否闰年
print(calendar.isleap(2000))

# leapdays: 获取指定年份之间的闰年的个数
print(calendar.leapdays(2001, 2019))

# 获取某个月的日历字符串
# 格式：calendar.month(年，月)
# 返回值：月日历的字符串
m2 = calendar.month(2018, 3)
print(m2)

# monthrange()
# 格式：calendar.monthrange(年, 月)
# 返回值：元组(周几开始,总天数)
# 注意：周默认 0-6 表示周一到周天
w,t = calendar.monthrange(2017, 3)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 返回值：二级列表
# 注意：矩阵中没有天数  用 0 表示
m = calendar.monthcalendar(2019,2)
print(type(m))
print(m)

# prcal() 直接打印日历
calendar.prcal(2018)
# help(calendar.prcal)

# prmonth() 直接打印整个月的日历
# 格式：calendar.prmonth(年，月)
# 返回值：无
calendar.prmonth(2018, 3)

# weekday() 获取周几
# 格式：calendar.weekday(年，月，日)
# 返回值：周几对应的数字
calendar.weekday(2018, 3, 22)


