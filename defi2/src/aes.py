"""
Module pour l'AES
"""
from cryptography.fernet import Fernet
import constantes2 as c
import base64

def crypte_aes(texte: str, cle: int) -> str:
    """
    Fonction qui crypte un texte avec l'algorithme AES avec la bibliothèque cryptography

    Args:
        texte (str): Le texte à crypter
        cle (int): La clé de cryptage

    Returns:
        str: Le texte crypté
    """
    cle_bytes = cle.to_bytes(c.NOMBRE_OCTETS_CLE, 'big')
    cle_encoded = base64.urlsafe_b64encode(cle_bytes)
    f = Fernet(cle_encoded)
    texte_crypte = f.encrypt(texte.encode())
    return texte_crypte.hex()


def decrypte_aes(texte: str, cle: int) -> str:
    """
    Fonction qui décrypte un texte avec l'algorithme AES avec la bibliothèque cryptography

    Args:
        texte (str): Le texte à décrypter
        cle (int): La clé de décryptage

    Returns:
        str: Le texte décrypté
    """
    try:
        cle_bytes = cle.to_bytes(c.NOMBRE_OCTETS_CLE, 'big')
        cle_encoded = base64.urlsafe_b64encode(cle_bytes)
        f = Fernet(cle_encoded)
        texte_decrypte = f.decrypt(bytes.fromhex(texte))
        return texte_decrypte.decode()
    except Exception as e:
        raise Exception('Une erreur est survenue lors du décryptage') from e
    