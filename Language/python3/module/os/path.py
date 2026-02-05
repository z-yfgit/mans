## os.path函数
# 说明：提供了一些用于处理文件路径的函数

# os.path.abspath函数
# 返回一个路径的绝对路径
"""
参数：
    path: 路径字符串

"""


# os.path.dirname函数
# 返回一个路径的目录部分
"""
参数：
    path: 路径字符串

"""


# os.path.basename函数
# 返回一个路径的文件名部分
"""
参数：
    path: 路径字符串

"""

import os

# 获取当前脚本的绝对路径
current_script_path = os.path.abspath(__file__)
print("当前脚本的绝对路径:", current_script_path)

# 获取当前脚本的目录路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))
print("当前脚本所在的目录:", current_script_dir)

# 获取当前脚本的文件名
current_script_name = os.path.basename(current_script_path)
print("当前脚本的文件名:", current_script_name)
