## cat命令&
说明：连接文件并在标准输出上打印

### 用法
```
cat [OPTION]... [FILE]...
```

| 选项 | 说明
| --- | ---
| -n    | 输出时显示行号
| -E    | 显示行结束符为$
| -e    | 等同于 -vE
| -v    | 显示不可打印字符
| -s    | 压缩多个空行
| -b    | 输出时显示非空行号

### 示例
```sh
# 显示/etc/hosts文件的内容并显示行号
cat -n /etc/hosts

# 直接将文本追加到文件中。如果是覆盖，cat后面写一个>
cat >> /tmp/yourfile << EOF
Your content
EOF

# 提权追加文本
sudo bash -c "cat >> /etc/hosts" << EOF
Your content
EOF
```
