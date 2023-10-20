"""
Module permettant de faire des tests unitaires sur le main
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from main import affichage_message_numero_1, affichage_message_numero_2


class TestMain(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du main

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_affichage_message_numero_1(self):
        """
        Fonction permettant de tester la méthode affichage_message_numero_1
        """
        self.assertIsNone(affichage_message_numero_1())

    def test_affichage_message_numero_2(self):
        """
        Fonction permettant de tester la méthode affichage_message_numero_2
        """
        self.assertIsNone(affichage_message_numero_2())
