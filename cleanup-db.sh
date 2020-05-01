#!/usr/bin/env bash
root_dir=$(pwd)
cd infrastructure/terraform

public_ip_address=$(cat terraform.tfstate | jq '.outputs.public_ip_address.value')
username=$(cat terraform.tfstate | jq '.outputs.username.value')
password=$(cat terraform.tfstate | jq '.outputs.password.value')
database=$(cat terraform.tfstate | jq '.outputs.db_name.value')

# Remove quotes
public_ip_address=${public_ip_address//\"/}
username=${username//\"/}
password=${password//\"/}
database=${database//\"/}

docker run --rm --tty -v \
"$PWD":/data mesmacosta/mysql-db-cleaner:stable \
--mysql-host $public_ip_address \
--mysql-user $username \
--mysql-pass $password \
--mysql-database $database

cd $root_dir