## crontab命令

### 用法
```
crontab [ -u user ] file
crontab [ -u user ] [ -i ] { -e | -l | -r }
```

### 选项
| 选项 | 说明
| --- | ---
| -u USER   | 指定要操作的用户，缺省为当前用户
| -l        | 显示当前用户计划任务
| -e        | 编辑计划任务
| -i        | 使用-r选项时，会向用户确认是否移除
| -r        | 移除计划任务，慎用

### 示例
```sh
# 编辑test用户的定时任务
crontab -eu test

# 排除包含cron内容中包含delete_cron的任务，再应用到cron在，简单说，该方法可以删除包含delete_cron的任务
crontab -l | grep -v delete_cron | crontab

# 新增一个定时任务，每分钟执行一次echo 'hello world'
# echo "* * * * * echo 'hello world'" | crontab -
```

### 定时任务示例
```

```
