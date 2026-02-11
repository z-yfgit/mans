## apt命令
说明：Debian-family Linux系统的软件包管理工具

### 用法
```
apt [-h] [-o=config_string] [-c=config_file] [-t=target_release] [-a=architecture] 
        {list | search | show | update | install pkg [{=pkg_version_number | /target_release}]... 
        | remove pkg...  | upgrade | full-upgrade | edit-sources | {-v | --version} | {-h | --help}}
```

### 示例

```sh
# 更新可用软件包列表
apt update


# 重新安装包
apt reinstall nginx

# 升级指定的包
apt install --only-upgrade policykit-1

# 卸载所有自动安装且不再使用的软件包
apt autoremove


```




### apt使用代理
```sh
# 编辑apt代理配置文件
vi /etc/apt/apt.conf.d/10proxy

Acquire::http::Proxy "http://192.168.68.116:1080";
```

### 配置apt源
```sh
# 配置阿里源，debian 11.x (bullseye)
cat >> /etc/apt/sources.list << EOF
deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib
deb https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main
deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib
deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib
deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib
EOF
```