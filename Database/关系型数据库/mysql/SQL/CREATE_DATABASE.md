## CREATE DATABASE语句&
说明：创建数据库

CREATE DATABASE 和 CREATE SCHEMA 是等价的。

### 用法
```
CREATE DATABASE [IF NOT EXISTS] db_name [create_option] ...
```

| 创建选项 | 说明
| --- | ---
| CHARACTER SET charset_name    | 指定数据库默认字符集，默认utf8mb4
| COLLATE collation_name        | 指定数据库默认字符集排序规则，默认utf8mb4_unicode_ci
| ENCRYPTION { 'Y' | 'N' }      | 是否加密数据库，默认N

ENCRYPTION

### 示例
```sql
-- 如果数据库db01不存在，则创建
CREATE DATABASE IF NOT EXISTS db01;

-- 查看数据库db01的创建语句
SHOW CREATE DATABASE db01;
```
