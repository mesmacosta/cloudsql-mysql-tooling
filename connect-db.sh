#!/usr/bin/env bash
root_dir=$(pwd)
cd infrastructure/terraform

instance_id=$(cat terraform.tfstate | jq '.outputs.instance_id.value')

# Remove quotes
instance_id=${instance_id//\"/}

cd $root_dir

gcloud sql connect $instance_id --user=admin


