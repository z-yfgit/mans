## CREATE TABLE语句
说明：创建表

### 用法
```
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)
    [table_options]
    [partition_options]

CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    [(create_definition,...)]
    [table_options]
    [partition_options]
    [IGNORE | REPLACE]
    [AS] query_expression


复制已有表结构（不含数据）
CREATE [TEMPORARY] TABLE [IF NOT EXISTS] tbl_name
    { LIKE old_tbl_name | (LIKE old_tbl_name) }
```


| 参数 | 说明
| --- | ---
| TEMPORARY         | 创建临时表，会话结束后自动删除
| IF NOT EXISTS     | 如果表不存在则创建，否则忽略
| tbl_name          | 表名
| create_definition | 列定义，格式为：column_name data_type [column_options]
| table_options     | 表选项，格式为：option_name option_value
| partition_options | 分区选项，格式为：option_name option_value
| IGNORE            | 忽略错误，继续执行
| REPLACE           | 替换错误，继续执行
| AS                | 从查询表达式中复制数据


| column_options | 列选项
| --- | ---
| AUTO_INCREMENT    | 自动递增，默认0
| PRIMARY KEY       | 主键，默认0
| UNIQUE KEY        | 唯一键，默认0
| FOREIGN KEY       | 外键，默认0   
| DEFAULT           | 默认值，默认NULL
| COMMENT           | 注释，默认''




```sql




-- 查看表结构
show create table tbl_name;


-- 创建按月分区的订单表
CREATE TABLE `order_part` 
    (
        `id` int DEFAULT NULL,
        `create_time` datetime DEFAULT NULL
    )
    PARTITION BY RANGE (to_days(`create_time`))
        (
            PARTITION p202401 VALUES LESS THAN (TO_DAYS('2024-02-01')),
            PARTITION p202402 VALUES LESS THAN (TO_DAYS('2024-03-01')),
            PARTITION p202403 VALUES LESS THAN (TO_DAYS('2024-04-01'))
        ) 

-- 添加分区p202404
ALTER TABLE order_part ADD PARTITION (PARTITION p202404 VALUES LESS THAN (TO_DAYS('2024-05-01')));
```
