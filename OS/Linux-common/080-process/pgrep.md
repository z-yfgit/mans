## pgrep命令
说明：pgrep命令用于根据进程名称查找进程ID。

### 用法
```
pgrep [options] <pattern>
```

| 选项 | 说明
| --- | ---
| -f | 匹配完整的进程命令行
| -l | 显示进程名称
| -c | 仅显示匹配进程的数量

```sh
# 查找所有nginx主进程
pgrep nginx

# 查找所有nginx工作进程
pgrep -f "nginx: worker process"
```
