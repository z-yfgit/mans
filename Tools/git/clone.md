## git clone命令
说明：克隆仓库到一个新的目录

为已克隆存储库中的每个分支创建远程跟踪分支(使用`git branch --remotes`可见)，并创建并签出从已克隆存储库的当前活动分支派生的初始分支。

### 用法

```
git clone [--template=<template_directory>]
                 [-l] [-s] [--no-hardlinks] [-q] [-n] [--bare] [--mirror]
                 [-o <name>] [-b <name>] [-u <upload-pack>] [--reference <repository>]
                 [--dissociate] [--separate-git-dir <git dir>]
                 [--depth <depth>] [--[no-]single-branch] [--no-tags]
                 [--recurse-submodules[=<pathspec>]] [--[no-]shallow-submodules]
                 [--[no-]remote-submodules] [--jobs <n>] [--sparse] [--[no-]reject-shallow]
                 [--filter=<filter>] [--] <repository>
                 [<directory>]

<repository>
    远程仓库URL地址

[<directory>]
    指定一个空目录为克隆位置，默认克隆到当前目录
```

| 选项 | 说明
| ---- | ---
| -v   | 更详细的输出
| -q   | 更安静的输出
| -b   | 克隆指定分支
| -l   | 从本地存储库克隆
| -s   | 设置为共享存储库

### 示例

```sh
# 克隆https仓库
git clone https://github.com/engild/mans.git

# 克隆指定分支
git clone -b branch_name https://github.com/engild/mans.git

# 使用指定ssh私钥文件克隆仓库
git clone git@github.com:xxx/yyy.git --config core.sshcommand="ssh -i ~/.ssh/id_rsa2"
```
