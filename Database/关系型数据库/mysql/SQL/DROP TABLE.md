## DROP TABLE语句&
说明：删除一个或多个表

### 用法
```
DROP [TEMPORARY] TABLE [IF EXISTS] tbl_name [, tbl_name] ...
```
| 参数 | 说明
| --- | ---
| IF EXISTS | 如果表不存在则忽略，否则删除

```sql
-- 删除表user
DROP TABLE IF EXISTS user;
```