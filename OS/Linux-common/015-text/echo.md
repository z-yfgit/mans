## echo命令&
说明：输出字符串到标准输出

### 用法
```
echo [OPTION]... [STRING]...
```

| 选项 | 说明
| --- | ---
| -n    | 不输出末尾的换行符
| -e    | 开启转义字符解释

### 示例
```sh
# 输出字符串到标准输出
echo "hello world"

# 不输出末尾的换行符
echo -n "hello world"

# 开启转义字符解释
echo -e "hello\nworld"
```
