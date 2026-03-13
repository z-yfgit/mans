## ulimit命令

### 用法
```
ulimit [-SHabcdefiklmnpqrstuvxPT] [limit]
```

| 选项 | 说明
| --- | ---
| -S | 软限制
| -H | 硬限制
| -n |
| -u |



### 示例
```sh
# 查看当前用户的单进程最大打开文件数
ulimit -n

# 限制最大内存为100MB（单位：KB，100*1024=102400）
ulimit -v 102400

# 限制最大CPU核心数为1（限制进程只能用1核）
ulimit -u 1
```
