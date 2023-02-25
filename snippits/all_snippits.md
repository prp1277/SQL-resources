# Show Create Procedure
## Show DDL of procedure.

```sql
 SHOW CREATE PROCEDURE $procedure_name$;
$caret$
```

# Alter Table Add Index
## Alter table snippet to add an index.

```sql
 ALTER TABLE $table_name$
  ADD INDEX $index_name$ ($index_column_name$);
$caret$
```

# Begin
## Empty BEGIN..END block snippet.

```sql
 BEGIN
$caret$ 
END
```

# Show Databases
## Show all database currently exist on the server.

```sql
 SHOW DATABASES;
$caret$
```

# Create User with Privileges
## Create user with privileges. Specify user password.

```sql
 CREATE USER $user_name$;
 GRANT ALL PRIVILEGES ON *.* TO $user_name$;
 SET PASSWORD FOR $user_name$ = Password($password$);
 FLUSH PRIVILEGES;
$caret$
```

# Create Table with Options Definitions
## Create table statement with table options definition.

```sql
 CREATE TABLE IF NOT EXISTS $table_name$(
  $column1_name$ $column1_type$)
  CHARACTER SET $character$ COLLATE $collate$;
$caret$
```

# GroupBy
## GROUP BY fragment.

```sql
 GROUP BY $caret$
```

# Select Limit
## SELECT * FROM ... LIMIT n.

```sql
 SELECT * FROM $table_name$ LIMIT $number$;
```


# Create SSL User
## Create user with SSL requirement snippet.

```sql
 CREATE USER $user_name$
 IDENTIFIED BY $password$;
 GRANT USAGE ON *.* TO $user_name$ REQUIRE SSL;
$caret$
```

# Show Function Status
## Show function status.

```sql
 SHOW FUNCTION STATUS LIKE '$function_name$';
$caret$
```

# Truncate
## Truncate table snippet.

```sql
 TRUNCATE TABLE $table_name$;
$caret$
```

# Create View
## Create view snippet creates a new view, or replaces an existing one.

```sql
 CREATE OR REPLACE ALGORITHM = UNDEFINED VIEW $view_name$
  AS $caret$
```

# Alter Procedure
## Alter procedure snippet with SQL SECURITY DEFINER.

```sql
 ALTER PROCEDURE $procedure_name$
  SQL SECURITY DEFINER COMMENT 'Alter procedure characteristics';
$caret$
```

# Create Procedure with parameters
## Create procedure with parameters.

```sql
 CREATE PROCEDURE $procedure_name$(
 IN $IN_parameter_name$ $IN_parameter_type$,
 OUT $OUT_parameter_name$  $OUT_parameter_type$)
CONTAINS SQL
BEGIN
$caret$
END;
```

# Case
## Insert case construction snippet.

```sql
 CASE $case_operand$
  WHEN $caret$ THEN 
  ELSE 
END CASE;
```

# Drop Function
## Drop function snippet.

```sql
 DROP FUNCTION IF EXISTS $function_name$;
$caret$
```

# Show Variables Like
## Shows the values of MySQL system variables.

```sql
 SHOW VARIABLES LIKE '$pattern$'$caret$;
```

# Create Trigger
## Create trigger snippet with AFTER INSERT.

```sql
 CREATE TRIGGER $trigger_name$
AFTER INSERT
  ON $table_name$
  FOR EACH ROW
BEGIN
  $caret$
END;
```

# Fetch Cursor
## Fetch with a cursor.

```sql
 FETCH $cursor_name$ 
  INTO $variable_name_to_fetch_into$
$caret$
```

# Drop Table
## Drop table snippet.

```sql
 DROP TABLE IF EXISTS $table_name$ CASCADE;
$caret$
```

# Insert with Select Clause
## Insert rows into the table using select statement.

