# cloudsql-mysql-tooling

Scripts with the goal to enable easy usage of some MySQL operations.

## INIT DATABASE
Execute
```bash
./init-db.sh
```

## CREATE METADATA
### Creating Schemas and Tables in MySQL
Execute
```bash
./connect-db.sh
```
Provide your password when prompted, then execute:
```bash
CREATE SCHEMA MY_SCHEMA;
CREATE TABLE MY_SCHEMA.MY_TABLE (name INT, address TEXT);
exit
```

## CLEAN UP MYSQL
### Clean up MySQL Schemas and Tables
```bash
./cleanup-db.sh
```

## DELETE DEMO
### Delete the MySQL database
```bash
./delete-db.sh
```

