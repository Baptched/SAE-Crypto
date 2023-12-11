"""
Module permettant de faire des tests unitaires sur la fonction decrypte_substitution
pour le message numéro 2
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from message2 import decrypte_substitution
import constantes as const


class TestDecrypteSubstitution(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la fonction decrypte_substitution

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_decrypte_substitution_lettre_minuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec des lettres minuscules
        """
        self.assertEqual(decrypte_substitution("a", const.CLE_SUBSTITUTION),
                         "r")
        self.assertEqual(decrypte_substitution("ab", const.CLE_SUBSTITUTION),
                         "rm")
        self.assertEqual(decrypte_substitution("abc", const.CLE_SUBSTITUTION),
                         "rmu")

    def test_decrypte_substitution_lettre_majuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec des lettres majuscules
        """
        self.assertEqual(decrypte_substitution("A", const.CLE_SUBSTITUTION),
                         "R")
        self.assertEqual(decrypte_substitution("AB", const.CLE_SUBSTITUTION),
                         "RM")
        self.assertEqual(decrypte_substitution("ABC", const.CLE_SUBSTITUTION),
                         "RMU")

    def test_decrypte_substitution_caractere_special(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec des caractères spéciaux
        """
        self.assertEqual(decrypte_substitution(" ", const.CLE_SUBSTITUTION),
                         " ")
        self.assertEqual(decrypte_substitution("  ", const.CLE_SUBSTITUTION),
                         "  ")
        self.assertEqual(decrypte_substitution("   ", const.CLE_SUBSTITUTION),
                         "   ")

    def test_decrypte_substitution_chiffre(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec des chiffres
        """
        self.assertEqual(decrypte_substitution("1", const.CLE_SUBSTITUTION),
                         "1")
        self.assertEqual(decrypte_substitution("12", const.CLE_SUBSTITUTION),
                         "12")
        self.assertEqual(decrypte_substitution("123", const.CLE_SUBSTITUTION),
                         "123")

    def test_decrypte_substitution_cle_vide(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec une clé vide
        """
        self.assertEqual(decrypte_substitution("a", ""), None)
        self.assertEqual(decrypte_substitution("ab", ""), None)
        self.assertEqual(decrypte_substitution("abc", ""), None)

    def test_decrypte_substitution_cle_trop_courte(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec une clé trop courte
        """
        self.assertEqual(decrypte_substitution("a", "a"), None)
        self.assertEqual(decrypte_substitution("ab", "ab"), None)
        self.assertEqual(decrypte_substitution("abc", "abc"), None)

    def test_decrypte_substitution_cle_trop_longue(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec une clé trop longue
        """
        self.assertEqual(
            decrypte_substitution("a", "abcdefghijklmnopqrstuvwxzaddyz"), None)
        self.assertEqual(
            decrypte_substitution("ab", "abcdefghijklmnopqrstuvwxydzdzdz"),
            None)
        self.assertEqual(
            decrypte_substitution("abc", "abcdefghijklmnopqrstuvwxyzaszad"),
            None)

    def test_decrypte_substitution_message_2(self):
        """
        Fonction permettant de tester la fonction decrypte_substitution
        avec le message 2 décrypté
        """
        self.assertEqual(
            decrypte_substitution(const.MESSAGE_3, const.CLE_SUBSTITUTION),
            const.MOT_2)
