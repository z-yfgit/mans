## git restore命令
说明：恢复工作区文件

### 用法
```
git restore [<options>] [--source=<tree>] [--staged] [--worktree] [--] <pathspec>...
git restore [<options>] [--source=<tree>] [--staged] [--worktree] --pathspec-from-file=<file> [--pathspec-file-nul]
git restore (-p|--patch) [<options>] [--source=<tree>] [--staged] [--worktree] [--] [<pathspec>...]
```

| 选项 | 说明
| --- | ---
| --staged | 恢复暂存区文件
|  | 
|  | 

### 示例
```sh
# 恢复README.md文件的修改
git restore README.md

# 取消暂存README.md文件
git restore --staged README.md

```
