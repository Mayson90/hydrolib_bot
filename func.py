from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from dyct import d_hydro, d_drugs, d_leaders, d_downloads


def create_menu(menu):
    # Функция создания меню

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    row = [KeyboardButton(x) for x in menu[:]]
    markup.add(*row)
    markup.row('Главное Меню')

    return markup


class GetObjects:

    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    async def get_units(self):
        # Функция создания меню персонажей из вызова по ключу фракции

        user_id = self.message.from_user.id
        menu = list(d_hydro[self.message.text])
        markup = create_menu(menu)
        await self.bot.send_message(user_id, 'Выбери персонажа:', reply_markup=markup)

    async def get_unit_card(self, frac):
        # Функция получения карточки персонажа из вызова по ключу фракции и персонажа

        user_id = self.message.from_user.id
        url = str(d_hydro[frac][self.message.text])
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

    async def get_leaders(self):
        # Функция создания меню тактических карт из вызова по ключу лидера

        user_id = self.message.from_user.id
        menu = list(d_leaders[self.message.text])
        markup = create_menu(menu)
        await self.bot.send_message(user_id, 'Выбери карточку:', reply_markup=markup)

    async def get_leaders_card(self, card):
        # Функция получения карточки лидера из вызова по ключу лидера и его карточки

        user_id = self.message.from_user.id
        url = str(d_leaders[card][self.message.text])
        await self.bot.send_photo(user_id, url)
