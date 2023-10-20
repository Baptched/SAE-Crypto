# SAE - Cryptographie

Baptiste Chédeville  

GitHub : [Lien vers le projet](https://github.com/Baptched/SAE-Crypto)

## Origine du projet

Lors de la SAE Crypto, il nous a été donné plusieurs messages a décrypter.
Pour cela, nous devions trouver nous même la méthode de chiffrement.
Et d'implémenter des fonctions en python qui decrypte ces différents messages.

## Réalisation

### Décryptage 

#### Message 1

Les differentes fonctions sont retrouvables dans le fichier `message1.py`.

Le premier message qui nous a été donné est :

```
BDQE PG OTQYUZ EQ OMOTQ GZ FDQEAD
MOODAOTQ M GZ MDNDQ FAGF DQOAGHQDF P'AD
ZQ ZQSXUSQ BME XM VQGZQ BAGOQ RQGUXXG
SDMZP QEF EAZ EQODQF YMXSDQ EM FMUXXQ YQZGQ
DAZPQE QF OAXADQQE EAZF XQE NMUQE CG'UX BADFQ
MZUEQQE QF EGODQQE, XQGDE EMHQGDE EAZF RADFQE.
YMUE MFFQZFUAZ M ZQ BME XQE ODACGQD,
YQYQ EU XM RMUY FUDMUXXQ FQE QZFDMUXXQE,
QZ MGOGZ OME FG ZQ PAUE EGOOAYNQD
```

Ce message est crypté grâce à la méthode de César avec un décalage de 12. 
Cette méthode consiste a décallé chaque lettre de l'alphabet d'un certains decallage, ici 12.

(Python functions in `message1.py` from line 8 to 39)

En le déchiffrant, nous obtenons :

```
PRES DU CHEMIN SE CACHE UN TRESOR
ACCROCHE A UN ARBRE TOUT RECOUVERT D'OR
NE NEGLIGE PAS LA JEUNE POUCE FEUILLU
GRAND EST SON SECRET MALGRE SA TAILLE MENUE
RONDES ET COLOREES SONT LES BAIES QU'IL PORTE
ANISEES ET SUCREES, LEURS SAVEURS SONT FORTES.
MAIS ATTENTION A NE PAS LES CROQUER,
MEME SI LA FAIM TIRAILLE TES ENTRAILLES,
EN AUCUN CAS TU NE DOIS SUCCOMBER
```

Et enfin pour retrouver le mot caché, il faut utilisé la méthode de Acrostiche qui consiste a prendre la première lettre de chaque mot.

(Python function in `message1.py` from line 42 to 60)

On trouve donc le mot `PANGRAMME`


### Message 2 et 3

Les differentes fonctions sont retrouvables dans le fichier `message2.py`.

Le second message donné est :

```
AE IOW ZQBLNR WASIXQ WJR YKJ KGYUJAGY UU OXSLN TXRCUQYM
IY IRCTQ HPNF RR RQBIIIGOFN XQ WTCEKK DQ OIH MHXDUDQW BAYNVUDQYM
NR MRRPQD SU CXVMUQV HOHLWLQ CYT LRY GRQYMTRRY RPBMVXTVUES
QF EXNFO UEHAMAEM RV MQEWPGR IRCTQ HTREOVRQ XE HUOYKIFGXXOA
```

Ce message a été crypter avec la technique de Vigenère qui est une méthode de chiffrement par substitution polyalphabétique. Elle consiste à utiliser une clé  pour chiffrer un message. À chaque caractère du message, on applique un décalage variable basé sur la lettre correspondante de la clé.

(Python functions in `message2.py` from line 8 to 35)

On trouve le message :

```
LE VIF ZEPHYR JUBILE SUR LES KUMQUATS DU CLOWN GRACIEUX
IL CACHE DANS LA REPETITION LE SECRET DE CES MURMURES MALHEUREUX
NE GARDEZ DU PREMIER SOUFFLE QUE LES PREMIERES APPARITIONS
ET AINSI DEVOILEZ LE MESSAGE CACHE DERRIERE LA SUBSTITUTION
```

En analysant ce message, il nous ai dit de faire un pangramme avec ce message et de faire une subtitution avec.

Un pangramme est un message contenant toutes les lettres de l'alphabet.

(Python function in `message2.py` from line 38 to 52)

On trouve donc le pangramme : `LEVIFZPHYRJUBSKMQATDCOWNGX`

En utilisant cette clé dans une subtitution sur le message numéro 3 qui nous ai donné.

Message numéro 3 : 

```
EALOK, OKCT LOFX PLPSF! UF VKIF L ZKCASYA FTD: FUYXFEFDH
```

(Python function in `message2.py` from line 56 to 79)

On trouve la phrase :

```
BRAVO, VOUS AVEZ GAGNE! LE CODE A FOURNIR EST: ELIZEBETH
```

### Main

Un fichier `main.py` permet de lancer les fonctions concu ainsi qu'afficher les resultats avec les messages cryptés qui nous ont été fournis.

Le fichier main se lance avec la commande :

```bash
python3 src/main.py
```

### GitHub

Tout au long de ce projet, un référentiel GitHub a été utilisé en suivant la méthode de gestion des versions Git Flow.

Lien du GitHub : [Lien vers le projet](https://github.com/Baptched/SAE-Crypto)


### Qualité de code

Pour amméliorer la qualité du code lors de ce projet, j'ai ajouté un fichier `Makefile` permettant grâce au diminutif `make` de lancer différentes commandes sur le projet.

Pour installer les différentes commandes du Makefile, il faut exécuter la commande :

```bash
pip install -r requirements.txt
```

- Pylint grâce à la commande :

```bash
make lint
```

- Yapf avec 

```bash
make format
```

- Mypy avec :

```bash
make typehint
```

Ces trois commandes permmettent de maintenir une bonne syntaxe et qualité de code.

Le makefile permet aussi de lancer les tests unitaires avec :

```bash
make tests
```

et de voir le coverage de ces tests avec 

```bash
make coverage
```

J'ai aussi mis en place sur le GitHub une GitHub action qui reprend les commandes du makefile.

Cette GitHUb action verifie la qualité du code ainsi que les tests unitaires.

### Tests unitaires

Dans le répertoire tests, des tests unitaires on été implémenter pour tester de différentes façons les fonctions qui ont été implémenter.
Les tests sont implémenter pour coubir 100% du code impélmenté.

On peut lancer les tests avec la commande :

```bash
make tests
```

Et le coverage de ces tests :

```bash
make coverage
```
