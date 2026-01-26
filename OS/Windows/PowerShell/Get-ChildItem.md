## Get-ChildItem命令
说明：

别名
    gci
    dir
    ls

### 用法
```
Get-ChildItem
    [[-Path] <string[]>]
    [[-Filter] <string>]
    [-Include <string[]>]
    [-Exclude <string[]>]
    [-Recurse]
    [-Depth <uint>]
    [-Force]
    [-Name]
    [<CommonParameters>]

Get-ChildItem
    [[-Filter] <string>]
    -LiteralPath <string[]>
    [-Include <string[]>]
    [-Exclude <string[]>]
    [-Recurse]
    [-Depth <uint>]
    [-Force]
    [-Name]
    [<CommonParameters>]
```

| 选项 | 说明
| --- | ---
| -Path <路径>  | 指定要获取项的路径。默认值为当前目录 (.)。
| -Name         | 仅返回项的名称，而不返回项的详细信息
| -Force        | 强制获取项，包括隐藏项和系统项。

### 示例
```powershell
# 获取C:\Windows目录下的所有项
gci -Path C:\Windows
```