"""
Module permettant de faire des tests unitaires sur la fonction decrypte_cesar
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from message1 import decrypte_cesar
import constantes as const


class TestDecrypteCesar(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la fonction decrypte_cesar

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_decrypte_cesar_lettre_minuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar 
        avec des lettres minuscules
        """
        self.assertEqual(decrypte_cesar("a", 0), "a")
        self.assertEqual(decrypte_cesar("a", 3), "x")
        self.assertEqual(decrypte_cesar("a", 22), "e")

    def test_decrypte_cesar_lettre_majuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar 
        avec des lettres majuscules
        """
        self.assertEqual(decrypte_cesar("A", 0), "A")
        self.assertEqual(decrypte_cesar("A", 12), "O")
        self.assertEqual(decrypte_cesar("A", 32), "U")

    def test_decrypte_cesar_caractere_special(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar 
        avec des caractères spéciaux
        """
        self.assertEqual(decrypte_cesar(" ", 0), " ")
        self.assertEqual(decrypte_cesar(" ", 5), " ")
        self.assertEqual(decrypte_cesar(" ", 12), " ")

    def test_decrypte_cesar_chiffre(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar 
        avec des chiffres
        """
        self.assertEqual(decrypte_cesar("1", 0), "1")
        self.assertEqual(decrypte_cesar("1", 5), "1")
        self.assertEqual(decrypte_cesar("1", 12), "1")

    def test_decrypte_cesar_phrase(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar 
        avec des phrases
        """
        self.assertEqual(decrypte_cesar("A b C", 0), "A b C")
        self.assertEqual(decrypte_cesar("xy z", 5), "st u")
        self.assertEqual(decrypte_cesar("S B D", 12), "G P R")

    def test_decrypte_cesar_message_crypter(self):
        """
        Fonction permettant de tester la fonction decrypte_cesar
        avec le message crypté numéro 1
        """
        self.assertEqual(decrypte_cesar(const.MESSAGE_1, 12),
                         const.MESSAGE_1_DECRYPTE)
