## ip命令
说明：用于配置和管理网络接口、路由表等网络相关信息

### 用法
`ip`很多子命令可以被缩写，比如`ip address`可以被缩写为`ip addr`或者`ip a`，具体如下：

| 标准写法 | 缩写形式
| --- | ---
| ip address        | ip addr, ip a |
| ip address show   | ip a s        |
| ip address delete | ip addr del   |
| ip route          | ip r          |
| ip route add      | ip r a        |
| ip route del      | ip r d        |

### 示例
```sh
# 显示所有网卡信息
ip a

# 显示eth0网卡的信息
ip a s eth0

# 从网卡上删除指定IP
ip addr del 192.168.0.1 dev eth0
```

## ip route
```sh
# 查看路由信息
ip r

# 添加静态路由，访问192.168.0.0/24通过192.168.0.1
ip route add 192.168.0.0/24 via 192.168.0.1

# 增加默认路由，via 192.168.0.1 是我的默认路由器
ip route add default via 192.168.0.1 dev eth0

# 清空路由表
ip route flush all

# 删除路由
ip route del 192.168.1.1 dev 192.168.0.1
```
