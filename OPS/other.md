## 扫描新增磁盘
```sh
for i in `ls /sys/class/scsi_host` ; do echo "- - -" > /sys/class/scsi_host/$i/scan ; done
echo 1  >/sys/bus/pci/slots/69/power
lspci -s 65:00.0 -v |grep -i slot
```

## 将命令输出结果丢弃
```sh
ls >/dev/null 2>&1
```

## 单引号中使用变量
```sh
echo 'hello "'${var_name}'"'
```

## 一次创建多个有规律的文件
```sh
touch file{1..5}.txt
ls
# file1.txt  file2.txt  file3.txt  file4.txt  file5.txt
```

## 快速给文件添加后缀
```sh
cp file{,.bak}
ls
# file file.bak
```