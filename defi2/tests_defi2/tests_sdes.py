"""
Module de tests pour le SDES
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from sdes import crypter, decrypt


class TestSDES(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du SDES

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_crypter(self):
        """
        Fonction permettant de tester la fonction crypter
        """
        self.assertEqual(crypter(0b0000000000, 0b10101010), 0b00010001)
        self.assertEqual(crypter(0b1110001110, 0b10101010), 0b11001010)
        self.assertEqual(crypter(0b1110001110, 0b01010101), 0b01110000)
        self.assertEqual(crypter(0b1111111111, 0b10101010), 0b00000100)

    def test_decrypter(self):
        """
        Fonction permettant de tester la fonction decrypter
        """
        self.assertEqual(decrypt(0b0000000000, 0b00010001), 0b10101010)
        self.assertEqual(decrypt(0b1110001110, 0b11001010), 0b10101010)
        self.assertEqual(decrypt(0b1110001110, 0b01110000), 0b01010101)
        self.assertEqual(decrypt(0b1111111111, 0b00000100), 0b10101010)
