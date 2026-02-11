## journalctl命令&
说明：查询由systemd服务记录的日志

### 用法	

| 选项 | 说明
| --- | ---
| -x   | 在可能的地方添加消息解释
| -u   | 显示指定unit的日志
| -e   | 直接跳到末尾
| -S   | 显示不超过指定日期的条目<br>-S yesterday: 显示昨天以来的日志<br>-S today: 显示今天以来的日志<br>-S -3h：显示最近3小时的日志
| -U   | 显示不早于指定日期的记录
| -f   | 跟踪日志输入，类似tail -f
| -n   | 指定打印多少行，默认只打印1000行
| -g   | 显示指定字符串的日志，类似grep命令

### 示例

```sh
# 查看network服务的日志
journalctl -xe -u network

# 查看network服务的最后10000行日志，并实时跟踪
journalctl -f -n 10000 -u network

# 查看network服务的今天以来的日志
journalctl -u network -S today
```
