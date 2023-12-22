# SAE - Cryptographie

Baptiste Chédeville  
Noa Jacquet
2A3B

GitHub : [Lien vers le GitHub](https://github.com/Baptched/SAE-Crypto)


## Introduction

Dans le cadre de la SAE Cryptographie, nous avons réalisé un projet sur la cryptographie.
Ce projet est découpé en 4 parties.
Plusieurs questions sont posées dans chaque partie et nous devons y répondre.
Pour répondre à ces questions, nous devons implémenter des algorithmes de cryptographie et faire des recherches sur internet.
Différents types de cryptographie sont abordés dans ce projet.


## Lancer le projet

Pour lancer le projet, il faut tout d'abord cloner le GitHub :

```bash
git clone https://github.com/Baptched/SAE-Crypto
```

Puis télécharger les dépendances :

```bash
pip install -r requirements.txt
```

Ensuite, il faut lancer le fichier `main.ipynb` avec Jupyter Notebook.
Ce fichier contient des exemples d'utilisation des fonctions implémentées.


## Réponse aux questions

### Partie 1 : premières tentatives


#### 1) RSA

Eve a à sa disposition la clé publique qui est composée de n et e. n correspond à la multiplication de p et de q, tandis que e est l'exposant public.
Avec cette clé privée, il est seulement possible de crypter un message mais pas de le décrypter.
Pour décrypter les messages, il faut la clé privée.
Si Eve veut venir à bout de RSA, elle doit donc trouvé la clé privée d.


Ce qui est possible grâce à la connaissance de la clé public (n, e), mais pour cela il suffit de retrouver les facteurs premiers p et q
Puis de recalculer la clé privée d comme l'ont fait Alice et Bob.


Hors, ici Alice et Bob ont utilisé le protocole RSA correctement donc p et q sont des nombres premiers très très grands.
Donc pour retrouver ces nombres il faut refactoriser le nombre n qui est donc lui aussi très très grand.

C'est ici que la sécurité du protocole RSA rentre en jeu, car cette sécurité repose sur l'hypothèse selon lequelle, trouver les facteurs premiers d'un nombre cryptographiquement grand tel que n, est un problème impossible à résoudre dans un temps raisonnable.


En conclusion si Alice et Bob ont utilisé le protocole RSA correctement, Eve ne trouvera jamais la clé privée et ne pourra jamais décrypter les messages de Alice et Bob.


#### 2) SDES

L'algorithme SDES est peu sécurisé car il est très simple. En effet, cet algorithme se base sur des clés de petite taille (10 bits). 
Ce qui signifie qu'il existe 2**10 clés soit 1024 clés possibles.

Ce qui est très vulnérable à une méthode “force brute” qui consisterais à essayer chaque clé jusqu'à trouver la bonne.


#### 3) Double SDES

En utilisant une méthode "force brute", le double SDES permet de grandement augmenter le nombre de clé à tester.
En effet, cette méthode utilise deux étapes de chiffrement avec chacune une clé de 10 bits.
Donc le nombre de clé à tester est le produit du nombre de clés des deux étapes soit 1 048 576 clés (1024 * 1024)


Mais avec une certaine technique, le double SDES n'est pas plus sûr que le SDES seul.

La technique est l'attaque par rencontre au milieu (Meet in the middle).

Cette technique exploite le fait que le chiffrement est composé de deux parties indépendantes (ici avec le double SDES).

Pour cela, Eve doit récupérer un message crypté et ce même message non crypté.

Puis ensuite Eve choisit un ensemble de clés possibles pour la première étape de chiffrement et un autre ensemble pour la seconde étape.
Elle chiffre le message clair avec toutes les clés du premier ensemble et stocke le résultat.
Puis dans un second temps, elle chiffre le message crypté mais cette fois-ci avec le second ensemble de clés et le stock.
L'étape suivante est de rechercher une correspondance entres les deux résultats obtenus. Si elle trouve une correspondance, cella indique un couple de clés qui ont été utilisé pour crypter le message.

Donc en essayant toute les possibilités, il faut essayer les 1024 clés deux fois. Soit 2048 essais. Pour déchiffrer le double SDES.


#### 4) A vous de jouer

L'ensemble des fonctions sont retrouvables dans le fichier `aes.py`.
Ces fonctions sont testées dans le fichier `tests/test_aes.py`.
Et elles sont utilisées dans le fichier `main.ipynb`.



### Partie 2 : un peu d'aide

#### 1) AES

Maintenant que le protocole utilise AES avec des clés de 256 bits, il est beaucoup plus difficile de le casser surtout avec une méthode de force brute.
En effet, il y a 2**256 clés possibles soit 1.1579209e+77 clés possibles.
Il est donc impossible de tester toutes les clés possibles dans un temps raisonnable.
La sécurité de AES repose sur le fait que le nombre de clés possibles est trop grand pour être testé.
La seule méthode pour casser AES est de trouver une faille dans l'algorithme AES.
Ce qui est très peu probable car AES est un algorithme très utilisé et très étudié.
Ou que la clé choisie par Alice et Bob soit trop faible comme par exemple une clé de 1 bit.
Dans ce cas, il est possible de casser AES avec une méthode de force brute.
Mais si Alice et Bob ont utilisé AES correctement, il est impossible de casser AES.

#### 2) Illustration expérimentale

Les fonctions sont retrouvables dans le fichier `aes.py`.
Ces fonctions sont testées dans le fichier `tests/test_aes.py`.
Et elles sont utilisées dans le fichier `main.ipynb` ou une illustration expérimentale est faite pour comparer AES et double SDES.

#### 3) Types d'attaques

Il y a plusieurs types d'attaques possibles sur AES.

- Attaque par force brute : Cette attaque consiste à tester toutes les clés possibles jusqu'à trouver la bonne. Mais comme vu précédemment, cette attaque est impossible à réaliser sur AES.

- Ataque par temps caché (Timing Attacks) : En analysant le temps mis par l'algorithme pour chiffrer ou déchiffrer des données, un attaquant pourrait essayer d'inférer des informations sur la clé secrète.

- Attaque par canaux cachés (Side Channel Attacks) : En analysant la consommation électrique de l'algorithme AES, un attaquant pourrait essayer d'inférer des informations sur la clé secrète.

- Attaque par colision : Cette attaque consiste à trouver deux messages différents qui ont le même message chiffré.

- Attaque par analyse différentielle : Cette attaque consiste à analyser les différences entre les entrées et les sorties de l'algorithme AES. 

- Attaque par analyse linéaire : Cette attaque consiste à analyser les corrélations linéaires entre les entrées et les sorties de l'algorithme AES.

- Attaque par faute : Cette attaque consiste à injecter une faute dans l'algorithme AES.

- Attaque par faute par canaux cachés : Cette attaque consiste à injecter une faute dans l'algorithme AES et à analyser la consommation électrique de l'algorithme AES.

Toutes ces attaques sont très difficiles à mettre en place et nécessitent beaucoup de ressources.
Et ne permettent pas de casser AES mais de trouver des failles dans l'algorithme AES. C'est à dire de trouver des cas ou AES n'est pas sécurisé.


#### 4) La clé cachée

Pour retrouver la clé cachée dans les images, nous avons dans un premier temps examiné la composition des images, c'est à dire les pixels qui les composent.
Nous avons donc implémenté une fonction qui permet de récupérer les pixels de la première image et de les comparer avec les pixels de la seconde image.
Cette fonction est retrouvable dans le fichier `steganographie.py` et est testée dans le fichier `tests/test_steganographie.py`.

On a donc dans un premier temps vu que les deux images étaient différentes et que les pixels étaient différents.
Nous avons ensuite essayé de trouver une correspondance entre les pixels des deux images.

Dans un premier temps, pour chaque pixel de la seconde image, nous l'avons soustrait au pixel correspondant de la première image.
Nous avons vite remarqué qu'à certains endroits la valeur retournée était négative. Ce qui n'est pas possible dans une clé.
Après différentes recherches, nous avons trouvé que les valeurs négatives étaient seulement au début des images.

Du coup, dans un second temps nous avons essayé de garder seulement le dernier bit de chaque pixel de la seconde image.
Puis nous avons trouvé la clé de 64 bits.

Cette fonction est retrouvable dans le fichier `steganographie.py` et est testée dans le fichier `tests/test_steganographie.py`.
Ainsi que dans le fichier `main.ipynb` ou nous avons affiché la clé.


### Partie 3 : analyse des messages

Pour retrouver les messages cachés dans la trame .cap, nous avons utilisé le logiciel Wireshark dans un premier temps.
Nous avons donc ouvert la trame .cap avec Wireshark et nous avons filtré les paquets avec le protocole UDP et le port 9999.

Nous avons donc trouvé 2 paquets UDP.

Ensuite, nous avons utilisé la librairie scapy pour lire la trame .cap et récupérer les paquets UDP avec le port 9999.

Cette fonction est retrouvable dans le fichier `analyse_trace.py` et est testée dans le fichier `tests/test_analyse_trace.py`.

Nous avons ensuite decrypté les messages avec la clé que nous avions précédemment trouvé et l'algorithme AES en mode CBC.
La particularité de ce mode est qu'il faut un vecteur d'initialisation (IV) pour le premier bloc.
Comme expliqué dans le sujet, le vecteur d'initialisation est ajouté en tête du message et plus particulièrement dans les 16 premiers octets.
Nous avons donc récupéré les 16 premiers octets de chaque message et nous les avons utilisé comme vecteur d'initialisation.
Puis nous avons décrypté le message avec AES en mode CBC.
Il a fallu ajouter un padding au message pour que sa taille soit un multiple de 128 bits.

Cette fonction est retrouvable dans le fichier `analyse_trace.py` et est testée dans le fichier `tests/test_analyse_trace.py`.
Ainsi que dans le fichier `main.ipynb` ou nous avons affiché les messages décryptés.


### Partie 4 : un peu de recul


1) L'utilisation constante de la même clé par Alice et Bob n'est généralement pas considérée comme une bonne pratique en cryptographie. Cela est dû au fait qu'une clé statique augmente le risque de compromission si elle est exposée à un attaquant. Le changement régulier des clés est recommandé pour renforcer la sécurité du système. Cependant, il est également important de mettre en place des mécanismes appropriés pour gérer et distribuer ces clés de manière sécurisée

