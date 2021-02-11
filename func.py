from telebot import types
from dyct import d_hydro, d_drugs, d_leaders


def create_menu(menu):

# Функция создания главного меню

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(menu[0], menu[1], menu[2])
    markup.row('Главное Меню')

    return markup

def create_main_menu(menu):

# Функция создания меню c возвратом в главное меню

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if len(menu) == 4:
        cut = menu[:4]
        markup.row(cut[0], cut[1])
        markup.row(cut[2], cut[3])
        del menu[:4]

    elif len(menu) == 9:
        cut = menu[:9]
        markup.row(cut[0], cut[1], cut[2])
        markup.row(cut[3], cut[4], cut[5])
        markup.row(cut[6], cut[7], cut[8])
        del menu[:9]

    markup.row('Главное Меню')

    return markup

def create_menu_tactics(menu):

# Функция создания меню тактических карт

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if len(menu) == 6:
        cut = menu[:6]
        markup.row(cut[0], cut[1], cut[2])
        markup.row(cut[3], cut[4], cut[5])
        del menu[:6]	
    else:
        print('Error while creating menu of tactics')

    markup.row('назад - Лидеры')

    return markup

def create_menu_detail(menu):

# Функция создания меню для юнитов фракций

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    if len(menu) == 9:
        cut = menu[:9]
        markup.row(cut[0], cut[1], cut[2])
        markup.row(cut[3], cut[4], cut[5])
        markup.row(cut[6], cut[7], cut[8])
        del menu[:9]

    elif len(menu) == 10:
        cut = menu[:10]
        markup.row(cut[0], cut[1])
        markup.row(cut[2], cut[3], cut[4])
        markup.row(cut[5], cut[6], cut[7])
        markup.row(cut[8], cut[9])
        del menu[:10]

    elif len(menu) == 14:
        cut = menu[:14]
        markup.row(cut[0], cut[1], cut[2])
        markup.row(cut[3], cut[4], cut[5])
        markup.row(cut[6], cut[7], cut[8])
        markup.row(cut[9], cut[10])
        markup.row(cut[11], cut[12])
        markup.row(cut[13])
        del menu[:14]		

    markup.row('назад - Фракции')

    return markup

class items:
	
    def __init__(self, bot, message):
		
        self.bot = bot
        self.message = message

    def get_units(self):

    # Функция создания меню персонажей из вызова по ключу фракции

        user_id = self.message.from_user.id
        menu = list(d_hydro[self.message.text])
        markup = create_menu_detail(menu)
        self.bot.send_message(user_id, 'Выбери персонажа:', reply_markup=markup)

    def get_unit_card(self, frac):

    # Функция получения карточки юнита из вызова по ключу фракции и персонажа
		
        user_id = self.message.from_user.id
        url = str(d_hydro[frac][self.message.text])
        self.bot.send_photo(user_id, url)

    def get_drug_card(self):

    # Функция получения карт усилителей по ключу

        user_id = self.message.from_user.id
        url = str(d_drugs[self.message.text])
        self.bot.send_photo(user_id, url)

    def get_leaders(self):

    # Функция создания меню тактический карт из вызова по ключу лидера

        user_id = self.message.from_user.id
        menu = list(d_leaders[self.message.text])
        markup = create_menu_tactics(menu)
        self.bot.send_message(user_id, 'Выбери карточку:', reply_markup=markup)	

    def get_leaders_card(self, card):	

    # Функция получения карточки лидера из вызова по ключу лидера и его карточки

        user_id = self.message.from_user.id
        url = str(d_leaders[card][self.message.text])
        self.bot.send_photo(user_id, url)