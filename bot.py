import telebot
import random
import config
import db_users

from telebot import types
from func import create_menu, create_main_menu, create_menu_detail, items
from dyct import d_hydro, d_mis, d_set, d_drugs, d_leaders


bot = telebot.TeleBot(config.token)

text_messages = {
    'start':
        u'Приветствую тебя, {name}!\n\n'
        u'Навигация по ГЛАВНОМУ МЕНЮ:\n\n'
        u'|ФРАКЦИИ| - навигация по перснонажам фракций\n'
        u'|УСИЛИТЕЛИ| - получить карты усилителей\n'
        u'|ТАКТИКИ| - получить карты тактик\n'
        u'|ПРАВИЛА| - скачать актуальные правила\n'
        u'|РАНДОМАЙЗЕР| - случайный выбор миссии и расстановки\n\n'
        u'кнопка |Главное Меню| снизу',
    
    'help':
        u'С предложениям по улучшению, а также об ошибках\n'
        u'просьба писать - https://vk.com/33ud934nf\n',

    'destroy':
        u'011011100110111101110111001000000110100100100000011000010110110100100000011000100110010101100011011011110110110101100101001000000110010001100101011000010111010001101000001000000111010001101000011001010010000001100100011001010111001101110100011100100110111101111001011001010111001000100000011011110110011000100000011101110110111101110010011011000110010001110011\n'
}

# Меню основных комманд бота

@bot.message_handler(commands=['start'])
def get_start(message):
    db_users.create_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное Меню')
    bot.send_message(message.from_user.id, text_messages['start'].format(name=message.from_user.first_name), reply_markup=markup)

@bot.message_handler(commands=['help'])
def get_start(message):
    db_users.create_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное Меню')
    bot.send_message(message.from_user.id, text_messages['help'], reply_markup=markup)

@bot.message_handler(commands=['destroy'])
def get_start(message):
    db_users.create_user(message)
    animation = 'https://media.giphy.com/media/26n6XC8EYdrzRniWQ/giphy.gif'
    bot.send_message(message.from_user.id, text_messages['destroy'])
    bot.send_animation(message.from_user.id, animation)

@bot.message_handler(content_types=['text'])
def get_nav(message):
    db_users.create_user(message)

# Функция навигации по фракциям и персонажам

    if message.text == 'Главное Меню':
        get_menu(message)

    if message.text == 'Фракции':
        get_fractions(message)
		
    elif message.text == 'Усилители':
        get_drugs(message)

    elif message.text == 'Тактики':
        get_tactics(message)

    elif message.text == 'Правила':
        get_rules(message)

    elif message.text == 'Гидропедия':
        get_pedia(message)    

    elif message.text == 'Рандомайзер':
        get_random(message)	

    elif message.text == 'назад - Лидеры':
        get_tactics(message)	

    elif message.text == 'назад - Фракции':
        get_fractions(message)		

    elif message.text in list(d_drugs):
    # Получить список усилителей
        get_drugs_all(message)

    elif message.text in list(d_leaders):
    # Получить список лидеров фракций
        get_all_leaders(message)

    elif message.text in list(d_leaders['Правительство - Дэвис']):
    # Получить карточки Дэвиса
        get_devis(message)		

    elif message.text in list(d_leaders['Синдикат - Винсент']):
    # Получить карточки Винсента
        get_vinsent(message)	

    elif message.text in list(d_leaders['Синдикат - Заводила']):
    # Получить карточки Заводилы
        get_firebrand(message)

    elif message.text in list(d_leaders['Нисимура - Тэцуи']):
    # Получить карточки Тэцуи
        get_tetsui(message)	

    elif message.text in list(d_hydro):
    # Получить юнитов фракции
        get_all_units(message)			

    elif message.text in list(d_hydro['Правительство']):
    # Получить карточки юнитов Правительства
        get_gov(message)
	
    elif message.text in list(d_hydro['Синдикат']):
    # Получить карточки юнитов Синдиката
        get_syn(message)

    elif message.text in list(d_hydro['Нисимура']):
    # Получить карточки юнитов Нисимуры
        get_nis(message)


def get_menu(message):

# Функция главного меню

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Фракции', 'Усилители', 'Тактики')
    markup.row('Правила', 'Гидропедия', 'Рандомайзер')
    bot.send_message(message.from_user.id, 'Выбери категорию:', reply_markup=markup)

def get_rules(message):

# Функция загрузки правил
	
    url = 'https://drive.google.com/uc?export=download&id=1O0gneqLQzETQ-Mn8SqsXqe0z7LY9vwIO'
    bot.send_message(message.from_user.id, 'документ загружается...')
    bot.send_document(message.from_user.id, url)

def get_pedia(message):

# Функции загрузки гидропедии

    url = 'https://drive.google.com/uc?export=download&id=1WZHJQJ3NEDtm27jb1VMNkBWyT5wp2zZO'
    bot.send_message(message.from_user.id, 'документ загружается...')
    bot.send_document(message.from_user.id, url)

def get_drugs(message):

# Функция навигации по усилителям

    menu = list(d_drugs.keys())
    markup = create_main_menu(menu)
    bot.send_message(message.from_user.id, 'Выбери усилитель:', reply_markup=markup)

def get_drugs_all(message):

# Функция возвращает карты усилителей

    drugs = items(bot, message)
    drugs.get_drug_card()

def get_tactics(message):

# Функция навигации по тактикам лидеров фракций

    menu = list(d_leaders.keys())
    markup = create_main_menu(menu)
    bot.send_message(message.from_user.id, 'Выбери лидера:', reply_markup=markup)

def get_all_leaders(message):

# Функция возвращает список всех карт Лидеров

    l_cards = items(bot, message)
    l_cards.get_leaders()

def get_devis(message):

# Функция возвращает карты Дэвиса

    devis = items(bot, message)
    devis.get_leaders_card('Правительсвто - Дэвис')

def get_vinsent(message):

# Функция возвращает карты Винсента

    vinsent = items(bot, message)
    vinsent.get_leaders_card('Синдикат - Винсент')

def get_firebrand(message):

# Функция возвращает карты Заводилы

    firebrand = items(bot, message)
    firebrand.get_leaders_card('Синдикат - Заводила')

def get_tetsui(message):

# Функция возвращает карты Тэцуи

    tetsui = items(bot, message)
    tetsui.get_leaders_card('Нисимура - Тэцуи')			

def get_fractions(message):

# Функция навигации по фракциям

    menu = list(d_hydro.keys())
    markup = create_menu(menu)
    bot.send_message(message.from_user.id, 'Выбери фракцию:', reply_markup=markup)

def get_random(message):

# Функция рандомного выбора миссий и расстановок

    random_mis = random.choice(list(d_mis.values()))
    random_set = random.choice(list(d_set.values()))
    bot.send_photo(message.from_user.id, random_mis)
    bot.send_photo(message.from_user.id, random_set)

def get_all_units(message):

# Функция навигации по персонажам всех Фракций

    units = items(bot, message)
    units.get_units()

def get_syn(message):

# Функция возвращает карты юнитов Синдиката

    syn = items(bot, message)
    syn.get_unit_card('Синдикат')

def get_nis(message):

# Функция возвращает карты юнитов Нисимуры

    nis = items(bot, message)
    nis.get_unit_card('Нисимура')

def get_gov(message):

# Функция возвращает карты юнитов Правительства
	
    gov = items(bot, message)
    gov.get_unit_card('Правительство')

bot.polling(none_stop=True)