import hashlib
import getpass
import pandas

from Crypto.Cipher import AES


def enregistrement_utilisateur(sel_fixe_eu, fichier_eu, u=getpass.getuser()):

    try:
        p = getpass.win_getpass()
        sel = u + sel_fixe_eu
        mdp_sale = p + sel
        mdp_sale_hach = hashlib.sha512(mdp_sale.encode()).hexdigest()
    except Exception as error:
        print("Error : ", error)
    else:
        fichier_eu.write(u + "," + mdp_sale_hach + "\n")


def recherche_utilisateur(fichier_ru, user_ru, password_ru, sel_fixe_ru):

    sel = user_ru + sel_fixe_ru
    mdp_sale = password_ru + sel
    mdp_sale_hach = hashlib.sha512(mdp_sale.encode()).hexdigest()
    dataframe = pandas.read_csv(fichier_ru)
    for data in dataframe.itertuples(index=False):
        if data[0] == user_ru and data[1] == mdp_sale_hach:
            return True
    return False


def enregistrement(sel_fixe, utilisateur):

    with open("mot_de_passe.txt", "a") as fichier:
        enregistrement_utilisateur(sel_fixe, fichier, utilisateur)


def login(sel_fixe, utilisateur):

    password = input("Password : ")
    result = recherche_utilisateur("mot_de_passe.txt", utilisateur, password, sel_fixe)
    return result


def chiffrement(fichier_a_chiffre, destination_chiffrement, user, sel_fixe):

    password_fichier_chiffrement = input("Password pour chiffrement : ")
    sel = user + sel_fixe
    mdp_sale = password_fichier_chiffrement + sel
    mdp_sale_hach = hashlib.sha512(mdp_sale.encode()).digest()
    mdp_sale_hach_16_bytes = mdp_sale_hach[:16]

    f = open(fichier_a_chiffre, "rb")
    data = f.read()
    f.close()

    key = mdp_sale_hach_16_bytes
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(destination_chiffrement, "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()


def dechiffrement(destination_dechiffrement, fichier_chiffrer, user, sel_fixe):

    password_fichier_chiffrement = input("Password pour chiffrement : ")
    sel = user + sel_fixe
    mdp_sale = password_fichier_chiffrement + sel
    mdp_sale_hach = hashlib.sha512(mdp_sale.encode()).digest()
    mdp_sale_hach_16_bytes = mdp_sale_hach[:16]

    file_in = open(fichier_chiffrer, "rb")
    nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

    # let's assume that the key is somehow available again
    cipher = AES.new(mdp_sale_hach_16_bytes, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

    file_out = open(destination_dechiffrement + "fichier_dechiffrer", "w")
    file_out.write(data.decode("utf-8"))
    file_out.close()


if __name__ == "__main__":

    # paramètres
    _sel_fixe = "FIXE"
    _fichier_a_chiffre = "a_chiffrer/fichier.txt"
    _destination_chiffrement = "fichier_chiffrer/encrypted.bin"
    _dossier_dechiffrement = "dechiffrer/"

    # Enregistrement
    print("### ENREGISTREMENT ###")
    _utilisateur = input("Votre nom d'utilisateur : ")
    if _utilisateur != "":
        enregistrement(_sel_fixe, _utilisateur)

    # Login
    print("### LOGIN ###")
    _utilisateur = input("Votre nom d'utilisateur : ")
    if _utilisateur != "":
        print(login(_sel_fixe, _utilisateur))

    # Chiffrement de fichier
    print("### CHIFFREMENT ###")
    _utilisateur = input("Votre nom d'utilisateur : ")
    if _utilisateur != "":
        chiffrement(_fichier_a_chiffre, _destination_chiffrement, _utilisateur, _sel_fixe)

    # Déchiffrement
    print("### DECHIFFREMENT ###")
    _utilisateur = input("Votre nom d'utilisateur : ")
    if _utilisateur != "":
        dechiffrement(_dossier_dechiffrement, _destination_chiffrement, _utilisateur, _sel_fixe)

