## git log命令
说明：显示提交日志

### 用法
| 选项 | 说明
| --- | ---
| --oneline     | 一行显示
| -p            | 显示每次提交的差异
| -N            | 显示最近的N次提交
| --since       | 显示最近多久的提交，等同于 --after
| --until       | 显示指定时间之前的提交，等同于 --before
| --author      | 显示指定作者的提交
| --grep        | 搜索提交说明中的关键字
| --pretty      | 自定义输出格式
| --stat        | 显示每次提交的统计信息
| -S            | 过滤修改内容中包含某个字符串的提交
| --no-merges   | 不显示合并提交

### 示例
```sh
# 每次的提交日志显示在一行内
git log --oneline

# 最近两周的提交日志
git log --since=2.weeks

# 最近7天的提交日志
git log --since=7.days

# 自2026-01-01以来的提交日志
git log --since=2026-01-01

```
