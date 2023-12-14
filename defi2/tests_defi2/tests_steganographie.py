"""
Module de tests pour la stéganographie sur les images
"""

import sys
import os
import unittest

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
sys.path.append(os.path.join(ROOT, "src"))

from steganographie import meme_image, retrouve_cle


class TestSteganographie(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires de la stéganographie
    """

    def test_meme_image(self):
        """
        Fonction permettant de tester la fonction meme_image
        """
        self.assertFalse(
            meme_image("sujet/rossignol1.bmp", "sujet/rossignol2.bmp"))
        self.assertTrue(
            meme_image("sujet/rossignol1.bmp", "sujet/rossignol1.bmp"))
        self.assertTrue(
            meme_image("sujet/rossignol2.bmp", "sujet/rossignol2.bmp"))

    def test_retrouve_cle(self):
        """
        Fonction permettant de tester la fonction retrouve_cle
        """
        self.assertEqual(
            retrouve_cle(),
            "1110011101101101001100010011111110010010101110011001000001001100")
