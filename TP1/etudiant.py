from TP1.date import Date
import datetime
import pandas as pd


class Etudiant:
    nombre_de_classe: int = 0

    def __init__(self, prenom="", nom="", anniversaire=Date()):
        """Constructeur de la classe Etudiant"""
        self.prenom = prenom
        self.nom = nom
        if isinstance(anniversaire, Date):
            self.anniversaire = anniversaire
        elif isinstance(anniversaire, str):
            self.anniversaire = Date.from_iso_format(anniversaire)
        else:
            self.anniversaire = Date()
        Etudiant.nombre_de_classe += 1

    @property
    def adresse_lec(self):
        return self.prenom + "." + self.nom + "@etu.univ-tours.fr"

    @property
    def age(self):
        today = datetime.date.today()
        years = today.year - self.anniversaire.annee
        if today.month < self.anniversaire.mois:
            years -= 1
        else:
            if today.day < self.anniversaire.jour:
                years -= 1
        return years


def fiche_extractor(fiche_path):
    assert isinstance(fiche_path, str)
    dataframe = pd.read_csv(fiche_path, sep=';', header=None)
    students = []
    for data in dataframe.itertuples(index=False):
        students.append(Etudiant(data[1], data[0], data[2]))
    return students


if __name__ == '__main__':

    etudiant1 = Etudiant("Paul", "Dupont", Date(22, 2, 1998))
    print("âge de l'étudiant Paul Dupont né le 22/02/1998")
    print(etudiant1.age)
    print("")

    etudiant2 = Etudiant("Michel", "Martin", Date(8, 8, 2000))
    print("adresse étudiante de Michel Martin")
    print(etudiant2.adresse_lec)
    print("")

    print("liste des étudiant depuis le ficheetu.csv")
    for student in fiche_extractor("../../fichetu.csv"):
        print("nom de l'étudiant : " + student.nom + "\tdate d'anniversaire : " + student.anniversaire.__str__() +
              "\tâge : " + student.age.__str__())
