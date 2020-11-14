class Date:
    annee: int
    mois: int
    jour: int

    def __init__(self, jour=1, mois=1, annee=1960):
        """
        Constructeur de la classe Date

        :param jour: jour de la date
        :type jour: int
        :param mois: mois de la date
        :type mois: int
        :param annee: année de la date
        :type annee: int
        """

        if jour < 0 or jour > 31:
            raise ValueError("le jour doit être compris entre 1 et 31")
        if mois < 0 or mois > 12:
            raise ValueError("le mois doit être compris entre 1 et 12")

        self.jour = jour
        self.mois = mois
        self.annee = annee

    @staticmethod
    def from_iso_format(iso_format="01/01/1960"):
        sep = iso_format.split("/")
        return Date(int(sep[0]), int(sep[1]), int(sep[2]))

    def __eq__(self, other: 'Date') -> bool:
        """ Surcharge de l'opérateur == """
        if isinstance(other, Date):
            if self.jour == other.jour:
                if self.mois == other.mois:
                    if self.annee == other.annee:
                        return True
        return False

    def __lt__(self, other: 'Date') -> bool:
        """ Surcharge de l'opérateur < """
        if isinstance(other, Date):
            if self.annee < other.annee:
                return True
            elif self.annee == other.annee:
                if self.mois < other.mois:
                    return True
                elif self.mois == other.mois:
                    if self.jour < other.jour:
                        return True
        return False

    def __str__(self):
        return "" + str(self.annee) + "-" + str(self.mois) + "-" + str(self.jour)


if __name__ == "__main__":
    date1 = Date(31, 5, 2020)
    date2 = Date(6, 9, 2020)

    print(date1 == date2)
    print(date1 < date2)
    print(date2 < date1)
