import sqlite3
from xml.dom.minidom import parse, parseString
import pandas as pd

def exportDBToXML(nomFicXML,nomFicDB) :
    try:
        outfile = open(nomFicXML, "w")
        db = sqlite3.connect(nomFicDB)
        cursor = db.cursor()
        outfile.write('<?xml version="1.0" ?>\n')
        outfile.write('<Tables>\n')
        outfile.write('<Communes>\n')
        cursor.execute('''SELECT IDCommune, CodeCommune, CodeDepartement, NomCommune, Population FROM Communes''')
        for row in cursor:
            print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
            outfile.write('  <row>\n')
            outfile.write('    <IDCommune>%s</IDCommune>\n' % row[0])
            outfile.write('    <CodeCommune>%s</CodeCommune>\n' % row[1])
            outfile.write('    <CodeDepartement>%s</CodeDepartement>\n' % row[2])
            outfile.write('    <NomCommune>%s</NomCommune>\n' % row[3])
            outfile.write('    <Population>%s</Population>\n' % row[4])
            outfile.write('  </row>\n')

        outfile.write('</Communes>\n')

        outfile.write('<Departements>\n')
        cursor.execute('''SELECT CodeDepartement, NomDepartement, CodeRegion FROM Departements LIMIT 10''')
        for row in cursor:
            outfile.write('  <row>\n')
            outfile.write('    <CodeDepartement>%s</CodeDepartement>\n' % row[0])
            outfile.write('    <NomDepartement>%s</NomDepartement>\n' % row[1])
            outfile.write('    <CodeRegion>%s</CodeRegion>\n' % row[2])
            outfile.write('  </row>\n')
        outfile.write('</Departements>\n')


        outfile.write('<Regions>\n')
        cursor.execute('''SELECT CodeRegion, NomRegion FROM Region LIMIT 10''')
        for row in cursor:
            outfile.write('  <row>\n')
            outfile.write('    <CodeRegion>%s</CodeRegion>\n' % row[0])
            outfile.write('    <NomRegion>%s</NomRegion>\n' % row[1])
            outfile.write('  </row>\n')
        outfile.write('</Regions>\n')
        outfile.write('</Tables>\n')
    except Exception as e:
        raise e
    finally:
        outfile.close()


