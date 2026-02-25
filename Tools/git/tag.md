## git tag命令
说明：创建、列出、删除或验证一个使用 GPG 签名的标签对象

### 用法
```
git tag [-a | -s | -u <keyid>] [-f] [-m <msg> | -F <file>] [-e] <tagname> [<commit> | <object>]
git tag -d <tagname>...
git tag [-n[<num>]] -l [--contains <commit>] [--no-contains <commit>]
git tag -v [--format=<format>] <tagname>...
        [--points-at <object>] [--column[=<options>] | --no-column]
        [--create-reflog] [--sort=<key>] [--format=<format>]
        [--merged <commit>] [--no-merged <commit>] [<pattern>...]
```

| 选项 | 说明
| --- | ---
| -l        | 列出所有标签
| -d        | 删除标签
|  | 

### 示例
```sh
# 查看所有标签
git tag

# 查看符合模式的标签
git tag -l "v1.8.5*"

# 删除标签v1.8.3
git tag -d v1.8.3

```

