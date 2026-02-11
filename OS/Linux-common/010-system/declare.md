## declare命令
说明：declare命令用于声明变量和数组

declare只能在bash shell中使用。

### 用法
```
declare [-aAfFgiIlnrtux] [-p] [name[=value] ...]
```

| 选项 | 说明
| --- | ---
| -a | 声明数组
| -A | 声明关联数组


### 示例
```bash
# 声明关联数组
declare -A user_info

# 关联数组添加元素
user_info["name"]="张三"
user_info["age"]=30
user_info["city"]="北京"

# 修改元素
user_info["age"]=31

# 删除元素


# 查询指定的键值
echo ${user_info["name"]}

# 打印关联数组所有key
echo "关联数组所有key：${!user_info[@]}"
# 补充：[*] 也可获取所有键，但会将所有键拼接为一个字符串

# 打印关联数组所有值
echo "关联数组所有值：${user_info[@]}"


# ============================================================
# 定义数组
declare -a user_like

# 添加数组元素
user_like+=("篮球")
user_like+=("足球")
user_like+=("跑步")

# 数组所有元素
echo ${user_like[@]}

# 指定索引元素
echo ${user_like[0]}  # 输出：篮球

# 修改数组元素
user_like[1]="游泳"

# 删除数组元素
unset user_like[1]
echo ${user_like[@]}

# 验证
echo "删除索引1后：${user_like[@]}"  # 输出：篮球 跑步
echo "数组索引：${!user_like[@]}"    # 输出：0 2 3（索引1被删除，留下空洞）

# 重新构造数组，消除索引空洞（让索引连续）
user_like=("${user_like[@]}")
echo "重排后索引：${!fuser_like[@]}"  # 输出：0 1 2

# 数组长度
echo "数组长度：${#user_like[@]}"  # 输出：3
```