2) Le protocole plutôt Bonne Confidentialité semble être inspiré par le protocole TLS/SSL (Transport Layer Security/Secure Sockets Layer), qui est couramment utilisé pour sécuriser les communications sur Internet. Le fait qu'il utilise UDP sur le port 9999, la phase d'échange de clé asymétrique suivie d'une communication symétrique chiffrée avec AES-256 en mode CBC, ainsi que l'utilisation du vecteur d'initialisation (IV) en tête du message sont des caractéristiques qui rappellent le fonctionnement de TLS/SSL.

3) L'utilisation la plus répandue de TLS/SSL est pour sécuriser les connexions HTTP, créant ainsi HTTPS (HTTP Secure). Cela garantit la confidentialité et l'intégrité des données échangées entre un utilisateur et un site web.

4) Différents réseaux sociaux utilisent ces méchanismes de chiffrement :

- WhatsApp utilise le protocole Signal pour le chiffrement de bout en bout. Il s'agit d'un protocole open source qui utilise des clés de session générées localement sur les appareils des utilisateurs. Les messages sont chiffrés sur l'appareil émetteur et déchiffrés sur l'appareil récepteur.

- iMessage utilise un chiffrement de bout en bout basé sur le protocole APNs et iCloud. Les messages sont chiffrés sur l'appareil émetteur, envoyés chiffrés sur les serveurs d'Apple, puis déchiffrés sur l'appareil récepteur

