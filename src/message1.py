"""
Module permettant de decrypter le message numéro 1
"""


def decrypte_cesar(message: str, nb_decalage: int) -> str:
    """
    Fonction permettant de déchiffrer un message chiffré par la méthode de César 
    selon un décalage donné
    Le message peut contenir des caractères spéciaux, des chiffres et des 
    lettres minuscules ou majuscules

    Args:
        message (str): Le message chiffré à déchiffrer
        nb_decalage (int): Le nombre de décalage à effectuer pour chaque lettre

    Returns:
        str: Le message decrypter
    """
    message_decrypte = ""

    for caractere in message:
        if caractere.isalpha():
            # chr permet de convertir un code ASCII en caractère
            # ord permet de convertir un caractère en code ASCII
            if caractere.islower():
                caractere_decrypte = chr(
                    (ord(caractere) - nb_decalage - ord("a")) % 26 + ord("a"))
            else:
                caractere_decrypte = chr(
                    (ord(caractere) - nb_decalage - ord("A")) % 26 + ord("A"))
        else:
            caractere_decrypte = caractere
        message_decrypte += caractere_decrypte
    return message_decrypte


def decrypte_acrostiche(message: str) -> str:
    """
    Fonction permettant de déchiffrer un message chiffré par la méthode de 
    l'acrostiche
    Le message peut contenir des caractères spéciaux, des chiffres et des 
    lettres minuscules ou majuscules

    Args:
        message (str): Le message chiffré à déchiffrer

    Returns:
        str: Le message décrypté
    """
    message_decrypte = ""
    lignes = message.split("\n")
    message_decrypte = ""
    for ligne in lignes:
        message_decrypte += ligne[0]
    return message_decrypte
