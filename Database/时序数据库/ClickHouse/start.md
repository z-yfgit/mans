## clickhouse start命令
说明：启动clickhouse

### 用法
```
Usage: clickhouse start
  -h [ --help ]                         produce help message
  --prefix arg (=/)                     prefix for all paths
  --binary-path arg (=usr/bin)          directory with binary
  --config-path arg (=etc/clickhouse-server)
                                        directory with configs
  --pid-path arg (=var/run/clickhouse-server)
                                        directory for pid file
  --user arg (=clickhouse)              clickhouse user
  --max-tries arg (=60)                 Max number of tries for waiting the 
                                        server (with 1 second delay)
```

| 选项 | 说明
| --- | ---
| --config-path | 指定配置目录

### 示例
```sh
# 直接启动clickhouse
clickhouse start

# 使用指定配置目录启动clickhouse
clickhouse start --config-path /apps/clickhouse/clickhouse-server
```
