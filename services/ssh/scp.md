## scp命令
说明：使用openSSH协议进行文件传输

### 用法
```
scp [-346ABCOpqRrsTv] [-c cipher] [-D sftp_server_path] [-F ssh_config] 
    [-i identity_file] [-J destination] [-l limit] [-o ssh_option] [-P port] 
    [-S program] source ... target
```

| 选项 | 说明
| --- | ---
| -r    | 递归复制目录
| -P    | 指定端口号

### 示例
```sh
# 复制本地目录到远程服务器
scp -r /path/to/local/dir root@192.168.30.20:/root/

```
