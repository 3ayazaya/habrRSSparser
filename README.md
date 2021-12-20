# habrRSSparser

![habrRSSParser](https://user-images.githubusercontent.com/22868859/145724745-38fc2184-21e7-4525-a3ce-fdbc7eb58776.png)

## _Parse and read simple_

**habrRSSparser** is a python script for parsing habs from habr.com via RSS and write them to PostgreSQL database.

## Features


- Change sections
- Set PostgreSQL databae scheme

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
DB_HOST='<YOUR_DATABASE_IP_OR_URL_FOR_CONNECTION>'
DATABASE='<YOUR_DATABASE_NAME_FOR_CONNECTION>'
DB_PASSWORD='<YOUR_DATABASE_USER_PASSWORD_FOR_CONNECTION>'
```

## Build app

Build app with docker-compose
```shell
docker-compose build
```

## Run app
Running app with docker-compose
```shell
docker-compose up
```

## Crontab
For automatization you can run this app via **cron**
```shell
crontab -e
```
And write for example (start every 5 min):
```editorconfig
*/5 * * * * /usr/local/bin/docker-compose -f /<FULL_PATH_TO_HABRRSSPARSER_FOLDER>/docker-compose.yml start > /dev/null
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

