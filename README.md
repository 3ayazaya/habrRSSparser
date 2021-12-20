# habrRSSparser

![habrRSSParser](https://user-images.githubusercontent.com/22868859/145724745-38fc2184-21e7-4525-a3ce-fdbc7eb58776.png)

## _Parse and read simple_

**habrRSSparser** is a python script for parsing habs from habr.com via RSS and write them to PostgreSQL database.

## Install app

habrRSSparser requires `docker` and `docker-compose` to run.

Clone repo
```shell
git clone https://github.com/3ayazaya/habrRSSparser
cd habrRSSparser
```

Create **.env** file
```shell
touch app/.env
```

Configure **.env** file

```shell
vim app/.env
```
Paste and configure
```
DB_USER='<YOUR_DATABASE_USER_FOR_CONNECTION>'
DATABASE='<YOUR_DATABASE_NAME_FOR_CONNECTION>'
DB_PASSWORD='<YOUR_DATABASE_USER_PASSWORD_FOR_CONNECTION>'
```

## Build app
Set **env**
```shell
set -a
source app/.env
```
Build app with _docker-compose_
```shell
docker-compose build
```

## Run app
Running app with _docker-compose_
```shell
docker-compose up -d
```

## Logs
Logs are stored in `app/logs` folder

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

