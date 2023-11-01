import sqlite3
from database import sql_queryies


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        self.cursor = self.connection.cursor()

    def sql_create(self):
        if self.connection:
            print('Database connected')
        self.connection.execute(sql_queryies.CREATE_TABLE_PROFILE)
        self.connection.execute(sql_queryies.CREATE_TABLE_MUSIC)

    # USERS
    def sql_insert_telegram_users_command(self, telegram_id, username):
        self.cursor.execute(sql_queryies.INSERT_PROFILE_QUERY,
                            (None, telegram_id, username))
        self.connection.commit()

    def sql_select_telegram_users_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'username': row[2]
        }
        return self.cursor.execute(sql_queryies.SELECT_PROFILE_QUERY,
                                   (telegram_id,)).fetchall()

    # MUSIC
    def sql_insert_music_list_command(self, telegram_id, music):
        self.cursor.execute(sql_queryies.INSERT_MUSIC_QUERY,
                            (None, telegram_id, music))
        self.connection.commit()

    def sql_select_music_list_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            'id': row[0],
            'telegram_id': row[1],
            'music': row[2]
        }
        return self.cursor.execute(sql_queryies.SELECT_MUSIC_QUERY,
                                   (telegram_id,)).fetchall()
