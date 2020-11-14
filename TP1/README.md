# Python TP1

## 1. Afficher « Bonjour le monde ! »
**Console :**

    Bonjour le monde !
 
## 2. En mode console (sans fenêtre), proposez un petit menu : 1. Choisir un nom de fichier, 2. Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme. Vous écrirez les fonctions associées aux choix.

**Console :**

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.

>     2

    Impossible d'écrire, nom du fichier vide

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.

>     1
     
    Entrez le nom du fichier :
    
>     test

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     4

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     2

    Votre texte : 
    
>     Ceci est un test

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     3

    Ceci est un test
    
    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     4

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     2

    Votre texte :
    
>     Ceci est un autre test

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     2

    Votre texte : 
    
>     Ceci est un ajout de texte

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.

>     3

    Ceci est un autre test
    Ceci est un ajout de texte
    
    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     4

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     3

    1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le fichier complet, 4. Vider le fichier, 9. Quitter le programme.
    
>     9

    

## 3. 	- Concevoir une classe Date (avec redéfinition (surcharge) de == ( __eq__ ) et de < ( __lt__ )) ;

**Test:**
>     if __name__ == "__main__":
>         date1 = Date(20, 4, 2020)
>         date2 = Date(6, 9, 2020)
> 
>         print(date1 == date2)
>         print(date1 < date2)
>         print(date2 < date1)

**Console:**

    False
    True
    False

## 3.	- Concevoir une classe Etudiant (avec une méthode adresselec qui fabrique l'adresse électronique prenom.nom@etu.univ-tours.fr et une méthode âge) ; 
##    - Lire le fichier fichetu.csv et constituer une liste d'objets Etudiant.

**Test:**
>     if __name__ == '__main__':
> 
>         etudiant1 = Etudiant("Paul", "Dupont", Date(22, 2, 1998))
>         print("âge de l'étudiant Paul Dupont né le 22/02/1998")
>         print(etudiant1.age)
>         print("")
> 
>         etudiant2 = Etudiant("Michel", "Martin", Date(8, 8, 2000))
>         print("adresse étudiante de Michel Martin")
>         print(etudiant2.adresse_lec)
>         print("")
> 
>         print("liste des étudiant depuis le ficheetu.csv")
>         for student in fiche_extractor("../fichetu.csv"):
>             print("nom de l'étudiant : " + student.nom + "\tdate d'anniversaire : " + student.anniversaire.__str__() +
>                   "\tâge : " + student.age.__str__())

