import random

from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot import types

from conf import token
import db_users
from dyct import d_commands, d_hydro, d_mis, d_set, d_drugs, d_leaders, d_msg
from func import create_menu, create_main_menu, GetCards


bot = AsyncTeleBot(token)

text_messages = {
    'start':
        u'Приветствую тебя, {name}!\n\n'
        u'Навигация по ГЛАВНОМУ МЕНЮ:\n\n'
        u'|ФРАКЦИИ| - навигация по персонажам фракций\n'
        u'|УСИЛИТЕЛИ| - получить карты усилителей\n'
        u'|ТАКТИКИ| - получить карты тактик\n'
        u'|СКАЧАТЬ| - скачать актуальные правила, FAQ и т.д.\n'
        u'|РАНДОМАЙЗЕР| - случайный выбор миссии и расстановки\n\n'
        u'кнопка |Главное Меню| снизу',

    'help':
        u'С предложениям по улучшению, а также об ошибках\n'
        u'просьба писать - https://discord.gg/eaWJFDdddM\n',

    'destroy':
        d_msg
}


# Меню основных команд бота

@bot.message_handler(commands=['start'])
async def get_start(message):
    await db_users.create_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное Меню')
    await bot.send_message(message.from_user.id, text_messages['start'].format(name=message.from_user.first_name),
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
async def get_start(message):
    await db_users.create_user(message)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Главное Меню')
    await bot.send_message(message.from_user.id, text_messages['help'], reply_markup=markup)


@bot.message_handler(commands=['destroy'])
async def get_start(message):
    await db_users.create_user(message)
    animation = 'https://media.giphy.com/media/26n6XC8EYdrzRniWQ/giphy.gif'
    await bot.send_message(message.from_user.id, text_messages['destroy'])
    await bot.send_animation(message.from_user.id, animation)


@bot.message_handler(content_types=['text'])
async def get_nav(message):
    await db_users.create_user(message)

    # Функция навигации по фракциям и персонажам

    if message.text != '':
        # Получить основные команды
        for key, value in d_commands.items():
            if message.text == key:
                await eval(value)

    if message.text in list(d_drugs):
        # Получить список усилителей
        await get_drugs_all(message)
    if message.text in list(d_leaders):
        # Получить список лидеров фракций
        await get_all_leaders(message)
    if message.text in list(d_hydro):
        # Получить персонажей фракции
        await get_all_units(message)
    if message.text in list(d_leaders['Правительство - Дэвис']):
        # Получить карточки Дэвиса
        await get_devis(message)
    if message.text in list(d_leaders['Синдикат - Винсент']):
        # Получить карточки Винсента
        await get_vinsent(message)
    if message.text in list(d_leaders['Синдикат - Заводила']):
        # Получить карточки Заводилы
        await get_firebrand(message)
    if message.text in list(d_leaders['Нисимура - Тэцуи']):
        # Получить карточки Тэцуи
        await get_tetsui(message)
    if message.text in list(d_hydro['Правительство']):
        # Получить карточки персонажей Правительства
        await get_gov(message)
    if message.text in list(d_hydro['Синдикат']):
        # Получить карточки персонажей Синдиката
        await get_syn(message)
    if message.text in list(d_hydro['Нисимура']):
        # Получить карточки персонажей Нисимуры
        await get_nis(message)


async def get_menu(message):
    # Функция главного меню

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Фракции', 'Усилители', 'Тактики')
    markup.row('Скачать', 'Рандомайзер')
    await bot.send_message(message.from_user.id, 'Выбери категорию:', reply_markup=markup)


async def get_downloads(message):
    # Функция меню загрузок

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Правила', 'Гидропедия', 'FAQ')
    markup.row('Главное Меню')
    await bot.send_message(message.from_user.id, 'Выбери категорию:', reply_markup=markup)


async def get_rules(message):
    # Функция загрузки правил

    url = 'https://drive.google.com/uc?export=download&id=1O0gneqLQzETQ-Mn8SqsXqe0z7LY9vwIO'
    await bot.send_message(message.from_user.id, 'документ загружается...')
    await bot.send_document(message.from_user.id, url)


async def get_pedia(message):
    # Функции загрузки гидропедии

    url = 'https://drive.google.com/uc?export=download&id=1WZHJQJ3NEDtm27jb1VMNkBWyT5wp2zZO'
    await bot.send_message(message.from_user.id, 'документ загружается...')
    await bot.send_document(message.from_user.id, url)


async def get_faq(message):
    # Функции загрузки гидропедии

    url = 'https://drive.google.com/uc?export=download&id=1XAxfrmShesX-pzJdVsKdVCPEFCvNwbnK'
    await bot.send_message(message.from_user.id, 'документ загружается...')
    await bot.send_document(message.from_user.id, url)


async def get_drugs(message):
    # Функция навигации по усилителям

    menu = list(d_drugs.keys())
    markup = create_main_menu(menu)
    await bot.send_message(message.from_user.id, 'Выбери усилитель:', reply_markup=markup)


async def get_drugs_all(message):
    # Функция возвращает карты усилителей

    drugs = GetCards(bot, message)
    await drugs.get_drug_card()


async def get_tactics(message):
    # Функция навигации по тактикам лидеров фракций

    menu = list(d_leaders.keys())
    markup = create_main_menu(menu)
    await bot.send_message(message.from_user.id, 'Выбери лидера:', reply_markup=markup)


async def get_all_leaders(message):
    # Функция возвращает список всех карт Лидеров

    l_cards = GetCards(bot, message)
    await l_cards.get_leaders()


async def get_devis(message):
    # Функция возвращает карты Дэвиса

    devis = GetCards(bot, message)
    await devis.get_leaders_card('Правительство - Дэвис')


async def get_vinsent(message):
    # Функция возвращает карты Винсента

    vinsent = GetCards(bot, message)
    await vinsent.get_leaders_card('Синдикат - Винсент')


async def get_firebrand(message):
    # Функция возвращает карты Заводилы

    firebrand = GetCards(bot, message)
    await firebrand.get_leaders_card('Синдикат - Заводила')


async def get_tetsui(message):
    # Функция возвращает карты Тэцуи

    tetsui = GetCards(bot, message)
    await tetsui.get_leaders_card('Нисимура - Тэцуи')


async def get_fractions(message):
    # Функция навигации по фракциям

    menu = list(d_hydro.keys())
    markup = create_menu(menu)
    await bot.send_message(message.from_user.id, 'Выбери фракцию:', reply_markup=markup)


async def get_random(message):
    # Функция случайного выбора миссий и расстановок

    random_mis = random.choice(list(d_mis.values()))
    random_set = random.choice(list(d_set.values()))
    await bot.send_photo(message.from_user.id, random_mis)
    await bot.send_photo(message.from_user.id, random_set)


async def get_all_units(message):
    # Функция навигации по персонажам всех Фракций

    units = GetCards(bot, message)
    await units.get_units()


async def get_syn(message):
    # Функция возвращает карты персонажей Синдиката

    syn = GetCards(bot, message)
    await syn.get_unit_card('Синдикат')


async def get_nis(message):
    # Функция возвращает карты персонажей Нисимуры

    nis = GetCards(bot, message)
    await nis.get_unit_card('Нисимура')


async def get_gov(message):
    # Функция возвращает карты персонажей Правительства

    gov = GetCards(bot, message)
    await gov.get_unit_card('Правительство')


asyncio.run(bot.polling(none_stop=True))
