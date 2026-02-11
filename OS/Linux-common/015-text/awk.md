## awk命令
说明：模式扫描和处理工具

linux三剑客之一，用于文本处理、数据提取、数据转换等。

### 用法
```
awk [ POSIX or GNU style options ] -f program-file [ -- ] file ...

awk [ POSIX or GNU style options ] [ -- ] program-text file ...
```

| 选项 | 说明
| --- | ---
| -F            | 指定分隔符（默认空格）。例如：-F ';' 、 -F '[-:]'可以同时指定多个分隔符
| -v var=value  | 设置变量，方便在awk脚本时使用。例如：-v user=root -v pw=123456

### awk变量

### awk预定义变量
| 变量 | 说明
| --- | ---
| $N  | 当前行的第N个字段，比如n为1表示第一个字段
| $0  | 执行过程中当前行的文本内容
| NF  |

FILENAME  当前输入文件的名

FS  字段分隔符（默认是任何空格）

NR  表示记录数，在执行过程中对应于当前的行号

FNR  各文件分别计数的行号

###  分隔符示例
```sh
# 默认以空格分隔，打印第2列
awk '{print $2}'

# 指定冒号为分隔符
awk -F: '{print $2}'

# 同时指定多个分隔符
awk -F"[:/]" '{print $2}'
awk -F"[][]" '{print $2}'   # 如果分隔符是方括号，必须这么写，不能写-F'[[]]'

# 覆盖预定变量，以单词做分隔符
awk -v FS='time' '{print $2}'
```


### 示例（运算）
```sh

```

### 筛选打印
```sh
# 打印第2列，且第5列包含keywork的行
awk '$5~"keywork"{ print $2 }'

# 打印第2列，且第5列不包含keywork的行
awk '$5!~"keywork"{ print $2 }'

# 打印第2列，且第5列等于keywork的行
awk '$5=="keywork"{ print $2 }'

# 打印第2列，且第5列不等于keywork的行
awk '$5!="keywork"{ print $2 }'

# 过滤某一列的数字大于10的行
awk -F ':'  '$2>100{print $0}'
```


### 其他示例
```sh
# 打印最后一列
awk '{print $NF}'

# 打印倒数第二列。
awk '{print $(NF-1)}'

# 调用外部变量，或者调用其他命令的执行结果
export VAR_NAME=aa ; echo | awk -v VAR="$VAR_NAME" '{print VAR}'
echo | awk -v VAR=$(echo 123) '{print VAR}'

# awk执行系统命令，注意双引号的位置！
awk '{system("echo "$1" "$2"; echo "$3" "$4)}'

# 下面是一个批量修改镜像的标签，并推送到指定镜像仓库的自动化脚本示例
export SRC_REPO=example.com/reponame/
export DEST_REPO=1.2.3.4:5000/reponame/
docker images | grep "$SRC_REPO" | tr / ' ' | awk '{system("echo docker tag "$5" ${DEST_REPO}"$3":"$4" ;echo docker push ${DEST_REPO}"$3":"$4)}'
```
