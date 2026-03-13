## for循环

### 基础循环
```sh
for num in {1..10}
do
    # 这里是循环体，可以添加你需要执行的操作
    echo "当前数字：$num"

done
```

```sh
declare -a data
data+=("a")
data+=("b")
data+=("c")

for ((i=0; i<${#data[@]}-1; i++)); do
    current=${data[$i]}
    next=${data[$((i+1))]}
    echo "当前: $current, 下一个: $next"
done
```
