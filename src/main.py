"""
Module d'affichage pour les differents messages
"""

import constantes as const
from message1 import decrypte_cesar, decrypte_acrostiche


def affichage_message_numero_1():
    """
    Fonction permettant d'afficher le message numéro 1
    """
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


if __name__ == "__main__":
    affichage_message_numero_1()
