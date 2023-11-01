# USERS
CREATE_TABLE_PROFILE = """CREATE TABLE IF NOT EXISTS telegram_users 
                          (ID INTEGER PRIMARY KEY,
                           TELEGRAM_ID INTEGER,
                           USERNAME CHAR(60),
                           UNIQUE(TELEGRAM_ID))"""

INSERT_PROFILE_QUERY = """INSERT OR IGNORE INTO telegram_users VALUES (?,?,?)"""

SELECT_PROFILE_QUERY = """SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?"""

# MUSIC
CREATE_TABLE_MUSIC = """CREATE TABLE IF NOT EXISTS music_list
                        (ID INTEGER PRIMARY KEY,
                        TELEGRAM_ID INTEGER,
                        MUSIC TEXT,
                        UNIQUE(ID))"""

INSERT_MUSIC_QUERY = """INSERT OR IGNORE INTO music_list VALUES (?,?,?)"""

SELECT_MUSIC_QUERY = """SELECT * FROM music_list WHERE TELEGRAM_ID = ?"""

# MEME
CREATE_TABLE_MEME = """CREATE TABLE IF NOT EXISTS meme_list
                       (ID INTEGER PRIMARY KEY,
                       TELEGRAM_ID INTEGER,
                       MEME TEXT,
                       UNIQUE(ID))"""

INSERT_MEME_QUERY = """INSERT OR IGNORE INTO meme_list VALUES (?,?,?)"""

SELECT_MEME_QUERY = """SELECT * FROM meme_list WHERE TELEGRAM_ID = ?"""
