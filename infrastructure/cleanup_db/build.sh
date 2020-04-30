
#!/usr/bin/env bash
docker build -t mysql-db-cleaner .
docker tag mysql-db-cleaner mesmacosta/mysql-db-cleaner:stable
docker push mesmacosta/mysql-db-cleaner:stable
