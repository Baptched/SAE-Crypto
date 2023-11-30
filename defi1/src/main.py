"""
Module d'affichage pour les differents messages
"""

import constantes as const
from message1 import decrypte_cesar, decrypte_acrostiche
from message2 import decrypte_vigenere, decrypte_pangramme, decrypte_substitution


def affichage_message_numero_1():
    """
    Fonction permettant d'afficher le message numéro 1
    """
    print("")
    print("Message numéro 1 :")
    print("")
    print(const.MESSAGE_1)
    print("")
    print(
        "En utilisant la méthode de César avec un décalage de 12, on trouve le message :"
    )
    print("")
    print(decrypte_cesar(const.MESSAGE_1, 12))
    print("")
    print(
        "En utilisant la méthode de l'acrostiche sur le message sur ce message, on trouve :"
    )
    print("")
    print(decrypte_acrostiche(decrypte_cesar(const.MESSAGE_1, 12)))


def affichage_message_numero_2():
    """
    Fonction permettant d'afficher le message numéro 2
    """
    print("")
    print("Message numéro 2 :")
    print("")
    print(const.MESSAGE_2)
    print("")
    print(
        "En utilisant la méthode de Vigenère avec la clé PANGRAMME, on trouve le message :"
    )
    print("")
    print(decrypte_vigenere(const.MESSAGE_2, const.MOT_1))
    print("")
    print("En utilisant la méthode du pangramme sur ce message, on trouve :")
    print("")
    print(decrypte_pangramme(decrypte_vigenere(const.MESSAGE_2, const.MOT_1)))
    print("")
    print(
        "En utilisant la méthode de substitution avec le pangramme que nous venons d'obtenir"
    )
    print("on trouve le message :")
    print("")
    print(
        decrypte_substitution(
            const.MESSAGE_3,
            decrypte_pangramme(decrypte_vigenere(const.MESSAGE_2,
                                                 const.MOT_1))))


if __name__ == "__main__":
    affichage_message_numero_1()
    affichage_message_numero_2()
