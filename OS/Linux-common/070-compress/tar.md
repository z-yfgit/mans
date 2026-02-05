## tar命令&
说明：文件归档工具

### 用法
```
Traditional usage
    tar {A|c|d|r|t|u|x}[GnSkUWOmpsMBiajJzZhPlRvwo] [ARG...]

UNIX-style usage
    tar -A [OPTIONS] ARCHIVE ARCHIVE

    tar -c [-f ARCHIVE] [OPTIONS] [FILE...]

    tar -d [-f ARCHIVE] [OPTIONS] [FILE...]

    tar -t [-f ARCHIVE] [OPTIONS] [MEMBER...]

    tar -r [-f ARCHIVE] [OPTIONS] [FILE...]

    tar -u [-f ARCHIVE] [OPTIONS] [FILE...]

    tar -x [-f ARCHIVE] [OPTIONS] [MEMBER...]

GNU-style usage
    tar {--catenate|--concatenate} [OPTIONS] ARCHIVE ARCHIVE

    tar --create [--file ARCHIVE] [OPTIONS] [FILE...]

    tar {--diff|--compare} [--file ARCHIVE] [OPTIONS] [FILE...]

    tar --delete [--file ARCHIVE] [OPTIONS] [MEMBER...]

    tar --append [-f ARCHIVE] [OPTIONS] [FILE...]

    tar --list [-f ARCHIVE] [OPTIONS] [MEMBER...]

    tar --test-label [--file ARCHIVE] [OPTIONS] [LABEL...]

    tar --update [--file ARCHIVE] [OPTIONS] [FILE...]

    tar --update [-f ARCHIVE] [OPTIONS] [FILE...]

    tar {--extract|--get} [-f ARCHIVE] [OPTIONS] [MEMBER...]
```


| 操作模式选项 | 说明
| --- | ---
| -c        | 创建一个新的归档
| -t        | 列出归档中的内容
| -d        | 对比归档中的文件与当前系统中的文件是否有差异
| -r        | 添加文件到归档中
| -x        | 从归档中提取文件
| --delete  | 删除归档中的文件

| 压缩选项 | 说明
| --- | ---
| -a                    | 通过归档文件后缀来自动选择压缩程序
| --no-auto-compress    | 与-a选项相反，不自动选择压缩程序
| -z                    | 使用gzip压缩
| -j                    | 使用bzip2压缩
| -J, --xz              | 使用xz压缩
| --lzma                | 使用xz压缩
| --lzip                | 使用lzip压缩
| --lzop                | 使用lzop压缩
| --zstd                | 使用zstd压缩
| -Z                    |

| 本地文件名选项 | 说明
| --- | ---
| -C    | 切换到目录

| 文件属性处理选项 | 说明
| --- | ---
| -m                    | 不要提取文件修改时间
| --owner=OWNER         | 设置提取文件的所有者和组
| --group=GROUP         | 设置提取文件的组
| --mode=MODE | 设置提取文件的权限
| --time=TIME | 设置提取文件的时间
| --no-same-owner | 不保留文件的所有者
| --no-same-permissions | 不保留文件的权限

| 设备选择和切换选项 | 说明
| -f    | 指定归档文件

| 覆盖控制选项 | 说明
| --- | ---
| -k                | 不覆盖已存在的文件
| -K                | 覆盖已存在的文件
| --remove-files    | 文件添加到归档中后，删除原文件

| 信息输出选项 | 说明
| --- | ---
| -v    | 显示详细的操作信息

### 示例
```sh
# 创建归档文件
tar -cf file.tar file1 file2

# 创建归档文件，并根据gz后缀自动选项gzip工具进行压缩
tar -acf file.tar.gz file1 file2

# 列出归档文件内容
tar -tf file.tar.gz

# 添加文件到归档
tar -rf file.tar.gz file3

# 对比归档中的文件与当前系统中的文件是否有差异
tar -df file.tar.gz file3

# 解压缩file.tar.gz文件到dir1目录
tar -xf file.tar.gz -C dir1

# 删除归档文件中的dir1/test.txt文件
tar -f file.tar.gz --delete dir1/test.txt
```
