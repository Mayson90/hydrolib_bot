import os
from dotenv import load_dotenv

load_dotenv()

# токен бота
token = os.getenv('BOT_TOKEN')
# подключение к базе
connection = str(os.environ.get('DB_CONNECTION'))
db = 'hydrolib_db'
