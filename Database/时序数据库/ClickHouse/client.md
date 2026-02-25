## ch client命令
说明：clickhouse客户端

在部分环境，执行chc会等同于执行clickhouse client命令。

### 用法
```
clickhouse client [args]
```

| 选项 | 说明
| --- | ---
| -u                | 用户名，默认default
| --password        | 密码，默认空
| --ask-password    | 提示输入密码
| -h                | 服务器地址，默认localhost
| --port            | 端口，默认9000
| -d                | 指定数据库
| -q                | 查询语句

### 示例
```sh
# 非交互式模式执行查询语句
ch client --ask-password -d system -q "show tables;"

```
