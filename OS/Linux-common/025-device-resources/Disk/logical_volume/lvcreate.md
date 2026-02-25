## lvcreate命令
说明：创建一个逻辑卷

lvcreate在VG中创建一个新的LV。对于标准lv，这需要从VG的空闲物理区段中分配逻辑区段。如果没有足够的空闲空间，可以使用其他pv扩展VG (vgextend(8))，或者减少或删除现有的lv (lvremove(8)、lvreduce(8))。

lvcreate还可以创建现有lv的快照，例如用于备份。新快照LV中的数据表示创建快照时原始LV的内容。

RAID LV可以通过在创建LV时指定LV类型来创建(参见lvmraid(7))。不同的RAID级别需要在VG中提供不同数量的惟一pv进行分配。


### 用法
```
创建线性卷（linear LV），默认，常用
lvcreate -L|--size Size[m|UNIT] VG 
      [ -l|--extents Number[PERCENT] ]
      [    --type linear ]
      [ COMMON_OPTIONS ]
      [ PV ... ]

创建条带卷（striped LV），类似 raid0
lvcreate -i|--stripes Number -L|--size Size[m|UNIT] VG
      [ -l|--extents Number[PERCENT] ]
      [ -I|--stripesize Size[k|UNIT] ]
      [ COMMON_OPTIONS ]
      [ PV ... ]

创建镜像卷（mirror LV），类似 raid1
lvcreate -m|--mirrors Number -L|--size Size[m|UNIT] VG
      [ -l|--extents Number[PERCENT] ]
      [ -R|--regionsize Size[m|UNIT] ]
      [    --mirrorlog core|disk ]
      [    --minrecoveryrate Size[k|UNIT] ]
      [    --maxrecoveryrate Size[k|UNIT] ]
      [ COMMON_OPTIONS ]
      [ PV ... ]
```

| 选项 | 说明
| --- | ---
| -L, --size Size[m|UNIT]     | 指定LV的大小
| -n, --name LV_NAME          | 指定LV的名称

### 示例
```sh
# 创建一个大小为 500GB 的线性卷，名字叫 mylv，指定从 myvg 这个 VG 中分配空间
lvcreate -L 500G -n mylv myvg

# 检查mylv这个LV是否创建成功
lvdisplay myvg/mylv   # 注意路径格式是：卷组名/逻辑卷名，直接指定lv名称查不到

# 格式化为ext4文件系统，注意路径格式是/dev/卷组名/逻辑卷名
mkfs.ext4 /dev/myvg/mylv

# 挂载mylv到目录/home/mylv
mkdir /data001
mount /dev/myvg/mylv /data001
```
