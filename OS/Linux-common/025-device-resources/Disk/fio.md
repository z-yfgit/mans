## fio命令
说明：这里写命令的简单说明

### 用法
```
fio [options] [job options] <job file(s)>
```

| 选项 | 说明
| --- | ---
| -name     | 任务名
| -filename | 读取/写入的文件名
| -bs       | 块大小
| -size     | 总大小
| -numjobs  | 并发
| -runtime  | 运行时间
| -rw       | 读写模式，可选randread/randwrite/read/write
| -ioengine | IO引擎，可选psync/libaio


### 示例
```sh
# 4K随机读
fio -filename=./rand_read_4K.txt -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=4k -size=10G -numjobs=50 -runtime=120 -group_reporting -name=rand_read_4k

# 4K顺序读
fio -filename=/home/sqe_read_4K.txt -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=4k -size=10G -numjobs=50 -runtime=120 -group_reporting -name=sqe_read_4k

# 4K随机写
fio -filename=/home/rand_write_4K.txt -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=4k -size=10G -numjobs=50 -runtime=120 -group_reporting -name=rand_write_4k

# 4K顺序写
fio -filename=/home/sqe_write_4K.txt -direct=1 -iodepth 1 -thread -rw=write -ioengine=psync -bs=4k -size=10G -numjobs=50 -runtime=120 -group_reporting -name=sqe_write_4k
```
