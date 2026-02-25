## find命令
说明：搜索文件或目录

### 用法

find [-H] [-L] [-P] [-D debugopts] [-Olevel] [path...] [expression]

### expression（表达式）
| 限制 | 说明
| --- | ---
| -maxdepth | 最大查找深度
| -mindepth | 最小查找深度
|       |              |
| 条件 | 说明
| -type     | 指定文件类型。 <br> f：普通文件<br>d：目录<br>b：块设备文件<br>l：符号链接文件<br>s：socket文件<br>c：字符设备文件<br>p：管道文件
| -name     | 按文件名查找
| -iname    | 忽略文件名的大小写
| -empty    | 查找空文件或目录
| -mtime    | 根据文件的modify时间查找，以天为单位。例如：+5表示5天之前，-5 表示5天之内，-100 +50表示查找100天以内50天之前的文件
| -ctime    | 根据文件的change时间查找，以天为单位。例如：+5表示5天之前，-5 表示5天之内，-100 +50表示查找100天以内50天之前的文件
| -atime    | 根据文件的access时间查找，以天为单位。例如：+5表示5天之前，-atime 5表示从上次访问到现在相隔大于5天而小于6天的文件
| -mmin     | 根据文件的modify时间查找，以分钟为单位。例如：+5表示5分钟之前，-5 表示5分钟之内，-100 +50表示查找100分钟以内50分钟之前的文件
| -cmin     | 根据文件的change时间查找，以分钟为单位。例如：+5表示5分钟之前，-5 表示5分钟之内，-100 +50表示查找100分钟以内50分钟之前的文件
| -amin     | 根据文件的access时间查找，以分钟为单位。例如：+5表示5分钟之前，-5 表示5分钟之内，-100 +50表示查找100分钟以内50分钟之前的文件
| -anewer   | 查找比某一个文件新的
| -cnewer   |
| -newer    |
| -newerXY  | XY可以是a、b、c、m、t 。<br> a：access时间<br>b：birth时间<br>c：change时间<br>m：modify时间<br>t：将参考内容理解为时间单位
| -gid      | 指定文件的gid
| -group    | 指定文件的属组
| -nogroup  | 查找没有属组的文件
| -uid      | 指定文件的uid
| -user     | 指定文件的属主
| -nouser   | 查找没有属主的文件
| -size     | 以文件大小为条件，单位可以是bcwkMG，+1G表示大于1G的文件，-10M表示小于10M的文件
|           | 
| -path | 
| -prune |

# 动作类选项
| 动作 | 说明
| --- | ---
| -delete                               | 将查找出来的文件删除
| -exec COMMAND \;-exec COMMAND {} \;   | 查到内容时要执行的命令，每查到一个内容都会执行一遍。{}表示查到的内容


```sh
# 查找修改时间是100天前的
find /home/your-path -mtime +100

# 查找并删除，访问时间是30天前，大小大于500M，类型是文件的，名字是test.log结尾的
find /home/logs -name "*test.log" -type f -size +500M -atime +30 -exec rm {} \;

# 跳过指定目录
find /home -path /home/user1 -prune -o -type f -print

# 跳过多个目录
find /home \( -path /home/user1 -o -path /home/user2 \) -prune -o -type f -print

# 查找修改时间大于2026-02-09 12:34:56.111444777，小于等于2026-01-02 12:35:58.222555888的文件
find -newermt "2026-01-02 12:34:56.111444777" ! -newermt "2026-01-02 12:35:58.222555888"
```
