## less命令
说明：比more更好用的分页显示文件内容工具


### 用法
```
less -?
less --help
less -V
less --version
less [-[+]aABcCdeEfFgGiIJKLmMnNqQrRsSuUVwWX~]
     [-b space] [-h lines] [-j line] [-k keyfile]
     [-{oO} logfile] [-p pattern] [-P prompt] [-t tag]
     [-T tagsfile] [-x tab,...] [-y lines] [-[z] lines]
     [-# shift] [+[+]cmd] [--] [filename]...
```

| 选项 | 说明
| --- | ---
| -i | 忽略大小写
| -N | 显示行号
| -S | 不换行显示
| +G | 打开时直接跳转到文件末尾


### 常用按键
| 按键 | 说明
| --- | ---
| q  :q  Q  :Q  ZZ  | 退出less
| h  H              | 显示帮助信息
| f  空格           | 向下滚动一屏
| b                 | 向上滚动一屏
| ↓                 | 向下滚动一行
| ↑                 | 向上滚动一行
| N→                | 向右移动N个字符。之后只按箭头即可
| N←                | 向左移动N个字符。之后只按箭头即可
| d                 | 向下滚动半屏
| u                 | 向上滚动半屏
| n                 | 搜索下一个匹配项
| N                 | 搜索上一个匹配项
| 20g               | 跳转到第20行
| 10                | 往下滚动10行
| /pattern          | 搜索pattern字符串，从当前位置向下搜索
| ?pattern          | 搜索pattern字符串，从当前位置向上搜索
| &pattern          | 仅显示匹配的行
| ESC-U             | 清除搜索高亮
| g  <              | 跳转到文件开头
| G  >              | 跳转到文件末尾
| =                 | 显示当前文件名、位置等信息
| ma                | 标记当前页面的第一行位置为a
| Mb                | 标记当前页面的最后一行位置为b
| 'a                | 跳转到标记a处
| ESC-Mb            | 取消标记b
| ''                | 回到上一个位置
| r                 | 刷新当前页面（有时候翻来翻去会有空行不显示，r可以刷新恢复）
| R                 | 重新加载当前文件


### 交互模式用的用法
```sh
# 仅显示匹配的行
&pattern

# 仅显示不匹配的行
&!pattern

# 按m设置标记。将当前位置标记为a
ma

# 按单引号跳转到指定标记，跳转到a标记处
'a
```
