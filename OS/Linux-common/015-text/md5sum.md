## md5sum命令&
说明：计算MD5校验和

### 用法
```
md5sum [OPTION]... [FILE]...
```
| 选项 | 说明
| --- | ---
| -c | 从文件中读取校验和并校验文件是否正确

### 示例
```sh
# 计算test.txt文件的MD5校验和
md5sum test.txt

# 计算字符串123456789的MD5校验和
echo 123456789 | md5sum

# 为多个文件生成校验文件
md5sum file1.jpg file2.zip > all_files.md5

# 校验文件是否被修改
md5sum -c all_files.md5
```
