## zip命令&
说明：压缩文件或目录的工具

zip压缩的文件可以被unzip命令解压缩

### 用法
```
zip  [-aABcdDeEfFghjklLmoqrRSTuvVwXyz!@$]  [--longoption ...]  [-b path] [-n suffixes] [-t date] 
    [-tt date] [zipfile [file ...]]  [-xi list]
```

zip压缩时会自动添加.zip后缀，除非归档名中已包含.明确指定其它后缀

重复执行zip命令可以追加文件到已存在的zip归档中

| 选项 | 说明
| --- | ---
| -#    | 压缩级别，0-9，默认6，1为最快，9为最高压缩比，0为不压缩
| -e    | 加密压缩文件
| -P    | 在压缩时明文（不安全）设置加密密码
| -r    | 递归压缩目录下所有文件
| -x    | 排除指定文件或目录不压缩，多个文件或目录用空格分隔
| -m    | 压缩后删除原始文件


### 示例
```sh
# 压缩test.txt文件为test.zip，并加密密码为123456
zip -e -P 123456 test test.txt

# 向test.zip追加test2.txt文件，此时不需要输入密码
zip test test2.txt

# 压缩test目录为test.zip
zip -r test.zip test/
```
