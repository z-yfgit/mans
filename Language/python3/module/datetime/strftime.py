import datetime
# from datetime import datetime, timedelta
yerstoday = datetime.datetime.now()

print(yerstoday)

# 格式化输出
format_str = yerstoday.strftime("%Y%m%d")
print(format_str)