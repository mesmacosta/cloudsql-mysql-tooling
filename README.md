# cloudsql-mysql-tooling

Scripts with the goal to enable easy usage of some MySQL operations.

## INIT database
```bash
./init-db.sh
```

## Creating Schemas and Tables in MySQL
```bash
./connect-db.sh
```
Provide your password when prompted, then execute:
```bash
CREATE SCHEMA MY_SCHEMA;
CREATE TABLE MY_SCHEMA.MY_TABLE (name INT, address TEXT);
exit
```

## Clean up MySQL Schemas and Tables
```bash
./cleanup-db.sh
```

## Delete the MySQL database
```bash
./delete-db.sh
```

