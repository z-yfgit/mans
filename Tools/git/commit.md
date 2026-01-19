## git commit命令
说明：记录变更到仓库

### 用法
```
git commit [options] [--] <pathspec>...

| 选项 | 说明 |
| --- | --- |
| -q        |
| -v        |
| -m <msg>  | 使用给出的<msg>作为提交消息。如果给出多个-m选项，它们的值将作为单独的段落连接起来。-m选项与-c、-C和-F相互排斥
| -a        | 提交所有更改的文件
| -i        | 提交指定的文件到索引中
| -o        | 只提交指定文件
| --amend   | 修正最近一次提交
| --no-edit | 不启动编辑器
```

### 示例
```sh
# 提交
git commit -m "提交说明"

# 将所有修改的文件提交
git commit -am "提交说明"

# 上一次提交说明有误，修改提交说明
git commit --amend -m "更新后的提交说明"

# 添加漏暂存的文件，并修正最近一次的提交
git add forgotten_file
git commit --amend --no-edit
```