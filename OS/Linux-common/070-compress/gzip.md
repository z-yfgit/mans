## gzip命令&
说明：压缩或解压缩gzip文件

gzip一般是用来压缩文件的，而不是目录，要压缩目录，需要使用tar命令先打包，然后再压缩。

### 用法
```
gzip [OPTION]... [FILE]..
```

gzip会自动给文件添加.gz后缀

| 选项 | 说明
| --- | ---
| -d    | 解压缩文件。这与使用gunzip命令相同
| -k    | 不删除源文件。部分版本没有这个选项
| -r    | 递归压缩目录下的所有文件
| -t    | 测试压缩文件是否完整
| -num  | 调整压缩速度。-1表示最快压缩方法（低压缩比），-9表示最慢压缩方法（高压缩比）。默认值为6

### 示例
```sh
# 压缩filename，并保留源文件，用级别5压缩
gzip -k -5 filename

# 压缩目录dir下的所有文件，并保留源文件
gzip -k dir   # 如果dir下有file1、file2文件，会在dir目录创建file1.gz、file2.gz压缩文件

# 测试压缩文件filename.gz是否完整
gzip -t filename.gz

# 解压缩filename.gz文件，并保留源文件
gzip -k -d filename.gz
```
