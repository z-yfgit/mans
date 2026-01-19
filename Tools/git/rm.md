## git rm命令
说明：从索引中、或者工作树及索引中，移除指定路径的文件。


### 用法
```
git rm [-f | --force] [-n] [-r] [--cached] [--ignore-unmatch]
        [--quiet] [--pathspec-from-file=<file> [--pathspec-file-nul]]
        [--] [<pathspec>...]
```

| 选项 | 说明
| --- | ---
| -f                | --force | 强制删除，忽略文件是否已修改
| --cached          | 仅从索引中取消暂存并删除文件，工作目录中的文件（无论是否已修改）将保持不变
| -n                | --dry-run | 演习，不实际删除文件

### 示例
```sh
git rm hosts

# 从暂存区移除README文件
git rm --cached README
```
