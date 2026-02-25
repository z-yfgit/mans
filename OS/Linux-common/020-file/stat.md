## stat命令
说明：显示文件或文件系统的状态信息

### 用法
```
stat [OPTION]... FILE...
```
| 选项 | 说明
| --- | ---
| -c    | 格式化输出
| -L    | 如果是符号链接，显示链接目标的状态信息

| 文件格式化 | 说明
| --- | ---
| %a    | permission bits in octal (note '#' and '0' printf flags)
| %A    | 文件权限
| %b    | number of blocks allocated (see %B)
| %B    | the size in bytes of each block reported by %b
| %C    | SELinux security context string
| %d    | device number in decimal
| %D    | device number in hex
| %f    | raw mode in hex
| %F    | 文件类型
| %g    | 文件所属组ID
| %G    | 文件所属组
| %h    | number of hard links
| %i    | inode号
| %m    | 挂载点
| %n    | 文件名
| %N    | quoted file name with dereference if symbolic link
| %o    | optimal I/O transfer size hint
| %s    | 文件大小，单位为字节
| %t    | major device type in hex, for character/block device special files
| %T    | minor device type in hex, for character/block device special files
| %u    | 文件所有者ID
| %U    | 文件所有者
| %w    | time of file birth, human-readable; - if unknown
| %W    | time of file birth, seconds since Epoch; 0 if unknown
| %x    | time of last access, human-readable
| %X    | time of last access, seconds since Epoch
| %y    | time of last data modification, human-readable
| %Y    | time of last data modification, seconds since Epoch
| %z    | time of last status change, human-readable
| %Z    | time of last status change, seconds since Epoch

| 文件系统格式化 | 说明
| --- | ---
| %a    | free blocks available to non-superuser
| %b    | total data blocks in file system
| %c    | total file nodes in file system
| %d    | free file nodes in file system
| %f    | free blocks in file system
| %i    | file system ID in hex
| %l    | maximum length of filenames
| %n    | file name
| %s    | block size (for faster transfers)
| %S    | fundamental block size (for block counts)
| %t    | file system type in hex
| %T    | file system type in human readable form

### 示例
```sh
# 显示文件权限、所有者、所属组和文件名
stat -c "%A %U %G %n" filename

# 显示符号链接的目标状态信息，而不是符号链接本身
stat /usr/bin/python3 -L
```
