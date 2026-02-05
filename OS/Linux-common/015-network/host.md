## host命令
说明：DNS查找工具

### 用法
```
host [-aCdilrTvVw] [-c class] [-N ndots] [-t type] [-W time]
            [-R number] [-m flag] hostname [server]
```
| 选项 | 说明
| --- | ---
| -w | 一直查询直到获得结果
| -W | 指定查询超时时间，单位为秒


```sh
# 使用grep命令仅过滤出来IP
host -W 3 hostname | grep -oP 'address \K\S+'
```