- Facebook Messenger utilise le protocole Signal pour le chiffrement de bout en bout. Les messages sont chiffrés sur l'appareil émetteur et déchiffrés sur l'appareil récepteur.

- Telegram utilise un chiffrement de bout en bout basé sur le protocole MTProto. Les messages sont chiffrés sur l'appareil émetteur, envoyés chiffrés sur les serveurs de Telegram, puis déchiffrés sur l'appareil récepteur.

5) Ces projets de loi ont pour objectif principal d’assurer la sécurité de chacun. Ils affirment que l'accès aux données chiffrées est nécessaire pour prévenir et enquêter sur des activités criminelles, notamment le terrorisme. Il est également estimé que les fournisseurs de services numériques sont responsables du contenu hébergé sur leur plateforme et devraient donc avoir accès à ce contenu afin de faciliter la détection de contenus illicites.

Cependant, autoriser l’accès aux communications des utilisateurs peut constituer de réelles complications, la principale étant le fait de compromettre le droit fondamental à la vie privée. En plus de cela, ces lois entraîneraient sûrement un affaiblissement des mesures de sécurité et donc mettraient en danger la confidentialité des données et la confiance des utilisateurs dans les services en ligne.

En résumé, le débat entre la nécessité de garantir la sécurité publique et la protection de la vie privée reste complexe. Trouver un équilibre entre ces deux impératifs constitue un défi majeur pour les législateurs, car cela nécessite une compréhension approfondie des implications techniques, juridiques et sociales.


