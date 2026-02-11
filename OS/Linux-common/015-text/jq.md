## jq命令
说明：命令行JSON处理器

### 用法
```
jq [options] <jq filter> [file...]
jq [options] --args <jq filter> [strings...]
jq [options] --jsonargs <jq filter> [JSON_TEXTS...]
```

| 选项 | 说明
| --- | ---
| -r | 去除输出值的引号
|  | 
|  | 

### 函数
| 函数 | 说明
| --- | ---
| to_entries    | 将JSON对象转换为键值对数组
| sort_by       | 对数组进行排序
| from_entries  | 将键值对数组转换为JSON对象
| tonumber      | 将字符串转换为数字
| select        | 过滤数组或对象，根据条件选择元素
| has           | 判断对象是否有指定的key
| contains      | 判断字符串是否包含指定的子字符串


### 示例
```sh
# 取json文本中key为id的值
| jq '.id'

# 如果host的值是一个列表，用[N]取值
| jq '.host[0].id'

# 遍历
echo '[1,2,3,4]' | jq '.[]'

# instances是个列表，遍历instances，打印每个数据中的id字段
jq '.instances[].id'

# 使用map函数遍历数组，进行处理或转换
echo '[1,2,3,4]' | jq 'map(. * 2)' 

# 如果数据中有hostname，才会读。这种方式不会返回null
jq 'select(has("hostname")) | .hostname'

# 查找一个元素是字典的列表，如果元素的key1的值等于AAA，则显示key2的值
jq '.[] | select(.key1 == "AAA") | .key2'

# 过滤host字段包含AAA
jq '.[] | select(.host | contains("AAA")) | .'

# 展示多个key
jq .key1,.key2
jq '.key1 + "\t" + .key2'

# 打印时数字转成字符串
jq '.key1 + "\t" + (.key2 | tostring)'

# 设置默认值
jq '."value" // 0 as $value | "The value is: " + ($value | tostring)' input.json

# 对key进行排序（无法准确排序数字）
jq 'to_entries | sort_by(.key) | from_entries' << EOF
{
  "332": "71778200 78106400 87167200 ",
  "1849": "70634600 99955000 87040000 84580600 90491400 96246200 ",
  "608": "85843200 71403600 ",
  "012": "77101800 78671200 98800400 76977000 75716800 ",
  "1200": "91112600 89516200 85014800 78593400 "
}
EOF
```
