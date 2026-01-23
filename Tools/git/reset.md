## git reset命令
说明：将当前 HEAD 重置为指定状态

### 用法
```
git reset [-q] [<tree-ish>] [--] <pathspec>...
git reset [-q] [--pathspec-from-file=<file> [--pathspec-file-nul]] [<tree-ish>]
git reset (--patch | -p) [<tree-ish>] [--] [<pathspec>...]
git reset [--soft | --mixed [-N] | --hard | --merge | --keep] [-q] [<commit>]
```

| 选项 | 说明
| --- | ---
| --soft    |
| --mixed   |
| --hard    |

### 示例
```sh
git reset HEAD^

# 撤销对CONTRIBUTING.md文件的暂存
git reset HEAD CONTRIBUTING.md

# 回滚到某一次提交，此次提交之后的修改会被退回到暂存区
git reset --soft <commit_id>

# 回滚到某一次提交，此次提交之后的修改不会有任何保留，用git status查看是没有记录的。
git reset --hard <commit_id>
```
