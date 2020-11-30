# Python TP3

## Reprenez vos programmes du TP1 (menu) et TP2 (calculatrice) et ajouter la gestion des exceptions (try, except, else, finally).

Voir le code source des tp1 et tp2

## Lever une exception avec assert et raise.

Voir le code source du tp1

## Demander pour enregistrement un login (input) et un mot de passe à l’utilisateur avec getpass() en mode console ou avec une fenêtre tkinter affichant des * à la place des caractères saisis. Stocker le couple login et hash mot de passe dans un fichier texte. Demander pour vérification un login et un mot de passe, vérifier la présence dans le fichier. Utiliser le « salage » pour renforcer le système avec une chaîne comprenant le login et une partie fixe.

La fonction enregistrement permet d'enregistrer le mot de passé chiffré de l'utilisateur.

La fonction login retourne vrai si l'utilisateur à bien été identifié correctement avec le fichier mot_de_passe.txt contenant tout les login/motdepasse

fichier mot_de_passe :

     yoann,ceca103504a8738343975cbf8ac0f6b785bf246a44988696f2134ec080dc9f18bb8e1d0d075099b2a9f5851ff48b34c944a92def38289879856686c240cd3b4b

## Demander à l’utilisateur le nom d’un fichier existant (par ex. un fichier texte que vous avez créé) que vous allez chiffrer dans un nouveau fichier en utilisant le mot de passe précédent avec l’algorithme AES 256. Vous pouvez utiliser la bibliothèque PyCryptodome

L'utilisateur chiffre le fichier fichier.txt dans le dossier a_chiffrer

fichier.txt :

     Ceci est un test
     
Ensuite le fichier est chiffré dans le dossier fichier_chiffrer:

encrypted.bin :

     Kt�
     � �Z�����(K�F\r���w 8f<��+�,�x���G
     
On peut déchiffrer le fichier en ayant connaissance du login et du mot de passe :

fichier_dechiffrer :

     Ceci est un test
     