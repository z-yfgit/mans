## unzip命令&
说明：列出、测试、提取zip压缩文件

### 用法
```
unzip [-Z] [-cflptTuvz[abjnoqsCDKLMUVWX$/:^]] file[.zip] [file(s) ...]  [-x xfile(s) ...] [-d exdir]
```

| 选项 | 说明
| --- | ---
| -l | 列出压缩文件中的文件列表，不提取文件
| -t | 测试压缩文件是否损坏
| -x | 排除指定文件或目录不提取，多个文件或目录用空格分隔
| -d | 指定解压到哪个目录，默认会提取到当前目录
| -n | 不覆盖已存在的文件

### 示例
```sh
# 列出test.zip文件中的文件列表
unzip -l test.zip

# 提取test.zip文件中的nginx.conf文件
unzip test.zip nginx.conf

# 测试test.zip文件是否损坏
unzip -t test.zip

# 提取test.zip文件到/path/to/dir目录，排除所有.cache文件
unzip test.zip -d /path/to/dir -x *.cache
```
