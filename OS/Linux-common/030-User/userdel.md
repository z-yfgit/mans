## userdel命令&
说明: 删除用户

### 用法
```
userdel [options] USER
```

| 选项 | 说明
| --- | ---
| -r   | 同时删除家目录和邮件（`/var/spool/mail/LOGIN`）文件。

### 示例
```sh
# 删除testuser用户，同时删除家目录和邮件文件
userdel -r test_user
```
