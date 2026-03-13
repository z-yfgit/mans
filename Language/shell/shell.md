# shell语法

## 比较符
| 比较符 | 说明
| --- | ---
| -eq | 等于（equal）
| -ne | 不等于（not equal）
| -gt | 大于（greater than）
| -lt | 小于（less than）
| -ge | 大于或等于（greater than or equal）
| -le | 小于或等于（less than or equal）

## 测试操作符
| 测试操作符 | 说明
| --- | ---
| -z | 字符串长度为0（empty）
| -n | 字符串长度不为0（not empty）
| -f | 文件存在（file exists）
| -d | 目录存在（directory exists）
| -e | 文件或目录存在（file or directory exists）
| -s | 文件大小不为0（file size is not zero）
| -r | 文件可读（file is readable）
| -w | 文件可写（file is writable）
| -x | 文件可执行（file is executable）


## case判断
```sh
case VAR in
    mode1)
        commands
    ;;

    mode2)
        commands
    ;;

    *)
        commands
esac
```

## if判断

```sh
# 文件存在返回True
if [ -f ${FILE} ]; then
    echo ${FILE} exist
fi

# 大于返回True
if [ 1 -gt 0 ]; then
    echo ok
fi

```

