import argparse
import logging
import sys
import uuid

from mysql.connector import connect

QUERY = """
SELECT  DISTINCT t.table_schema as schema_name
    FROM information_schema.tables t
    WHERE t.table_schema NOT IN
          ('mysql', 'information_schema',
           'performance_schema', 'sys')
    ORDER BY t.table_schema;
"""


def get_conn(connection_args):
    return connect(database=connection_args['database'],
                   host=connection_args['host'],
                   user=connection_args['user'],
                   password=connection_args['pass'])


def cleanup_metadata(connection_args):
    conn = get_conn(connection_args)

    cursor = conn.cursor()
    cursor.execute(QUERY)
    rows = cursor.fetchall()
    for row in rows:
        database_name = row[0]
        database_stmt = build_drop_database_statement(database_name)
        cursor.execute(database_stmt)
        print('Cleaned database: {}'.format(database_name))
        conn.commit()

    cursor.close()


def build_drop_database_statement(database_name):
    database_stmt = 'DROP DATABASE {};'.format(database_name)
    return database_stmt


def parse_args():
    parser = argparse.ArgumentParser(
        description='Command line to cleanup metadata from mysql')
    parser.add_argument('--mysql-host',
                        help='Your mysql server host',
                        required=True)
    parser.add_argument('--mysql-user',
                        help='Your mysql credentials user',
                        required=True)
    parser.add_argument('--mysql-pass',
                        help='Your mysql credentials password',
                        required=True)
    parser.add_argument('--mysql-database',
                        help='Your mysql database name',
                        required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    # Enable logging
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    cleanup_metadata({
        'database': args.mysql_database,
        'host': args.mysql_host,
        'user': args.mysql_user,
        'pass': args.mysql_pass
    })
