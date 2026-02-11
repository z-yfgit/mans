## dpkg命令
说明：Debian的包管理工具

### 示例

```sh
# 查看软件包的状态
dpkg -l policykit-1

# 查看所有软件包的状态
dpkg -l

# 查找软件包所属的文件，可以知道软件包安装在哪些文件中，命令是由哪个软件包安装的
dpkg -S iotop
```
