## Copy-Item命令&
说明：复制文件或目录

别名
    cpi
    cp
    copy

### 用法
```
Copy-Item [-Path] <string[]> [[-Destination] <string>] [-Recurse] [-Force] [<CommonParameters>]

Copy-Item [[-Destination] <string>]  [<CommonParameters>]
```

| 选项 | 说明
| --- | ---
| -Recurse  | 递归复制目录中的所有文件和子目录
| -Force    | 强制复制，不提示确认

### 示例
```powershell
# 复制目录 dir01 为 non-existing-dir
Copy-Item dir01 non-existing-dir -Recurse

# 复制文件 file01.txt 和 file02.txt 到目录 dir01
Copy-Item file01.txt, file02.txt dir01\

# 复制目录 dir01 到目录 dir02 中
Copy-Item dir01 dir02\ -Recurse
```
