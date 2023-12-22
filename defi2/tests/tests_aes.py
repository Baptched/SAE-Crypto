"""
Module de tests pour le AES
"""

import sys
import os
import unittest
from Crypto.Util.Padding import pad
from Crypto.Cipher import AES

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(os.path.join(ROOT, 'src'))

from aes import crypte_aes, decrypte_aes, crypte_aes_cbc, cassage_brutal_aes, decrypte_aes_cbc, estimation_temps_cassage_brutal
import constantes2 as c


class TestAES(unittest.TestCase):
    """
    Classe permettant de faire les tests unitaires du AES

    Args:
        unittest (unittes): La classe de base pour les tests unitaires
    """

    def test_crypte_aes(self):
        """
        Fonction permettant de tester la fonction crypte_aes
        """
        self.assertIsInstance(crypte_aes('Bonjour', 0b00000000), str)
        self.assertIsInstance(crypte_aes('Bonjour', 127), str)

    def test_decrypte_aes(self):
        """
        Fonction permettant de tester la fonction decrypte_aes
        """
        message_crypter = crypte_aes('Bonjour', 0b00000000)
        self.assertIsInstance(decrypte_aes(message_crypter, 0b00000000), str)
        self.assertEqual(decrypte_aes(message_crypter, 0b00000000), 'Bonjour')

    def test_crypte_aes_cbc(self):
        """
        Fonction permettant de tester la fonction crypte_aes_cbc
        """
        self.assertIsInstance(
            crypte_aes_cbc(0b00000110.to_bytes(16, 'big'),
                           0b00000110.to_bytes(c.NOMBRE_OCTETS_CLE, 'big'),
                           0b00000110.to_bytes(c.NOMBRE_OCTETS_CLE, 'big')),
            bytes)

    def test_crypte_aes_cbc_invalid_key(self):
        """
        Fonction permettant de tester la fonction crypte_aes_cbc avec une clé invalide
        """
        iv = b'\x00' * 16
        key = b'\x01' * 15
        plaintext = b'Test message'
        with self.assertRaises(Exception):
            crypte_aes_cbc(iv, plaintext, key)

    def test_decrypte_aes_cbc(self):
        """
        Fonction permettant de tester la fonction decrypte_aes_cbc
        """
        iv = b'\x00' * 16
        key = b'\x01' * 16
        plaintext = b'Test message'
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        decrypted_text = decrypte_aes_cbc(iv, ciphertext, key)
        self.assertEqual(decrypted_text, plaintext.decode('utf-8'))

    def test_decrypte_aes_cbc_invalid_key(self):
        """
        Fonction permettant de tester la fonction decrypte_aes_cbc avec une clé invalide
        """
        iv = b'\x00' * 16
        key = b'\x01' * 15  # Clé invalide
        ciphertext = b'\x00' * 16
        with self.assertRaises(Exception):
            decrypte_aes_cbc(iv, ciphertext, key)

    def test_decrypte_aes_cbc_invalid_ciphertext(self):
        """
        Fonction permettant de tester la fonction decrypte_aes_cbc avec un message invalide
        """
        iv = b'\x00' * 16
        key = b'\x01' * 16
        ciphertext = b'\x00' * 15  # Message invalide
        with self.assertRaises(Exception):
            decrypte_aes_cbc(iv, ciphertext, key)

    def test_cassage_brutal_aes(self):
        """
        Fonction permettant de tester la fonction cassage_brutal_aes
        """
        message_crypter = crypte_aes('Bonjour', 0b00000101)
        self.assertEqual(cassage_brutal_aes('Bonjour', message_crypter)[0], 5)

    def test_estimation_temps_cassage_brutal(self):
        """
        Fonction permettant de tester la fonction estimation_temps_cassage_brutal
        """
        message_crypter = crypte_aes('Bonjour', 0b0)
        message_crypter2 = crypte_aes('Bonjour', 23322)
        self.assertIsInstance(
            estimation_temps_cassage_brutal('Bonjour', message_crypter), tuple)
        self.assertIsInstance(
            estimation_temps_cassage_brutal('Bonjour', message_crypter2),
            tuple)
