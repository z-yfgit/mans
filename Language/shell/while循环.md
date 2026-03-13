## while循环

### 基础循环
```sh
# 初始化循环变量
num=1

while true
do
    # 这里是循环体，可以添加你需要执行的操作
    echo "当前数字：$num"
    ((num++))

    # 由于循环条件为true，所以需要在循环体中添加结束条件，否则会无限循环
    if [ $num -gt 10 ]; then
        break
    fi
    
done
```