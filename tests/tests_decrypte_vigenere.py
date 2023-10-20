"""
Module permettant de faire des tests unitaires sur la fonction decrypte_vigenere
pour le message numéro 2
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from message2 import decrypte_vigenere
import constantes as const


class TestDecrypteVigenere(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la fonction decrypte_vigenere

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_decrypte_vigenere_lettre_minuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere 
        avec des lettres minuscules
        """
        self.assertEqual(decrypte_vigenere("a", "a"), "A")
        self.assertEqual(decrypte_vigenere("a", "y"), "C")
        self.assertEqual(decrypte_vigenere("a", "q"), "K")

    def test_decrypte_vigenere_lettre_majuscule(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere 
        avec des lettres majuscules
        """
        self.assertEqual(decrypte_vigenere("A", "A"), "A")
        self.assertEqual(decrypte_vigenere("A", "U"), "G")
        self.assertEqual(decrypte_vigenere("A", "K"), "Q")

    def test_decrypte_vigenere_caractere_special(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere 
        avec des caractères spéciaux
        """
        self.assertEqual(decrypte_vigenere(" ", " "), " ")
        self.assertEqual(decrypte_vigenere(" ", "a"), " ")
        self.assertEqual(decrypte_vigenere(" ", "z"), " ")

    def test_decrypte_vigenere_chiffre(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere 
        avec des chiffres
        """
        self.assertEqual(decrypte_vigenere("1", "1"), "1")
        self.assertEqual(decrypte_vigenere("1", "2"), "1")
        self.assertEqual(decrypte_vigenere("1", "3"), "1")

    def test_decrypte_vigenere_cle_taille_differente(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere 
        avec une clé de taille différente de la taille du message
        """
        self.assertEqual(decrypte_vigenere("a", ""), "A")
        self.assertEqual(decrypte_vigenere("a", "ab"), "A")

    def test_decrypte_vigenere_message_crypter(self):
        """
        Fonction permettant de tester la fonction decrypte_vigenere
        avec le message crypté numéro 2
        """
        self.assertEqual(decrypte_vigenere(const.MESSAGE_2, const.MOT_1),
                         const.MESSAGE_2_DECRYPTE)
