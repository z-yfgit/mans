## ssh命令

```sh
# 将本地端口映射到远程主机。以下示例中，访问本机的7890就相当于访问192.168.1.10的80了
ssh -N -L 7890:192.168.1.10:80 root@192.168.1.10

```


## 常用参数
```sh
StrictHostKeyChecking no
UserKnownHostsFile /dev/null

```