```sql
 INSERT LOW_PRIORITY IGNORE
  INTO $table1_name$($column1_from_table1$, $column2_from_table1$)
  SELECT $column1_from_table2$, $column2_from_table2$ FROM $table2_name$
  ON DUPLICATE KEY UPDATE $column1_from_table1$ = $column1_from_table2$ * 10;
$caret$
```

# Multi table Update
## Multi table update snippet.

```sql
 UPDATE IGNORE $table1_name$, $table2_name$
  SET $table1_name$.$column1_name$ = $table2_name$.$column2_name$
  WHERE $table1_name$.$conditional_column$ = $conditional_value$;
$caret$
```

# Create User
## Create user snippet creates new MySQL accounts.

```sql
 CREATE USER $user_name$
  IDENTIFIED BY $password$;
$caret$
```

# Update
## Update table snippet.

```sql
 UPDATE LOW_PRIORITY $table_name$
  SET $column_to_set$ = $set_value$
  WHERE $conditional_column$ = $conditional_value$;
$caret$
```

# Select
## SELECT * FROM snippet.

```sql
 SELECT * FROM $caret$
```

# Create Event with Interval
## Create event snippets with interval definition.

```sql
 CREATE EVENT IF NOT EXISTS $event_name$
  ON SCHEDULE EVERY $interval$ STARTS $timestamp$
  ON COMPLETION PRESERVE
  ENABLE
  COMMENT 'comment this event'
  DO $caret$
```

# Create Event
## Create event snippet creates and schedules a new event.

```sql
 CREATE EVENT IF NOT EXISTS $event_name$
  ON SCHEDULE AT $timestamp$
  ON COMPLETION NOT PRESERVE
  COMMENT 'comment this event'
  DO $caret$
```

# Create Function
## Create function snippet with parameters.

```sql
 CREATE FUNCTION $function_name$ (
  $parameter_name1$ $parameter_type1$, $parameter_name2$ $parameter_type2$)
  RETURNS $return_type$
BEGIN
  $caret$
  RETURN ;
END;
```

# Alter Table Add Column
## Alter table snippet to add a column.

```sql
 ALTER TABLE $table_name$ 
  ADD COLUMN $column_name$ $data_type$;
$caret$
```

# Grant
## Grant some privilegies to user.

```sql
 GRANT $privilege1$, $privilege2$ ON $database_name$ TO $user_name$;
$caret$
```

# While
## While snippet.

```sql
 WHILE $condition$ DO 
$caret$
END WHILE;
```

# Create Database
## Create database snippet.

```sql
 CREATE DATABASE IF NOT EXISTS $database_name$;
$caret$
```

# Drop Event
## Drop event snippet.

```sql
 DROP EVENT IF EXISTS $event_name$;
$caret$
```

# Create Merge Table
## Create merge table snippet.

```sql
 CREATE TABLE IF NOT EXISTS $merge_table_name$(
  $column1_name$ $column1_type$ NOT NULL AUTO_INCREMENT PRIMARY KEY,
  $column2_name$ $column2_type$)
  ENGINE = MERGE UNION = ($table_to_merge1$, $table_to_merge2$) INSERT_METHOD = LAST;
$caret$
```

# Show Create Table
## Show DDL of table.

```sql
 SHOW CREATE TABLE $table_name$;
$caret$
```

# Alter View
## Alter view snippet changes the definition of a view, which must exist.

```sql
 ALTER ALGORITHM = MERGE VIEW $view_name$ ($column1$, $column2$)  
  AS $caret$
```

# Alter Table Drop Column
## Alter table snippet to drop a column.

```sql
 ALTER TABLE $table_name$ 
  DROP COLUMN $column_name$;
$caret$
```

# Region
## Code snippet for region.

```sql
 #region $name$
$caret$
#endregion
```

# Show Engine Innodb Status
## Snippet provides information about the InnoDB internal state.

```sql
 SHOW ENGINE INNODB STATUS;
$caret$
```

# Show Create View
## Show DDL of view.

```sql
 SHOW CREATE VIEW $view_name$;
$caret$
```

