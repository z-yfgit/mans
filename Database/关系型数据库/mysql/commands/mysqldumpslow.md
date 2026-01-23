## mysqldumpslow命令&
说明：MySQL提供的一个用于分析慢查询日志文件的工具

### 用法
```
mysqldumpslow [ OPTS... ] [ LOGS... ]
```

| 选项 | 说明
| --- | ---
| -s ORDER      | 排序方式<br>c：按执行次数排序<br>t：按执行时间排序<br>l：按锁定时间排序<br>r：按行数排序<br>at：按平均时间排序<br>al：按平均锁定时间排序<br>ar：按平均行数排序
| -g PATTERN    | 过滤模式，只显示包含指定字符串的慢SQL
| -t NUM        | 显示前NUM条慢SQL，默认10

### 示例
```sh
# 查看所有慢SQL，按执行次数排序
mysqldumpslow -s c /var/lib/mysql/slow.log

# 按执行时间排序，显示前10条慢SQL
mysqldumpslow -s t -t 10 /var/lib/mysql/slow.log

# 过滤包含keyword的慢SQL
mysqldumpslow -g 'keyword' /var/lib/mysql/slow.log

# 组合用法：按执行时间排序，显示前5条，且包含select的慢SQL
mysqldumpslow -s t -t 5 -g 'select' /var/lib/mysql/slow.log
```
