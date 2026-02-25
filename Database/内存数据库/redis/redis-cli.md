## redis-cli命令
说明：连接和操作Redis数据库

### 用法
```
redis-cli [OPTIONS] [cmd [arg [arg ...]]]
```

| 选项 | 说明
| --- | ---
| --scan        | 使用SCAN命令列出所有keys
| --pattern     | 指定扫描模式，与--scan一起使用



### 示例
```sh
redis-cli -h 127.0.0.1 -p 8479
```
