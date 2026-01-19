## lsof命令
说明：列出打开的文件


### 示例
```sh
# 查看filename被哪些进程打开了
lsof filename

# 查看使用了22端口的进程
lsof -i:22

# 查看进程6382打开了哪些文件
lsof -p 6382

# 查看哪些文件被删除了，但是有进程还在打开，空间没有被释放
lsof | grep -i delete
```
