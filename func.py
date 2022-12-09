from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from dyct import d_hydro, d_drugs, d_downloads


def create_menu(menu):
    # Функция создания меню

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    row = [KeyboardButton(x) for x in menu[:]]
    markup.add(*row)
    if 'Фракции' in menu:
        pass
    else:
        return markup.row('Главное Меню')

    return markup


class GetObjects:

    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    async def get_objects(self):
        # Функция создания меню персонажей из вызова по ключу фракции

        user_id = self.message.from_user.id
        menu = list(d_hydro[self.message.text])
        markup = create_menu(menu)
        await self.bot.send_message(user_id, 'Выбери объект:', reply_markup=markup)

    async def get_object_data(self, value):
        # Функция получения карточки персонажа из вызова по ключу фракции и персонажа

        user_id = self.message.from_user.id
        url = str(d_hydro[value][self.message.text])
        await self.bot.send_photo(user_id, url)

    async def get_drug_card(self):
        # Функция получения карт усилителей по ключу

        user_id = self.message.from_user.id
        url = str(d_drugs[self.message.text])
        await self.bot.send_photo(user_id, url)

    async def get_file_url(self):
        # Функция загрузки файла по ключу

        user_id = self.message.from_user.id
        url = str(d_downloads[self.message.text])
        await self.bot.send_message(user_id, 'документ загружается...')
        await self.bot.send_document(user_id, url)
