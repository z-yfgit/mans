## time.time函数&
# 说明：返回当前时间的时间戳

"""
参数：
    无

"""

import time

current_time = time.time()
# 获取当前时间的时间戳，单位为秒
print(current_time)

# 转换为毫秒
print(f"当前时间的时间戳（毫秒）：{current_time * 1000:.0f}")
