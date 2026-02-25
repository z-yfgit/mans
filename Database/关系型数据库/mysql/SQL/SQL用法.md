# SQL

SELECT table_name, data_length + index_length AS len, table_rows,
CONCAT(ROUND((data_length + index_length)/1024/1024,2),'MB') AS datas FROM information_schema.tables 
WHERE table_schema = 'database_name' ORDER BY len DESC; # 修改database_name


### where
| 运算符 | 说明 |
| ---		| ---
| =  		| 等于
| <>, != 	| 不等于
| > 		| 大于
| < 		| 小于
| >= 		| 大于等于
| <= 		| 小于等于

```sql
-- 单条件
select * from table_name where field = 'abc';

-- 多条件 AND
select * from table_name where field1 = 'abc' AND field2 = 'bbb';

-- 多条件 OR
select * from table_name where field1 = 'abc' OR field2 = 'bbb';
```

