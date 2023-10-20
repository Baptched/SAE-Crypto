"""
Module permettant de decrypter le message numéro 2
"""


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
    index_cle = 0
    if len(cle) == 0:
        return message.upper()
    for lettre in message:
        if lettre.isalpha():
            lettre_decrypte = chr(
                (ord(lettre) - ord(cle[index_cle]) - ord("A") * 2) % 26 +
                ord("A"))
            index_cle += 1
            if index_cle == len(cle):
                index_cle = 0
        else:
            lettre_decrypte = lettre
        message_decrypte += lettre_decrypte
    return message_decrypte
