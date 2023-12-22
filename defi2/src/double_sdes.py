"""
Module qui contient les fonctions pour faire un double SDES
"""

import time
import constantes2 as c
import threading
import os
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


def cassage_brutal(message_clair: str,
                   message_chiffre: str) -> tuple[int, int, int, float] | None:
    """
    Fonction qui casse le cryptage double SDES en testant toutes les clés possibles

    Args:
        message_clair (str): Le message clair
        message_chiffre (str): Le message chiffré

    Returns:
        tuple: La clé 1 et la clé 2, le nombre de tentatives et le temps de calcul
    """
    nombre_tentatives = 0
    debut = time.time()
    for cle1 in range(c.NOMBRE_CLE_POSSIBLE_SDES):
        for cle2 in range(c.NOMBRE_CLE_POSSIBLE_SDES):
            nombre_tentatives += 1
            if crypte_double_sdes(message_clair, cle1,
                                  cle2) == message_chiffre:
                temps = time.time() - debut
                temps = round(temps, 3)
                return (cle1, cle2, nombre_tentatives, temps)
    return None


def recherche_cle_partielle(message_clair: str, message_chiffre: str,
                            debut_cle_range: int, fin_cle_range: int,
                            resultat_partiel: list) -> None:
    """
    Fonction qui recherche la clé dans un intervalle donné

    Args:
        message_clair (str): Le message clair
        message_chiffre (str): Le message chiffré
        debut_cle_range (int): Le début de l'intervalle
        fin_cle_range (int): La fin de l'intervalle
        resultat_partiel (list): La liste qui contient le résultat partiel
    """
    for cle1 in range(debut_cle_range, fin_cle_range):
        for cle2 in range(c.NOMBRE_CLE_POSSIBLE_SDES):
            resultat_partiel[2] += 1
            if crypte_double_sdes(message_clair, cle1,
                                  cle2) == message_chiffre:
                resultat_partiel[0] = cle1
                resultat_partiel[1] = cle2
                return


def cassage_brutal_avec_thread(
        message_clair: str, message_chiffre: str
) -> tuple[int, int | None, int | None, float] | None:
    """
    Fonction qui casse le cryptage double SDES en testant toutes les clés possibles avec des threads

    Args:
        message_clair (str): Le message clair
        message_chiffre (str): Le message chiffré

    Returns:
        tuple: La clé 1 et la clé 2, le nombre de tentatives et le temps de calcul
    """
    debut = time.time()
    nombre_threads = os.cpu_count(
    ) or 1  # Détermine le nombre de threads en fonction du nombre de cœurs disponibles
    print(f"Nombre de threads: {nombre_threads}")
    threads = []
    le_resultat = [None, None, 0]  # [clé1, clé2, nombre_tentatives]

    # On crée les threads
    pas = c.NOMBRE_CLE_POSSIBLE_SDES // nombre_threads

    for i in range(nombre_threads):
        debut_cle_range = i * pas
        fin_cle_range = (
            i +
            1) * pas if i != nombre_threads - 1 else c.NOMBRE_CLE_POSSIBLE_SDES
        thread = threading.Thread(target=recherche_cle_partielle,
                                  args=(message_clair, message_chiffre,
                                        debut_cle_range, fin_cle_range,
                                        le_resultat))
        threads.append(thread)

    # On démarre tous les threads
    for thread in threads:
        thread.start()

    # On attend que tous les threads soient terminés
    while le_resultat[0] is None:
        pass

    temps = time.time() - debut
    return (le_resultat[0], le_resultat[1], le_resultat[2], temps)


def cassage_astucieux(
        message_clair: str,
        message_chiffre: str) -> tuple[int, int, int, float] | None:
    """
    Fonction qui casse le cryptage double SDES en utilisant
    les propriétés de la fonction de cryptage

    Args:
        message_clair (str): Le message clair
        message_chiffre (str): Le message chiffré

    Returns:
        tuple: La clé 1 et la clé 2, le nombre de tentatives et le temps de calcul
    """
    tableau = {}
    nombre_tentatives = 0
    debut = time.time()
    for cle1 in range(c.NOMBRE_CLE_POSSIBLE_SDES):
        message_crypte = crypte_double_sdes(message_clair, cle1, 0)
        tableau[message_crypte] = cle1
        nombre_tentatives += 1

    for cle2 in range(c.NOMBRE_CLE_POSSIBLE_SDES):
        nombre_tentatives += 1
        message_decrypte = decrypte_double_sdes(message_chiffre, 0, cle2)
        if message_decrypte in tableau:
            temps = time.time() - debut
            temps = round(temps, 3)
            return tableau[message_decrypte], cle2, nombre_tentatives, temps
    return None
