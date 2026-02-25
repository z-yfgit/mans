## git diff命令
说明：显示提交之间、提交和工作区之间等的差异

### 用法
```
git diff [<options>] [<commit>] [--] [<path>...]
git diff [<options>] --cached [--merge-base] [<commit>] [--] [<path>...]
git diff [<options>] [--merge-base] <commit> [<commit>...] <commit> [--] [<path>...]
git diff [<options>] <commit>...<commit> [--] [<path>...]
git diff [<options>] <blob> <blob>
git diff [<options>] --no-index [--] <path> <path>
```

### 示例
```sh
# 显示当前工作区与暂存区的差异
git diff

# 显示暂存区与上一个提交的差异
git diff --cached
```
