
#!/usr/bin/env bash
docker build -t mysql-metadata-generator .
docker tag mysql-metadata-generator mesmacosta/mysql-metadata-generator:stable
docker push mesmacosta/mysql-metadata-generator:stable
