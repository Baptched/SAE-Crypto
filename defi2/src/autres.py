"""
Module contenant différentes fonctions utiles
"""

import random


def genere_key_10_bits() -> int:
    """
    Fonction qui génère une clé aléatoire de 8 bits soit entre 0 et 255

    Returns:
        int: La clé générée
    """
    return random.randint(0, 2**10)


def genere_key_256_bits() -> int:
    """
    Fonction qui génère une clé aléatoire de 256 bits soit entre 0 et 2^256

    Returns:
        int: La clé générée
    """
    return random.randint(0, 2**256)
