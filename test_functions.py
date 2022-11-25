# -*- coding: utf-8 -*-
import unittest
from functions import *
class TestFunctions(unittest.TestCase):
    def test_crypter(self):
        self.assertEqual(crypter("BONJOUR", "FEU"),"GSHOSOW")
        self.assertNotEqual(crypter('bonjour', "feu"),"gshosow")
        self.assertEqual(crypter('BONJOUR', "feu"),"GSHOSOW")
        self.assertEqual(crypter('bonjour', "FEU"),"GSHOSOW")
        self.assertEqual(crypter('bonjour', "feu"),"GSHOSOW")
        self.assertEqual(crypter("JE VAIS BIEN", "AND"),"JR YAVV BVHN")
        self.assertNotEqual(crypter("JE VAIS BIEN","FEU"),"JR YAVV BVHN")
        self.assertEqual(crypter("BONJOUR","AAA"),"BONJOUR")
        self.assertEqual(crypter("SALUT A TOUS", "FOUR"),"XOFLY O NFZG")
        self.assertEqual(crypter("message", "avalon"),"MZSDOTE")
if __name__=='__main__':
    unittest.main()
