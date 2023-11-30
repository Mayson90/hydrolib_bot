import unittest

from bot import get_menu


def main_menu(menu):
    if menu == 'Главное Меню':
        print("[ERROR] Back to 'Главное Меню' in main_menu ")
    else:
        return True


class TestBotMenu(unittest.TestCase):
    def test_bot_back_to_main_menu(self):
        menu = get_menu('Главное Меню')
        assert main_menu(menu)
