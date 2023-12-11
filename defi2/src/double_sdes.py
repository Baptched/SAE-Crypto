"""
Module qui contient les fonctions pour faire un double SDES
"""

from sdes import crypter, decrypt


def crypte_double_sdes(texte: str, cle1: int, cle2: int) -> str:
    """
    Fonction qui fait un double SDES sur le texte donné avec les clés données

    Args:
        texte (str): Le texte à crypter de n'importe quelle longueur
        cle1 (int): La première clé
        cle2 (int): La deuxième clé

    Returns:
        str: Le texte crypté
    """
    texte_crypte = ""
    for char in texte:
        lettre_int = ord(char)
        crypter_1 = crypter(cle1, lettre_int)
        crypter_2 = crypter(cle2, crypter_1)
        texte_crypte += chr(crypter_2)
    return texte_crypte


def decrypte_double_sdes(texte: str, cle1: int, cle2: int) -> str:
    """
    Fonction qui fait un double SDES sur le texte donné avec les clés données

    Args:
        texte (str): Le texte à crypter de n'importe quelle longueur
        cle1 (int): La première clé
        cle2 (int): La deuxième clé

    Returns:
        str: Le texte crypté
    """
    texte_decrypte = ""
    for char in texte:
        lettre_int = ord(char)
        decrypter_1 = decrypt(cle2, lettre_int)
        decrypter_2 = decrypt(cle1, decrypter_1)
        texte_decrypte += chr(decrypter_2)
    return texte_decrypte
