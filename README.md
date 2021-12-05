# habrRSSparser
## _Parse and read simple_

habrRSSparser is a python script for parsing habs from habr.com via RSS and write them to PostgreSQL database.

![working](https://user-images.githubusercontent.com/22868859/144743169-b5e1cb37-26bf-4504-bfae-b900ec2dbc63.gif)

## Features


- Change sections
- Set PostgreSQL databae scheme

## Installation

habrRSSparser requires [Python](https://www.python.org/) v3.8+  and PostgreSQL client binary to run.

### For MacOS set PostgreSQL PATH

Set PATH

```sh
PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin/
```

Create venv and install the dependencies

```sh
git clone https://github.com/3ayazaya/habrRSSparser
cd habrRSSparser
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
chmod +x habrRSSparser.py
```

Create .env file

```sh
touch .env
```

Configure .env file

```
DB_USER='<YOUR_DATABASE_USER_FOR_CONNECTION>'
DB_HOST='<YOUR_DATABASE_IP_OR_URL_FOR_CONNECTION>'
DATABASE='<YOUR_DATABASE_NAME_FOR_CONNECTION>'
DB_PASSWORD='<YOUR_DATABASE_USER_PASSWORD_FOR_CONNECTION>'
```

Start parsing
```sh
./habrRSSparser.py
```
## Modules

habrRSSparser is currently use the following plugins.
Instructions on how to use them are linked below.

| Module | README |
| ------ | ------ |
| colorama | [pypi](https://pypi.org/project/colorama/) |
| feedparser | [pypi](https://pypi.org/project/feedparser/) |
| loguru | [GitHub](https://github.com/Delgan/loguru) |
| psycopg2 | [psycopg](https://www.psycopg.org/docs/) |
| time | [docs.python](https://docs.python.org/3/library/time.html) |
| python-dotenv | [pypi](https://pypi.org/project/python-dotenv/) |

