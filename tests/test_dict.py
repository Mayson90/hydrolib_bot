import sys
sys.path.append("..")

import unittest
import requests

import dict


class TestDictLinks(unittest.TestCase):
    def test_main_links(self):
        d = dict.d_hydro
        for key, values in d.items():
                for value in values.values():
                    resp = requests.get(value)
                    self.assertEqual(resp.status_code, 200)
                
    def test_missions_links(self):
        d = dict.d_mis
        for key, value in d.items():
            resp = requests.get(value)
            self.assertEqual(resp.status_code, 200)
    
    def test_setup_links(self):
        d = dict.d_set
        for key, value in d.items():
            resp = requests.get(value)
            self.assertEqual(resp.status_code, 200)

    def test_booster_links(self):
        d = dict.d_drugs
        for key, value in d.items():
            resp = requests.get(value)
            self.assertEqual(resp.status_code, 200)
    