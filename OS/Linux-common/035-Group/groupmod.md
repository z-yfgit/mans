## groupmod命令&
说明：修改用户组

### 用法
```
groupmod [options] GROUP
```

| 选项 | 说明
| --- | ---
| -g, --gid \<GID>              | 修改组ID
| -n, --new-name \<NEW_GROUP>   | 修改组名
| -o, --non-unique              | 允许使用重复的 GID

### 示例

```sh
# 将组ID为500的修改成组ID为1500
groupmod -g 1500 500

# 将组名test1_group修为为test2_group
groupmod -n test2_group test1_group
```
