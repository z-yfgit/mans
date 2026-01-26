## Remove-Item命令
说明：删除指定的项（如文件或目录）

别名
    ri
    rm
    rmdir
    del
    erase
    rd

### 用法
```
Remove-Item [-Path] <string[]>  [<CommonParameters>]

Remove-Item [<CommonParameters>]
```

| 选项 | 说明
| --- | ---
| -Path <路径>  | 指定要删除的项的路径。可以是文件或目录。
| -Recurse      | 递归删除目录中的所有项。
| -Force        | 强制删除项，包括隐藏项和系统项。

### 示例
```powershell
# 删除C:\example\test_dir目录及子项
Remove-Itemi -Recurse -Force -Path C:\example\test_dir

# 删除文件file1.txt和file2.txt
Remove-Item file1.txt, file2.txt
```
