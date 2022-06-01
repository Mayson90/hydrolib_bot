import os


# токен бота
token = str(os.environ.get('BOT_TOKEN'))

# подключение к базе
connection = str(os.environ.get('DB_CONNECTION'))
db = 'hydrolib_db'