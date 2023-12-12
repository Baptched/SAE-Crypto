"""
Module de tests pour le AES
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from aes import crypte_aes, decrypte_aes


class TestAES(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du AES

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_crypte_aes(self):
        """
        Fonction permettant de tester la fonction crypte_aes
        """
        self.assertIsInstance(crypte_aes("Bonjour", 0b00000000), str)
        self.assertIsInstance(crypte_aes("Bonjour", 127), str)

    def test_decrypte_aes(self):
        """
        Fonction permettant de tester la fonction decrypte_aes
        """
        message_crypter = crypte_aes("Bonjour", 0b00000000)
        self.assertIsInstance(decrypte_aes(message_crypter, 0b00000000), str)
        self.assertEqual(decrypte_aes(message_crypter, 0b00000000), "Bonjour")
