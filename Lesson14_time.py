# 内建模块 batteries included
# 时间 datatime
from datetime import datetime
print(datetime.now())
dt = datetime(2015, 4, 19, 12,20)
print(dt)

# 把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为epoch time
# 当前时间就是相对于epoch time的秒数，称为timestamp。
t = dt.timestamp()
print(t)
dt = datetime.fromtimestamp(t)
print(dt)
utcdt = datetime.utcfromtimestamp(t)
print(utcdt)

# str to datetime and datetime to str
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# 时间加减
from datetime import timedelta
print(now + timedelta(hours = 10, days = 2))

# 本地时间 转换为 UTC时间
from datetime import timezone
tz_utc_8 = timezone(timedelta(hours = 8))
dt = now.replace(tzinfo = tz_utc_8)
print(dt)

# 时区转换
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
# astimezone()将转换时区为北京时间:
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:
tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp
def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_h = int(re.split(r'[C\:]+', tz_str)[1])
    utc_tz_h = timezone(timedelta(hours = tz_h))
    return dt.replace(tzinfo = utc_tz_h).timestamp()

# 测试:

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')