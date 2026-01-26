## Select-String命令
说明：搜索指定的字符串

别名
    sls

### 用法
```
Select-String [-Path] <string[]> [-Pattern] <string[]> [-AllMatches] [-CaseSensitive] [-Context <Int32[]>] [-Encoding <string>] [-Exclude <string[]>] [-Include <string[]>] [-List] [-NotMatch] [-Quiet] [-SimpleMatch] [<CommonParameters>]

Select-String -InputObject <psobject> [-Pattern] <string[]> [-AllMatches] [-CaseSensitive] [-Context <Int32[]>] [-Encoding <string>] [-Exclude <string[]>] [-Include <string[]>] [-List] [-NotMatch] [-Quiet] [-SimpleMatch] [<CommonParameters>]
```

| 选项 | 说明
| --- | ---
| -CaseSensitive    | 使匹配项区分大小写。默认情况下，匹配项不区分大小写。
| -NotMatch         | 仅返回不匹配的行。

### 示例
```powershell
# 搜索 test.txt 文件中包含 hello 的行
select-string hello test.txt

# 只能匹配到HELLO
"Hello", "HELLO" | select-string -pattern "HELLO" -casesensitive
```
