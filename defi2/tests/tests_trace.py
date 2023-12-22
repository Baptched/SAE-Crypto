"""
Module de tests pour la recherche des messages cachés dans les images
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from analyse_trace import decrypte_message_alice_et_bob, retrouve_messages_trace
from steganographie import retrouve_cle


class TestTrace(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la
    recherche des messages cachés dans les images
    """

    def test_decrypte_message_alice_et_bob(self):
        """
        Fonction qui test decrypte les messages d'Alice et Bob dans le trace .cap
        """
        les_messages = retrouve_messages_trace()
        liste_messages: list[str] = decrypte_message_alice_et_bob(
            retrouve_cle(), les_messages)
        self.assertIsInstance(liste_messages, list)
        self.assertEqual(liste_messages[0], "La crypto c'est trop bien!")
        self.assertEqual(liste_messages[1], "Je suis complètement d'accord!")
