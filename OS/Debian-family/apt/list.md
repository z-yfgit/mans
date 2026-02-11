## apt list命令&
说明：列出安装包

与dpkg-query --list命令相似

### 用法
```sh
apt list [options] [package-patterns]
```
| 选项 | 说明
| --- | ---
| --installed       | 列出所有已安装的包
| --upgradable      | 列出所有可升级的包
| --all-versions    | 列出所有版本的包


### 示例
```sh
# 列出所有已安装的包
apt list --installed

# 列出所有可升级的包
apt list --upgradable

# 列出docker-ce所有可安装的版本
apt list docker-ce --all-versions
```