## Répartition des tâches

Lors de ce projet, nous avons travaillé en binôme.
Nous nous somme réparti les tâches de la façon suivante :
Mais nous avons travaillé ensemble sur certaines parties.

- Baptiste Chédeville : 
    - Partie 1 : Implémentation de l'algorithme double SDES
               : Implémentation cassage astucieux du double SDES
               : Reponse aux questions
    - Partie 2 : Implémentation du module stéganographie pour retrouver la clé cachée dans les images
    - Partie 3 : Implémentation du module analyse_trace pour retrouver les messages cachés dans la trame .cap
    - GitHub
    - Qualité de code
    - Tests unitaires
    - Fichier main.ipynb pour lancer les fonctions implémentées
    - Rapport

- Noa Jacquet :
    - Partie 1 : Implémentation du cassage brutal du double SDES
               : Implémentation d'un graphique de comparaison entre les deux méthodes de cassage
    - Partie 2 : Implémentation de l'algorithme AES
               : Implémentation du cassage brutal de l'algorithme AES
    - Partie 4 : Réponse aux questions
    - GitHub
    - Qualité de code
    - Tests unitaires
    - Rapport



### GitHub

Tout au long de ce projet, un référentiel GitHub a été utilisé en suivant la méthode de gestion des versions Git Flow.

Lien du GitHub : [Lien vers le GitHub](https://github.com/Baptched/SAE-Crypto)


### Qualité de code

Pour amméliorer la qualité du code lors de ce projet, nous avons ajouté un fichier `Makefile` permettant grâce au diminutif `make` de lancer différentes commandes sur le projet.

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

Le Makefile permet aussi de lancer les tests unitaires avec :

```bash
make tests
```

et de voir le coverage de ces tests avec 

```bash
make coverage
```

Nous avons aussi mis en place sur le GitHub une GitHub Action qui reprend les commandes du Makefile.

Cette GitHUb action vérifie la qualité du code ainsi que les tests unitaires.
Et pour passer cette GitHub Action, il faut obtenir 10/10 avec Pylint, ne pas avoir de problème avec Mypy et que tous les tests unitaires passent.
Cela permet de continuellement garder le GitHub propre ainsi que sans erreur.


### Tests unitaires

Dans le répertoire `tests`, des tests unitaires on été implémentés pour tester de différentes façons les fonctions qui ont été implémentées.
Les tests sont implémentés pour couvrir quasiment toutes les lignes de code des fonctions.

On peut lancer les tests avec la commande :

```bash
make tests
```

Et le coverage de ces tests :

```bash
make coverage
```
