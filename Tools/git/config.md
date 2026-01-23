## git config命令
说明：

### 用法
```
git config [<file-option>] [--type=<type>] [--fixed-value] [--show-origin] [--show-scope] [-z|--null] name [value [value-pattern]]
git config [<file-option>] [--type=<type>] --add name value
git config [<file-option>] [--type=<type>] [--fixed-value] --replace-all name value [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get name [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] --get-all name [value-pattern]
git config [<file-option>] [--type=<type>] [--show-origin] [--show-scope] [-z|--null] [--fixed-value] [--name-only] --get-regexp name_regex [value-pattern]
git config [<file-option>] [--type=<type>] [-z|--null] --get-urlmatch name URL
git config [<file-option>] [--fixed-value] --unset name [value-pattern]
git config [<file-option>] [--fixed-value] --unset-all name [value-pattern]
git config [<file-option>] --rename-section old_name new_name
git config [<file-option>] --remove-section name
git config [<file-option>] [--show-origin] [--show-scope] [-z|--null] [--name-only] -l | --list
git config [<file-option>] --get-color name [default]
git config [<file-option>] --get-colorbool name [stdout-is-tty]
git config [<file-option>] -e | --edit

```

在新版本中，--get、--rename-section、--remove-section、--list等选项已被弃用，取而代之的是子命令。
```sh
# 获取指定配置
git config --get name   # 旧方法
git config get name     # 新方法


# 列出配置
git config -l           # 旧方法
git config list         # 新方法
```



### 示例
```sh
# 设置全局配置
git config --global user.name "John Doe"

# 查看配置
git config -l

# 查看指定配置
git config user.name

# 通过正则表达式查看配置项
git config --get-regexp "user\."

# 取消指定全局配置
git config --global --unset user.name

# 交互式编辑全局配置
git config -e --global

# 删除指定section
git config --remove-section sec_name
```



### 配置项大全

| 配置项 | 说明
| --- | ---
| user.name         | 用户名
| user.email        | 用户邮箱
| core.editor       | 编辑器
| core.sshCommand   | 
| author.name       | 作者名
| author.email      | 作者邮箱
| committer.name    | 提交人名
| committer.email   | 提交人邮箱
