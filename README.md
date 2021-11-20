# habrRSSparser
## _Parse and read simple_

habrRSSparser is a python script for parsing habs from habr.com via RSS and write them to PostgreSQL database.

## Features

- Parse creds for database from env
- Change sections

## Installation

habrRSSparser requires [Python](https://www.python.org/) v3.8+ to run.

Install the dependencies and start the parsing.

```sh
git clone https://github.com/3ayazaya/habrRSSparser
cd habrRSSparser
pip install -r requirements.txt
python3 habrRSSparser.py
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
