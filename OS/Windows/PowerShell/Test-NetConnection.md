## Test-NetConnection命令
说明：测试与远程计算机的网络连接。

别名
    tnc

| 选项 | 说明
| --- | ---
| -ComputerName     | 要测试连接的计算机名称或IP地址
| -Port             | 要测试的端口

### 示例
```powershell
# 测试与jd.com的80端口的网络连接
Test-NetConnection jd.com -Port 80
```
