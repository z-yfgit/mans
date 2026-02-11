## chronyc命令
说明：chrony服务程序的命令行接口

### 用法
```
 chronyc [OPTION]... [COMMAND]...
```

| System clock | 说明
| --- | ---
| tracking      |

| Time sources | 说明
| --- | ---
| sources       | 显示当前时间源相关信息
| sourcestats   |
| selectdata    |

| NTP sources | 说明
| --- | ---
| activity      |
| authdata      |
| ntpdata       |



### 示例
```sh
# 显示时间源
chronyc sources -a -v
```
