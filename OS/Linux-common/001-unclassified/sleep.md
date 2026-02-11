## sleep命令&
说明：延迟指定的时间

sleep非常简单，就是延迟指定的时间

### 用法
```
sleep NUMBER[SUFFIX]...

suffix可以是s、m、h、d，分别表示秒、分、时、天
```

### 示例
```sh
# 延迟10秒
sleep 10

# 延迟0.5秒
sleep 0.5

# 延迟10分钟
sleep 10m

# 延迟无穷时间，部分系统支持
sleep infinity
```
