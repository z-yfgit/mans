## xargs命令
说明：将标准输入中读取数据作为参数传递给指定的命令

### 用法
```
xargs [OPTION]... COMMAND [INITIAL-ARGS]...
```

| 选项 | 说明
| --- | ---
| -r | 当标准输入为空时，不执行命令。批量删除 / 复制文件时必加，安全兜底
| -i | 用{}替换输入内容（自定义参数位置）
| -I | 等同于 -i
| -d | 指定分隔符，默认是空格
| -t | 执行前打印完整命令，调试用
| -p | 确认执行每个命令前，打印完整命令
| -n |


### 示例
```sh
# 批量复制文件到备份目录，此时如果不加-i，最终会变成cp test2.txt test2.txt
touch test.txt
ls test.txt | xargs -t -i cp {} test2.txt

# 输入是「dir1,dir2,dir3」，按逗号分割后传给mkdir
echo "dir1,dir2,dir3" | xargs -d ',' -r mkdir -p
```
