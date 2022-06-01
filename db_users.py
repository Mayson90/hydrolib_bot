from conf import db, connection

from pymongo import MongoClient
from datetime import datetime


client = MongoClient(connection)
db = client[db]


async def create_user(message):

    """Функция проверяет существующего пользователя
    
    Если его нет - создает нового
    
    Если пользователь существует - обновляет поле даты

    """

    set_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if db.users.find_one({'user_id': message.from_user.id}) is None:
        new_user = {
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'user_name': message.from_user.username,
            'user_id': message.from_user.id,
            'date': set_date,
        }
        await db.users.insert_one(new_user)

    else:
        db.users.update_one({'user_id': message.from_user.id}, {'$set': {'date': set_date}})

    return
