## time.strftime函数

import time

"""
%Y	4 位年份	            2026
%m	2 位月份（补 0）	     02
%d	2 位日期（补 0）	     05
%H	24 小时制小时（补 0） 	 10
%I	12 小时制小时（补 0）	 10
%M	分钟（补 0）	         00
%S	秒（补 0）	             00
%a	星期缩写	             Thu
%A	星期全称	             Thursday
"""

timestamp = time.time() * 1000000
# print(timestamp)
# timestamp = 1770281548
print(time.localtime(timestamp))
# 1. 直接格式化时间戳（localtime转本地时间，gmtime转UTC时间）
# format_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
format_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
# print(f"time模块格式化结果：{format_str}")  # 输出：2026-02-05 10:00:00