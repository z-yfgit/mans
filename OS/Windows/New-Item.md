## New-Item命令
说明：创建新项，例如文件、目录或注册表项

别名
    ni

### 用法
```
New-Item
    [-Path] <String[]>
    [-ItemType <String>]
    [-Value <Object>]
    [-Force]
    [-Credential <PSCredential>]
    [<CommonParameters>]

New-Item
    [[-Path] <String[]>]
    -Name <String>
    [-ItemType <String>]
    [-Value <Object>]
    [-Force]
    [-Credential <PSCredential>]
    [<CommonParameters>]
```

| 选项 | 说明
| --- | ---
| -Path         | 指定新项的路径
| -Name         | 指定新项的名称
| -ItemType     | 指定新项的类型，例如 File、Directory、RegistryKey 等
| -Force        | 强制创建新项，不提示确认



### 示例
```powershell
# 在当前目录创建一个新的文本文件，并写入指定的字符串
New-Item -ItemType "File" -Path . -Name "testfile1.txt" -Value "This is a text string."

# 在C盘根目录创建一个新的目录为 Logfiles
New-Item -ItemType "Directory" -Path "C:\" -Name "Logfiles" 

# 在C盘ps-test目录下创建一个新的目录为 scripts
New-Item -ItemType "Directory" -Path "C:\ps-test\scripts"
```
