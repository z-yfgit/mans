## timedatectl命令&
说明：查询或更改系统的时间和日期

### 用法
```
timedatectl [OPTIONS...] COMMAND ...
```

| 子命令 | 说明
| --- | ---
| status            | 显示当前时间设置
| set-time          | 设置系统时间。当ntp是禁用时才可以修改时间
| set-timezone      | 设置系统时区
| list-timezones    | 列出所有可用时区
| set-ntp           | 启用或禁用NTP时间同步


| 选项 | 说明
| --- | ---
| -H --host=[USER@]HOST     | 操作远程主机
| -M --machine=CONTAINER    | 操作本地容器

### 示例
```sh
# 显示当前时间设置
timedatectl status

# 启用NTP时间同步
timedatectl set-ntp on   # yes true都可以

# 禁用NTP时间同步
timedatectl set-ntp no   # off false都可以

# 设置系统时间为2023-01-01 12:00:00
timedatectl set-time "2023-01-01 12:00:00"
```
