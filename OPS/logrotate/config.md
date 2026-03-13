## 配置项说明

### 轮转
| rotate count      | 最多保留指定数量的备份
| olddir directory  | 日志会被移动到指定的目录中进行轮转。该目录必须与正在轮转的日志文件位于同一物理设备上，除非使用了copy, copytruncate 或 renamecopy选项。
| su user group     | 切换到指定用户和组进行日志轮转

### 切割频率
| 选项 | 说明
| --- | ---
| size SIZE | 文件大小超过 SIZE 时轮转
| hourly    | 每小时轮转一次
| daily     | 每天都会轮转
| weekly    | 每周轮转一次
| monthly   | 在一个月内首次运行 logrotate 时（通常是在每月的第一天），日志文件会进行轮转。
| yearly    | 在一年内首次运行 logrotate 时（通常是在每月的第一天），日志文件会进行轮转。

### 邮件通知
| nomail                        | 不发送邮件通知
| mail recipient@example.org    | 发送邮件通知

### 压缩
| nocompress    | 不压缩备份文件
| compress      | 压缩备份文件

| copytruncate | 复制并截断原始日志文件
| nocreate | 不创建新的日志文件
| missingok | 忽略缺失的日志文件
| notifempty | 不轮转空文件