**Console:**

    âge de l'étudiant Paul Dupont né le 22/02/1998
    21

    adresse étudiante de Michel Martin
    Michel.Martin@etu.univ-tours.fr

    liste des étudiant depuis le ficheetu.csv
    nom de l'étudiant : AMBROISE	date d'anniversaire : 1993-4-13	âge : 26
    nom de l'étudiant : ARCHAT	date d'anniversaire : 1993-12-9	âge : 26
    nom de l'étudiant : AZOUZ	date d'anniversaire : 1993-3-9	âge : 27
    nom de l'étudiant : BAI	date d'anniversaire : 1992-8-8	âge : 28
    nom de l'étudiant : BANAH	date d'anniversaire : 1993-5-18	âge : 26
    nom de l'étudiant : BASTAERT	date d'anniversaire : 1995-12-29	âge : 24
    nom de l'étudiant : BEN KHALIFA	date d'anniversaire : 1992-10-20	âge : 27
    nom de l'étudiant : BIAN	date d'anniversaire : 1990-12-26	âge : 29
    nom de l'étudiant : BOUVIER	date d'anniversaire : 1992-1-28	âge : 27
    nom de l'étudiant : CACHINHO	date d'anniversaire : 1990-11-17	âge : 29
    nom de l'étudiant : CAPO	date d'anniversaire : 1994-5-14	âge : 25
    nom de l'étudiant : CARNEIRO	date d'anniversaire : 1994-8-21	âge : 25
    nom de l'étudiant : CASCINO	date d'anniversaire : 1995-1-31	âge : 24
    nom de l'étudiant : CAUX	date d'anniversaire : 1994-4-24	âge : 25
    nom de l'étudiant : CHEN	date d'anniversaire : 1991-4-26	âge : 28
    nom de l'étudiant : COMBEMOREL	date d'anniversaire : 1994-1-13	âge : 25
    nom de l'étudiant : CORBILLE	date d'anniversaire : 1993-10-11	âge : 26
    nom de l'étudiant : CORREIA	date d'anniversaire : 1994-5-23	âge : 25
    nom de l'étudiant : DELEURENCE	date d'anniversaire : 1995-3-15	âge : 24
    nom de l'étudiant : DONG	date d'anniversaire : 1993-1-6	âge : 27
    nom de l'étudiant : DONG	date d'anniversaire : 1992-4-4	âge : 28
    nom de l'étudiant : DRONET	date d'anniversaire : 1995-6-15	âge : 24
    nom de l'étudiant : DURAND	date d'anniversaire : 1993-11-19	âge : 26
    nom de l'étudiant : FAYOUX	date d'anniversaire : 1993-1-15	âge : 26
    nom de l'étudiant : FILALI BOUKHRISS	date d'anniversaire : 1994-6-8	âge : 26
    nom de l'étudiant : FU	date d'anniversaire : 1990-7-20	âge : 29
    nom de l'étudiant : GILBERT	date d'anniversaire : 1993-6-11	âge : 26
    nom de l'étudiant : GREBIC	date d'anniversaire : 1994-4-13	âge : 25
    nom de l'étudiant : HEBERT	date d'anniversaire : 1993-5-1	âge : 27
    nom de l'étudiant : HORDE	date d'anniversaire : 1994-11-4	âge : 25
    nom de l'étudiant : JAZOULI BENLAHBOUB	date d'anniversaire : 1991-1-6	âge : 29
    nom de l'étudiant : JEOUIT	date d'anniversaire : 1995-4-13	âge : 24
    nom de l'étudiant : KARA	date d'anniversaire : 1994-11-3	âge : 25
    nom de l'étudiant : LI	date d'anniversaire : 1992-3-8	âge : 28
    nom de l'étudiant : LIU	date d'anniversaire : 1991-10-27	âge : 28
    nom de l'étudiant : LU	date d'anniversaire : 1992-8-2	âge : 28
    nom de l'étudiant : MATHE	date d'anniversaire : 1993-9-9	âge : 27
    nom de l'étudiant : MENARD	date d'anniversaire : 1994-8-9	âge : 26
    nom de l'étudiant : MENG	date d'anniversaire : 1991-4-25	âge : 28
    nom de l'étudiant : MENIN	date d'anniversaire : 1993-9-11	âge : 26
    nom de l'étudiant : MERCIER	date d'anniversaire : 1994-5-5	âge : 26
    nom de l'étudiant : MICHAUX	date d'anniversaire : 1993-8-5	âge : 27
    nom de l'étudiant : MOREAU	date d'anniversaire : 1992-4-29	âge : 27
    nom de l'étudiant : NIBEAUDEAU	date d'anniversaire : 1994-5-8	âge : 26
    nom de l'étudiant : NICOT	date d'anniversaire : 1993-5-31	âge : 26
    nom de l'étudiant : PAQUEREAU	date d'anniversaire : 1993-12-8	âge : 26
    nom de l'étudiant : PELE	date d'anniversaire : 1993-12-21	âge : 26
    nom de l'étudiant : PIGEON	date d'anniversaire : 1994-5-4	âge : 26
    nom de l'étudiant : POCHET	date d'anniversaire : 1994-3-28	âge : 25
    nom de l'étudiant : RAGUIDEAU	date d'anniversaire : 1991-3-31	âge : 28
    nom de l'étudiant : RAMDE	date d'anniversaire : 1994-5-30	âge : 25
    nom de l'étudiant : RINGARD	date d'anniversaire : 1994-8-11	âge : 25
    nom de l'étudiant : SALUDO	date d'anniversaire : 1994-12-8	âge : 25
    nom de l'étudiant : SAMSON	date d'anniversaire : 1993-1-12	âge : 26
    nom de l'étudiant : SHU	date d'anniversaire : 1991-4-15	âge : 28
    nom de l'étudiant : TALON	date d'anniversaire : 1995-5-1	âge : 25
    nom de l'étudiant : TROLAIS	date d'anniversaire : 1993-2-2	âge : 27
    nom de l'étudiant : WANG	date d'anniversaire : 1993-10-4	âge : 27
    nom de l'étudiant : YANG	date d'anniversaire : 1993-3-30	âge : 26
    nom de l'étudiant : ZHONG	date d'anniversaire : 1992-8-16	âge : 27 
