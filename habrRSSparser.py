from typing import Dict, Union, Any
from loguru import logger
import feedparser
from psycopg2 import connect
import re


def parse_posts() -> list:
    logger.info('Trying to parse habr.com via RSS...')

    try:
        rss_data = feedparser.parse('https://habr.com/ru/rss/all/all/?fl=ru')
        posts_count = len(rss_data.entries)
        posts_parsed = []

        for post in range(posts_count):
            post_content = rss_data.entries[post]
            post_id = re.search(r'post/(\d+)/', post_content.guid).group(1)
            tags = post_content.tags
            normal_tag = []

            for _ in range(len(tags)):
                normal_tag.append(tags[_]['term'])
            post_parsed: dict[str, Union[str, Any]] = {
                'post_id': post_id,
                'title': post_content.title,
                'link': post_content.guid,
                'description': post_content.description,
                'tags': ', '.join(normal_tag),
            }
            posts_parsed.append(post_parsed)
        return posts_parsed

    except Exception:
        logger.error("Unable to parse habr.com")
        exit(-1)

    finally:
        logger.info('habr.com successfully parsed!')


def update_db(posts_parsed: list) -> None:
    logger.info('Trying to connect database...')

    try:
        connection = connect(dbname='',
                             user='',
                             password='',
                             host='')
        cursor = connection.cursor()
        logger.info('Successfully connected to database!')

        for post in posts_parsed:
            cursor.execute(f'SELECT * FROM public.posts WHERE post_id={post["post_id"]}')
            db_response = cursor.fetchall()
            if not db_response:
                cursor.execute(f'INSERT INTO public.posts (title, link, description, tags, post_id) '
                               f'VALUES (\'{post["title"]}\','
                               f'\'{post["link"]}\','
                               f'\'{post["description"]}\','
                               f'\'{post["tags"]}\','
                               f'\'{post["post_id"]}\')')
                connection.commit()
                logger.info(f'INSERT INTO database post with post_id - {post["post_id"]}')

    except Exception:
        logger.error("Unable to connect or update database")
        exit(-1)

    finally:
        connection.close()
        logger.info('Database successfully updated!')


def main():
    logger.add('parser.log', format='{time} | {level} | {message}',
               level='DEBUG',
               rotation='15 KB',
               compression='zip')
    try:
        logger.info('===================================================================')
        logger.info('Starting parser')
        posts_parsed = parse_posts()
        update_db(posts_parsed)
        logger.info('Successful done!')

    except Exception:
        logger.error('Unable to parse habr.com and update database')
        exit(-2)


if __name__ == '__main__':
    main()
