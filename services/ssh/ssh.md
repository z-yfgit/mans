## ssh命令
说明：SSH客户端，用于登录远程主机

### 用法
```
ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
    [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
    [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
    [-i identity_file] [-J [user@]host[:port]] [-L address]
    [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
    [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
    [-w local_tun[:remote_tun]] destination [command [argument ...]]
```
| 选项 | 说明
| --- | ---
| -p | 指定SSH连接的端口号，默认值为22
| -o | 指定SSH连接的选项，格式为`-o option=value`
| -T    | 禁用伪终端分配，用于执行远程命令而不登录交互式shell

### 示例
```sh
# 将本地端口映射到远程主机。以下示例中，访问本机的7890就相当于访问192.168.1.10的80了
ssh -N -L 7890:192.168.1.10:80 root@192.168.1.10

# 测试使用 ssh 连接 git 仓库
ssh -T git@github.com
```


### 常用参数
```sh
StrictHostKeyChecking no
UserKnownHostsFile /dev/null

```