def exportXMLToDB(nomFicDB,nomFicXML):
    try :
        db = sqlite3.connect(nomFicDB)
        cursor = db.cursor()

        # Creation des tables
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                                  Communes(IDCommune  INTEGER PRIMARY KEY, CodeCommune INTEGER, CodeDepartement TEXT, NomCommune TEXT, Population INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                                  Departements(CodeDepartement TEXT PRIMARY KEY, NomDepartement TEXT, CodeRegion INTEGER)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS
                                  Region(CodeRegion INTEGER PRIMARY KEY, NomRegion TEXT)''')

        db.commit()
        dom = parse(nomFicXML)
        tables = dom.getElementsByTagName("Tables")
        communes = tables[0].getElementsByTagName( "Communes" )
        communesRow = communes[0].getElementsByTagName( "row" )
        cptID = 0
        for commune in communesRow :
            cursor.execute('''INSERT INTO Communes(IDCommune,CodeCommune, CodeDepartement, NomCommune,Population)
                                                              VALUES(?,?,?,?,?)''',
                           (cptID,

                           int(commune.getElementsByTagName("CodeCommune")[0].firstChild.data),
                            commune.getElementsByTagName("CodeDepartement")[0].firstChild.data,
                            commune.getElementsByTagName("NomCommune")[0].firstChild.data,
                            int(commune.getElementsByTagName("Population")[0].firstChild.data)))

            cptID += 1

        departements = tables[0].getElementsByTagName( "Departements" )
        departementsRow = departements[0].getElementsByTagName( "row" )
        for departement in departementsRow:
            cursor.execute('''INSERT INTO Departements(CodeDepartement, NomDepartement, CodeRegion)
                                                              VALUES(?,?,?)''',
                           (departement.getElementsByTagName("CodeDepartement")[0].firstChild.data,
                            departement.getElementsByTagName("NomDepartement")[0].firstChild.data,
                            int(departement.getElementsByTagName("CodeRegion")[0].firstChild.data)))

        regions = tables[0].getElementsByTagName( "Regions" )
        regionsRow = regions[0].getElementsByTagName( "row" )
        for region in regionsRow:
            cursor.execute('''INSERT INTO Region(CodeRegion, NomRegion)
                                                              VALUES(?,?)''',
                           (int(region.getElementsByTagName("CodeRegion")[0].firstChild.data),
                            region.getElementsByTagName("NomRegion")[0].firstChild.data))
        db.commit()

            # Catch the exception
    except Exception as e:
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
    finally:
        # Close the db connection
        db.close()


try:

    #Creation DB
    db = sqlite3.connect('mydb')
    cursor = db.cursor()

    print('Calcul de la population totale des départements à partir des communes : ')
    cursor.execute('''SELECT
                        Communes.CodeDepartement, NomDepartement, SUM(Population)
                      FROM
                        Communes INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
                      GROUP BY
                        Communes.CodeDepartement, NomDepartement
                        ''')
    for row in cursor:
        print('Nom du departement : "{0}", Population totale : {1}'.format(row[1], row[2]))

    print('Calcul de la population totale des régions à partir des communes : ')
    cursor.execute('''SELECT
                        Departements.CodeRegion, NomRegion, SUM(Population)
                      FROM
                        Communes
                        INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
                        INNER JOIN Region ON Departements.CodeRegion = Region.CodeRegion

                      GROUP BY
                        Departements.CodeRegion , NomRegion
                        ''')
    for row in cursor:
        print('Nom de la région: "{0}", Population totale : {1}'.format(row[1], row[2]))


    print('Liste des villes ayants le même nom (10 premières) : ')
    cursor.execute('''SELECT
                        Table1.NomCommune, Table2.NomCommune, GROUP_CONCAT(Table1.CodeDepartement, ',') AS CodeDepartement1,GROUP_CONCAT(Table2.CodeDepartement, ',') AS CodeDepartement2
                      FROM
                        Communes AS Table1 ,Communes AS Table2
                      WHERE
                        Table1.NomCommune = Table2.NomCommune and Table1.IDCommune <> Table2.IDCommune and Table1.CodeDepartement <> Table2.CodeDepartement
                      GROUP BY Table1.NomCommune, Table2.NomCommune
                      LIMIT 10
                        ''')
    for row in cursor:
        li = row[2].split(',') + row[3].split(',') #Création d'une liste à partir des GROUP_CONCAT
        li = list(set(li)) #Suppression des doublons
        print(' Ville : "{0}", Départements : {1}'.format(row[0],li))

    #Test exportation et importation en XML
    exportDBToXML("test.xml","mydb")
    exportXMLToDB("mydb2","test.xml")

    #Ajout des nouveaux découpages de regions dans les départements
    cursor.execute('ALTER TABLE Departements ADD COLUMN CodeNouvelleRegion INTEGER')
    dataframe = pd.read_csv('communes-2016.csv', sep=';', header=5, encoding = "ISO-8859-1")
    for row in dataframe.itertuples(index=False):
        cursor.execute("UPDATE Departements SET CodeNouvelleRegion = "+str(row[3])+" WHERE CodeDepartement = '"+str(row[2])+"' ")

    #Création table NouvelleRegion
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      NouvelleRegion(CodeNouvelleRegion INTEGER PRIMARY KEY, NomNouvelleRegion TEXT)''')
    dataframe = pd.read_csv('zones-2016.csv', sep=';', header=5, encoding = "ISO-8859-1")
    for row in dataframe.itertuples(index=False):
        if str(row[0]) == "REG":
            cursor.execute('''INSERT INTO NouvelleRegion(CodeNouvelleRegion, NomNouvelleRegion)
                                                      VALUES(?,?)''', (int(row[1]), row[2]))
    db.commit()
    cursor.execute('''SELECT CodeNouvelleRegion, NomNouvelleRegion FROM NouvelleRegion''')
    for row in cursor:
        print('{0} : {1}'.format(row[0], row[1]))

    print('Calcul de la population totale des nouvelles régions à partir des anciennes communes : ')
    cursor.execute('''SELECT
                        Departements.CodeNouvelleRegion, NomNouvelleRegion, SUM(Population)
                      FROM
                        Communes
                        INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
                        INNER JOIN NouvelleRegion ON Departements.CodeNouvelleRegion = NouvelleRegion.CodeNouvelleRegion

                      GROUP BY
                        Departements.CodeNouvelleRegion , NomNouvelleRegion
                        ''')
    for row in cursor:
        print('Nom de la région: "{0}", Population totale : {1}'.format(row[1], row[2]))

# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    raise e
finally:
    # Close the db connection
    db.close()


