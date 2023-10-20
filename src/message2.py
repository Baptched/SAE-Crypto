"""
Module permettant de decrypter le message numéro 2
"""

import constantes as const


def decrypte_vigenere(message: str, cle: str) -> str:
    """
    Fonction permettant de déchiffrer un message chiffré par la méthode de Vigenère
    Si la clé est vide, le message est retourné en majuscule

    Args:
        message (str): Le message chiffré à déchiffrer
        cle (str): La clé de chiffrement

    Returns:
        str: Le message décrypté
    """
    message_decrypte = ""
    index_cle = const.INITIALISE_INDEX
    if cle == "":
        return message.upper()
    for lettre in message:
        if lettre.isalpha():
            lettre_decrypte = chr(
                (ord(lettre) - ord(cle[index_cle]) - ord("A") * const.DOUBLE) %
                const.NOMBRE_LETTRES_ALPHABET + ord("A"))
            index_cle += const.INCREMENTE_INDEX
            if index_cle == len(cle):
                index_cle = const.INITIALISE_INDEX
        else:
            lettre_decrypte = lettre
        message_decrypte += lettre_decrypte
    return message_decrypte


def decrypte_pangramme(message: str) -> str:
    """
    Fonction permettant de récupérer le pangramme dans le message
    C'est-à-dire uniquement la première apparition de chaque lettre de l'alphabet

    Args:
        message (str): Le message à analyser

    Returns:
        str: Le pangramme du message
    """
    message_decrypte = ""
    for caractere in message:
        if caractere.isalpha() and caractere not in message_decrypte:
            message_decrypte += caractere
    return message_decrypte
