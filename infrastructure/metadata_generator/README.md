# mysql-metadata-generator

To test some MySQL capabilities, it’s good to have a good number of tables with different complex column types. This script generates random metadata for MySQL.

## Activate your virtualenv if it’s not up
```bash
pip install --upgrade virtualenv
python3 -m virtualenv --python python3 env
source ./env/bin/activate
```

## Install the requirements for the metadata generator
`pip install -r requirements.txt`

Then run the install requirements again.

## Run the script
`python metadata_generator.py`

## Developer environment

### Install and run Yapf formatter

```bash
pip install --upgrade yapf

# Auto update files
yapf --in-place metadata_generator.py

# Show diff
yapf --diff metadata_generator.py

# Set up pre-commit hook
# From the root of your git project.
curl -o pre-commit.sh https://raw.githubusercontent.com/google/yapf/master/plugins/pre-commit.sh
chmod a+x pre-commit.sh
mv pre-commit.sh .git/hooks/pre-commit
```

### Install and run Flake8 linter

```bash
pip install --upgrade flake8
flake8 metadata_generator.py
```
