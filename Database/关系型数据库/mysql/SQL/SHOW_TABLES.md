## SHOW TABLES语句
说明：显示数据库中的所有表

### 用法
```
SHOW [EXTENDED] [FULL] TABLES
    [{FROM | IN} db_name]
    [LIKE 'pattern' | WHERE expr]
```

| 选项 | 说明
| --- | ---
|  | 
|  | 
|  | 

### 示例
```sql
-- 显示所有表
SHOW TABLES;

-- 显示sys数据库中的所有表
SHOW TABLES IN sys;
```