# Insert with Set Clause
## Insert the value into the column using set statement.

```sql
 INSERT DELAYED INTO $table_name$
  SET $column1_name$ = $value_column1$;
$caret$
```

# Alter Database
## Alter database snippet with DEFAULT CHARACTER SET.

```sql
 ALTER DATABASE $database_name$
  DEFAULT CHARACTER SET $charset_name$ DEFAULT COLLATE $collate_name$;
$caret$
```

# Declare
## Condition declaration snippet with SQLSTATE.

```sql
 DECLARE $condition_name$ CONDITION
  FOR SQLSTATE $sqlstate_value$$caret$
```

# Show Create Function
## Show DDL of function.

```sql
 SHOW CREATE FUNCTION $FunctionName$;
$caret$
```

# Alter Table Add Foreign Key
## Alter table snippet to add a foreign key.

```sql
 ALTER TABLE $TableName$
  ADD CONSTRAINT FK_$TableName$_$IndexName$_$IndexColName$ FOREIGN KEY (col1)
    REFERENCES $IndexName$($IndexColName$) ON DELETE RESTRICT ON UPDATE RESTRICT;
```

# Insert
## Insert rows into the table snippet.

```sql
 INSERT HIGH_PRIORITY INTO $table_name$(
  $column1_name$, $column2_name$)
  VALUES ($value_column1$, $value_column2$);
$caret$
```

# Select Count
## Select counting the number of records snippet.

```sql
 SELECT COUNT(*) FROM $caret$
```

# Declare Cursor
## Cursor declaration snippet.

```sql
 DECLARE $cursor_name$ CURSOR FOR
  SELECT $table_name$.$column1_name$ 
FROM
  $table_owner$.$table_name$;
$caret$
```

# Delete
## Delete snippet with LIMIT.

```sql
 DELETE LOW_PRIORITY QUICK
  FROM $table_name$
  WHERE $column_name$ = $column_value$
  LIMIT $row_count$;
$caret$
```

# Drop Procedure
## Drop procedure snippet.

```sql
 DROP PROCEDURE IF EXISTS $procedure_name$;
$caret$
```

# Drop View
## Drop view snippet with CASCADE.

```sql
 DROP VIEW IF EXISTS $view_name$ CASCADE;
$caret$
```

# Repeat
## Insert repeat construction.

```sql
 REPEAT 
$caret$
UNTIL $condition$
END REPEAT;
```

# Revoke
## Revoke user privilegies snippet.

```sql
 REVOKE $privilege1$, $privilege2$ ON $database_name$ FROM $user_name$;
$caret$
```

# Replace
## Replace rows in the table snippet.

```sql
 REPLACE LOW_PRIORITY INTO $table_name$(
  $column1_name$, $column2_name$)
  VALUES ($value_column1$, $value_column2$);
$caret$
```

# Drop Trigger
## Drop trigger snippet.

```sql
 DROP TRIGGER $trigger_name$;
$caret$
```

# Alter Event
## Alter event snippet with ON SCHEDULE and STARTS CURRENT_TIMESTAMP.

```sql
 ALTER EVENT $event_name$
  ON SCHEDULE EVERY $interval$
  STARTS CURRENT_TIMESTAMP + $timestamp$
  ENABLE;
$caret$
```

# OrderBy
## ORDER BY fragment.

```sql
 ORDER BY $caret$
```

# Alter Function
## Alter function snippet can be used to change the characteristics of a stored function.

```sql
 ALTER FUNCTION $function_name$
 CONTAINS SQL COMMENT 'You must have the ALTER ROUTINE privilege for the routine';
$caret$
```

# Loop
## Insert loop construction.

```sql
 LOOP
$caret$
END LOOP;
```

# Multi table Delete
## Multi table delete snippet.

```sql
 DELETE $table1_name$
  FROM $table1_name$, $table2_name$
  WHERE $table1_name$.$column_name$ = $table2_name$.$column_name$;
$caret$
```