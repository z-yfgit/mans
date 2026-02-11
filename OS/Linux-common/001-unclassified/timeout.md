## timeout命令&
说明: 运行一个命令, 并在指定时间后终止它

### 用法
```
timeout [OPTION] DURATION COMMAND [ARG]...
timeout [OPTION]
```


### 示例
```sh
# 运行sleep 10秒, 在5秒后终止
timeout 5s sleep 10
```
