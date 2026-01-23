## ssh-copy-id命令&
说明：将本地公钥复制到远程主机的authorized_keys文件中

### 用法
```
/usr/bin/ssh-copy-id [-h|-?|-f|-n|-s] [-i [identity_file]] [-p port] [-F alternative ssh_config file] [[-o <ssh -o options>] ...] [user@]hostname
```

| 选项 | 说明
| --- | ---
| -p | 端口号
| -i | 身份文件
| -o | ssh选项
| -f | 强制覆盖
| -n | 不执行实际操作

### 示例
```sh
# 将本地公钥复制到远程主机
ssh-copy-id -i ~/.ssh/id_rsa.pub -p 2222 user@192.168.1.100
```

