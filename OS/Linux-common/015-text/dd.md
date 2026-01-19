## dd命令
说明：用于复制文件或设备的工具

### 示例
```sh
# 从/dev/zero往./testfile1写内容，块大小为1024字节，写1000个块
dd if=/dev/zero of=./testfile1 count=1000 bs=1024


# 结合tail命令，查看一个或多个文件的增长速度
tail -f file01 file02 | dd of=/dev/null status=progress
```