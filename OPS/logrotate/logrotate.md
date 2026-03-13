## logrotate命令
说明：日志轮转工具

### 用法
```
logrotate  [--force]  [--debug]  [--state  file] [--skip-state-lock] [--verbose] 
    [--log file] [--mail command] config_file [config_file2 ...]
``` 




### 示例
```sh
# 强制轮转
logrotate -f /etc/logrotate.d/xxx
```
