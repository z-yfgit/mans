## groupadd命令&
说明：添加新用户组

### 用法
```
groupadd [options] GROUP
```

| 选项 | 说明
| --- | ---
| -g   | 指定新组的ID
| -f   | 即使组已存在也不报错
### 示例

```sh
# 创建一个名为test_group的用户组，并设置组ID为600
groupadd -g 600 test_group
```
