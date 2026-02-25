## DELETE语句
说明：删除表中的数据

### 用法
```
单表语法
DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name [[AS] tbl_alias]
    [PARTITION (partition_name [, partition_name] ...)]
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]

多表语法
DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    tbl_name[.*] [, tbl_name[.*]] ...
    FROM table_references
    [WHERE where_condition]

DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    FROM tbl_name[.*] [, tbl_name[.*]] ...
    USING table_references
    [WHERE where_condition]

DELETE FROM table_name WHERE field_name = "value" limit 1;
```

| 子句 | 说明
| --- | ---
| PARTITION (partition_name [, partition_name] ...) | 删除指定分区数据，默认删除所有分区数据
| WHERE where_condition                             | 删除条件，默认删除所有记录
| ORDER BY ...                                      | 先排序再删除记录，默认不排序。与LIMIT结合使用时才有意义。
| LIMIT row_count                                   | 限制删除的记录数，默认删除所有记录

### 示例
```sql
-- 单表示例
-- 删除表table01中字段field01值为value01的一条数据
DELETE FROM table01 WHERE field01 = "value01" LIMIT 1;

-- 删除表table01中id最大的一条数据
DELETE FROM table01 ORDER BY id DESC LIMIT 1;
```
