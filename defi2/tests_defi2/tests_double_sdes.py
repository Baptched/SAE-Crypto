"""
Module de tests pour le double SDES
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from double_sdes import crypte_double_sdes, decrypte_double_sdes, cassage_brutal, cassage_astucieux


class TestSDES(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du SDES

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_crypte_double_sdes(self):
        """
        Fonction permettant de tester la fonction crypte_double_sdes
        """
        self.assertEqual(crypte_double_sdes("Bonjour", 0b00000000, 0b00000000),
                         "Bonjour")
        self.assertEqual(crypte_double_sdes("Bonjour", 0b11100011, 0b00000000),
                         "ÎFâQF±\x1a")
        self.assertEqual(
            crypte_double_sdes("Je m'appelle Baptiste", 0b00000000,
                               0b11100011),
            "×²\x13(¾¶--²¹¹²\x13Õ¶-\x81þê\x81²")

    def test_decrypte_double_sdes(self):
        """
        Fonction permettant de tester la fonction decrypte_double_sdes
        """
        self.assertEqual(
            decrypte_double_sdes("Bonjour", 0b00000000, 0b00000000), "Bonjour")
        self.assertEqual(
            decrypte_double_sdes("ÎFâQF±\x1a", 0b11100011, 0b00000000),
            "Bonjour")
        self.assertEqual(
            decrypte_double_sdes("×²\x13(¾¶--²¹¹²\x13Õ¶-\x81þê\x81²",
                                 0b00000000, 0b11100011),
            "Je m'appelle Baptiste")

    def test_cassage_brutal(self):
        """
        Fonction permettant de tester la fonction cassage_brutal
        """
        message_clair = "Je m'appelle Baptiste"
        message_crypte = crypte_double_sdes(message_clair, 0b00000000,
                                            0b11100011)
        self.assertEqual(
            cassage_brutal(message_clair, message_crypte)[0:2],
            (0b00000000, 0b11100011))
        message_clair = "Bonjour"
        message_crypte = crypte_double_sdes(message_clair, 0b00000000,
                                            0b00000000)
        self.assertEqual(
            cassage_brutal(message_clair, message_crypte)[0:2],
            (0b00000000, 0b00000000))
        message_clair = "Bonjour"
        message_crypte = crypte_double_sdes(message_clair, 0b11100011,
                                            0b00000000)
        self.assertEqual(
            cassage_brutal(message_clair, message_crypte)[0:2],
            (0b11100011, 0b00000000))

    def test_cassage_astucieux(self):
        """
        Fonction permettant de tester la fonction cassage_astucieux
        """
        message_clair = "Je m'appelle Baptiste"
        message_crypte = crypte_double_sdes(message_clair, 0b00000000,
                                            0b11100011)
        self.assertEqual(
            cassage_astucieux(message_clair, message_crypte)[0:2],
            (0b00000000, 0b11100011))
        message_clair = "Bonjour"
        message_crypte = crypte_double_sdes(message_clair, 0b00000000,
                                            0b00000000)
        self.assertEqual(
            cassage_astucieux(message_clair, message_crypte)[0:2],
            (0b00000000, 0b00000000))
        message_clair = "Bonjour"
        message_crypte = crypte_double_sdes(message_clair, 0b11100011,
                                            0b00000000)
        self.assertEqual(
            cassage_astucieux(message_clair, message_crypte)[0:2],
            (0b11100011, 0b00000000))
