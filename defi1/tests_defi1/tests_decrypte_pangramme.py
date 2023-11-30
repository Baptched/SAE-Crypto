"""
Module permettant de faire des tests unitaires sur la fonction decrypte_pangramme
pour le message numéro 2
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from message2 import decrypte_pangramme
import constantes as const


class TestDecryptePangramme(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la fonction decrypte_pangramme

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_decrypte_pangramme_lettre_minuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_pangramme 
        avec des lettres minuscules
        """
        self.assertEqual(decrypte_pangramme("a"), "a")
        self.assertEqual(decrypte_pangramme("ab"), "ab")
        self.assertEqual(decrypte_pangramme("abc"), "abc")

    def test_decrypte_pangramme_lettre_majuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_pangramme 
        avec des lettres majuscules
        """
        self.assertEqual(decrypte_pangramme("A"), "A")
        self.assertEqual(decrypte_pangramme("AB"), "AB")
        self.assertEqual(decrypte_pangramme("ABC"), "ABC")

    def test_decrypte_pangramme_caractere_special(self):
        """
        Fonction permettant de tester la fonction decrypte_pangramme 
        avec des caractères spéciaux
        """
        self.assertEqual(decrypte_pangramme(" "), "")
        self.assertEqual(decrypte_pangramme("  "), "")
        self.assertEqual(decrypte_pangramme("   "), "")

    def test_decrypte_pangramme_chiffre(self):
        """
        Fonction permettant de tester la fonction decrypte_pangramme 
        avec des chiffres
        """
        self.assertEqual(decrypte_pangramme("1"), "")
        self.assertEqual(decrypte_pangramme("12"), "")
        self.assertEqual(decrypte_pangramme("123"), "")

    def test_decrypte_pangramme_message_2(self):
        """
        Fonction permettant de tester la fonction decrypte_pangramme
        avec le message 2 decrypte
        """
        self.assertEqual(decrypte_pangramme(const.MESSAGE_2_DECRYPTE),
                         const.CLE_SUBSTITUTION)
