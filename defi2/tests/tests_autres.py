"""
Module de tests pour le module autres
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'src'))

from autres import genere_key_10_bits, genere_key_256_bits


class TestAutres(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du module autres

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_genere_key_10_bits(self):
        """
        Fonction permettant de tester la fonction genere_key_10_bits
        """
        key = genere_key_10_bits()
        self.assertTrue(0 <= key <= 2**10)

    def test_genere_key_256_bits(self):
        """
        Fonction permettant de tester la fonction genere_key_256_bits
        """
        key = genere_key_256_bits()
        self.assertTrue(0 <= key <= 2**256)
