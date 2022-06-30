# config.ini 

```shell:
[APP]
ENVIRONMENT = development
DEBUG = False

[DATABASE]
USERNAME = root
PASSWORD = p@ssw0rd
HOST = 127.0.0.1
PORT = 5432
DB = my_database

[LOGS]
ERRORS = logs/errors.log
INFO = data/info.log

[FILES]
STATIC_FOLDER = static
TEMPLATES_FOLDER = templates
```

# config.toml

```shell:
# Keys
title = "My TOML Config"

# Tables
[project]
name = "Facebook"
description = "Powerful AI which renders the back of somebody's head, based on their face."
version = "1.0.0"
updated = 1979-05-27T07:32:00Z
author = "Todd Birchard"

[database]
host = "127.0.0.1"
password = "p@ssw0rd"
port = 5432
name = "my_database"
connection_max = 5000
enabled = true

# Nested `tables`
[environments]
  [environments.dev]
    ip = "10.0.0.1"
    dc = "eqdc10"
  [environments.staging]
    ip = "10.0.0.2"
    dc = "eqdc10"
  [environments.production]
    ip = "10.0.0.3"
    dc = "eqdc10"

# Array of Tables
[[testers]]
id = 1
username = "JohnCena"
password = "YouCantSeeMe69"

[[testers]]
id = 3
username = "TheRock"
password = "CantCook123"
```

```python:
"""Load configuration from .toml file."""
import toml


# Read local `config.toml` file.
config = toml.load('settings/config.toml')
print(config)
```

# config.yaml

```shell:
appName: appName
logLevel: WARN

AWS:
    Region: us-east-1
    Resources:
      EC2:
        Type: "AWS::EC2::Instance"
        Properties:
          ImageId: "ami-0ff8a91507f77f867"
          InstanceType: t2.micro
          KeyName: testkey
          BlockDeviceMappings:
            -
              DeviceName: /dev/sdm
              Ebs:
                VolumeType: io1
                Iops: 200
                DeleteOnTermination: false
                VolumeSize: 20
      Lambda:
          Type: "AWS::Lambda::Function"
          Properties:
            Handler: "index.handler"
            Role:
              Fn::GetAtt:
                - "LambdaExecutionRole"
                - "Arn"
            Runtime: "python3.7"
            Timeout: 25
            TracingConfig:
              Mode: "Active"

routes:
  admin:
    url: /admin
    template: admin.html
    assets:
        templates: /templates
        static: /static
  dashboard:
    url: /dashboard
    template: dashboard.html
    assets:
        templates: /templates
        static: /static
  account:
    url: /account
    template: account.html
    assets:
        templates: /templates
        static: /static

databases:
  cassandra:
    host: example.cassandra.db
    username: user
    password: password
  redshift:
    jdbcURL: jdbc:redshift://<IP>:<PORT>/file?user=username&password=pass
    tempS3Dir: s3://path/to/redshift/temp/dir/
  redis:
    host: hostname
    port: port-number
    auth: authentication
    db: databaseconfig.yaml
```

```python:
import yaml

with open(f_cfg, "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

print(config)

```

# .env

```shell:

FLASK_ENV=development
FLASK_APP=app.py
COMPRESSOR_DEBUG=True
STATIC_FOLDER=static
TEMPLATES_FOLDER=templates

```

```python:
"""App configuration."""
from os import environ, path
from dotenv import load_dotenv


# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# General Config
SECRET_KEY = environ.get('SECRET_KEY')
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')

```