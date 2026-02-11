## base64命令&
说明：base64编码和解码工具

### 用法
```
base64 [OPTION]... [FILE]
```
| 选项 | 说明
| --- | ---
| -d | 对base64编码进行解码

### 示例
```sh
# 对字符串hello world进行base64编码
echo "hello world" | base64   # 输出：aGVsbG8gd29ybGQK

# 对test.txt文件进行base64编码
base64 test.txt > test.txt.base64

# 对test.txt文件进行base64解码
base64 -d test.txt.base64
```
