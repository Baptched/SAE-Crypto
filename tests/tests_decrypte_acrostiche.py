"""
Module permettant de faire des tests unitaires sur la fonction decrypte_acrostiche
pour le message numéro 1
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from message1 import decrypte_acrostiche
import constantes as const


class TestDecrypteAcrostiche(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la fonction decrypte_acrostiche

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_decrypte_acrostiche_lettre_minuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des lettres minuscules
        """
        self.assertEqual(decrypte_acrostiche("a"), "a")
        self.assertEqual(decrypte_acrostiche("ab"), "a")
        self.assertEqual(decrypte_acrostiche("abc"), "a")

    def test_decrypte_acrostiche_lettre_majuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des lettres majuscules
        """
        self.assertEqual(decrypte_acrostiche("A"), "A")
        self.assertEqual(decrypte_acrostiche("AB"), "A")
        self.assertEqual(decrypte_acrostiche("ABC"), "A")

    def test_decrypte_acrostiche_caractere_special(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des caractères spéciaux
        """
        self.assertEqual(decrypte_acrostiche(" "), " ")
        self.assertEqual(decrypte_acrostiche("  "), " ")
        self.assertEqual(decrypte_acrostiche("   "), " ")

    def test_decrypte_acrostiche_chiffre(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des chiffres
        """
        self.assertEqual(decrypte_acrostiche("1"), "1")
        self.assertEqual(decrypte_acrostiche("12"), "1")
        self.assertEqual(decrypte_acrostiche("123"), "1")

    def test_decrypte_acrostiche_phrase(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des phrases
        """
        self.assertEqual(decrypte_acrostiche("a b"), "a")
        self.assertEqual(decrypte_acrostiche("ab cd"), "a")
        self.assertEqual(decrypte_acrostiche("abc def"), "a")

    def test_decrypte_acrostiche_lignes(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec des lignes
        """
        self.assertEqual(decrypte_acrostiche("a\nb"), "ab")
        self.assertEqual(decrypte_acrostiche("ab\ncd"), "ac")
        self.assertEqual(decrypte_acrostiche("abc\ndef"), "ad")

    def test_decrypte_acrostiche_message_1(self):
        """
        Fonction permettant de tester la fonction decrypte_acrostiche 
        avec le message 1 décrypté
        """
        self.assertEqual(decrypte_acrostiche(const.MESSAGE_1_DECRYPTE),
                         const.MOT_1)
