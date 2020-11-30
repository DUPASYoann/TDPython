import os


# Choisir un nom de fichier
def fonction1(param_texte_fonction):
    print("Entrez le nom du fichier :")
    param_texte_fonction["Nom du fichier"] = input()


# Ajouter un texte
def fonction2(param_texte_fonction):
    if param_texte_fonction["Nom du fichier"] == "":
        print("Impossible d'écrire, nom du fichier vide")
    else:
        with open(param_texte_fonction["Nom du fichier"] + ".txt", "a") as objet_fichier:
            print("Votre texte : ")
            param_texte_fonction["Texte"] = input()
            objet_fichier.write(param_texte_fonction["Texte"] + "\n")
9

# Afficher le fichier complet
def fonction3(param_texte_fonction):

    # if os.path.isfile(param_texte_fonction["Nom du fichier"] + ".txt"):
    #     with open(param_texte_fonction["Nom du fichier"] + ".txt", "r") as objet_fichier:
    #         param_texte_fonction["Texte"] = objet_fichier.read()
    #         print(param_texte_fonction["Texte"])
    # else:
    #     print("Impossible de vider le fichier, nom du fichier invalide")

    try:
        assert os.path.isfile(param_texte_fonction["Nom du fichier"] + ".txt")
        with open(param_texte_fonction["Nom du fichier"] + ".txt", "r") as objet_fichier:
            param_texte_fonction["Texte"] = objet_fichier.read()
            print(param_texte_fonction["Texte"])
    except AssertionError:
        print("Impossible de vider le fichier, nom du fichier invalide")


# Vider le fichier
def fonction4(param_texte_fonction):
    if os.path.isfile(param_texte_fonction["Nom du fichier"] + ".txt"):
        open(param_texte_fonction["Nom du fichier"] + ".txt", "w")
    else:
        print("Impossible de lire, nom du fichier invalide")


if __name__ == '__main__':
    print('Bonjour le monde !')
    print("")
    print("1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le "
          "fichier complet, 4. Vider le fichier, 9. Quitter le programme.")
    choix = input()
    param_texte = {"Nom du fichier": "", "Texte": ""}

    while choix != "9":
        if choix == '1':
            fonction1(param_texte)
        elif choix == '2':
            fonction2(param_texte)
        elif choix == '3':
            fonction3(param_texte)
        elif choix == '4':
            fonction4(param_texte)
        print("1. Choisir un nom de fichier, 2.Ajouter un texte (que vous demanderez à l’utilisateur), 3. Afficher le "
              "fichier complet, 4. Vider le fichier, 9. Quitter le programme.")
        choix = input()
