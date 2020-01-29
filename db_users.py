import pymongo
from pymongo import MongoClient
from datetime import datetime

client = MongoClient('localhost', 27017)

db = client['hydrolib_db']

def check_user(message):

	# Функция проверяет существующего пользователя
	# Если его нет - создает нового
	# Если пользователь существует - обновляет поле даты

	set_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

	if db.users.find_one({'user_id': message.from_user.id}) == None:
		new_user = {
			'first_name': message.from_user.first_name,
			'last_name': message.from_user.last_name,
			'user_name': message.from_user.username,
			'user_id': message.from_user.id,
			'date': set_date,
		}
		db.users.insert_one(new_user)

	elif db.users.find_one({'user_id': message.from_user.id}) is not None:
		db.users.update_one({'user_id': message.from_user.id}, {'$set': {'date': set_date}})

	return