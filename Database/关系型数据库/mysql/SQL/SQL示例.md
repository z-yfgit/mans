## SQL示例

### 查看每个数据库所占磁盘大小
```sql
select
  table_schema as "库名",
  truncate(sum(`data_length`) / 1024 / 1024, 2) as "表所占空间（mb）",
  truncate(sum(`index_length`) / 1024 / 1024, 2) as "索引所占空间（mb）",
  truncate((sum(`data_length`) + sum(`index_length`)) / 1024 / 1024,2) as "空间累计（mb）"
from
  information_schema.`tables`
group by `table_schema`;
```

### 查看所有用户
```sql
select user,host from mysql.user;

-- 或者
SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;
```

