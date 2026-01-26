## Get-Process命令
说明：获取在本地计算机上运行的进程。

别名
    gps
    ps

### 用法
```
xxx [选项]
```

| 选项 | 说明
| --- | ---
|  | 
| -Name <进程名>                    | 获取指定进程名的进程
| -Id <进程ID>                     | 获取指定进程ID的进程
| -ErrorAction SilentlyContinue    | 忽略错误，继续执行

### 示例
```powershell
# 获取进程名为process01的进程信息，若进程不存在，忽略错误
Get-Process -Name process01 -ErrorAction SilentlyContinue

```

