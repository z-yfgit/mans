## UPDATE语句
说明：更新表中的行数据

```
单表语法
UPDATE [LOW_PRIORITY] [IGNORE] table_reference
    SET assignment_list
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]

value:
    {expr | DEFAULT}

assignment:
    col_name = value

assignment_list:
    assignment [, assignment] ...

多表语法

UPDATE [LOW_PRIORITY] [IGNORE] table_references
    SET assignment_list
    [WHERE where_condition]
```

| 子句 | 说明
| --- | ---
| IGNORE                    | 忽略更新错误，继续执行后续更新操作
| WHERE where_condition     | 条件，默认更新所有记录
| ORDER BY ...              | 先排序再更新记录，默认不排序。与LIMIT结合使用时才有意义。
| LIMIT row_count           | 限制更新的记录数，默认更新所有记录


```sql
-- 更新表 tbl_name 中，字段 col_1 值为 value_1 的一条数据
UPDATE tbl_name SET col_1 = "value_1" WHERE col_1 = "value_2" LIMIT 1;
```
