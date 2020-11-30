# Python TP5

## 1. Concevoir une base de données contenant les tables Communes, Departements, Regions

**Code:**

>        import sqlite3
>        import pandas as pd
>        
>        try:
>        
>            #Creation DB
>            db = sqlite3.connect('mydb')
>            cursor = db.cursor()
>        
>            #Creation des tables
>            cursor.execute('''CREATE TABLE IF NOT EXISTS
>                              Communes(IDCommune  INTEGER PRIMARY KEY, CodeCommune INTEGER, CodeDepartement TEXT, NomCommune TEXT, Population INTEGER)''')
>            cursor.execute('''CREATE TABLE IF NOT EXISTS
>                              Departements(CodeDepartement TEXT PRIMARY KEY, NomDepartement TEXT, CodeRegion INTEGER)''')
>            cursor.execute('''CREATE TABLE IF NOT EXISTS
>                              Region(CodeRegion INTEGER PRIMARY KEY, NomRegion TEXT)''')
>        
>            db.commit()
>        
>            #Insertion en base à partir des CSV        
>            cptID = 0
>            dataframe = pd.read_csv('communes.csv', sep=';', header=7, encoding = "ISO-8859-1")
>            for row in dataframe.itertuples(index=False):
>              cursor.execute('''INSERT INTO Communes(IDCommune,CodeCommune, CodeDepartement, NomCommune,Population)
>                                                  VALUES(?,?,?,?,?)''', (cptID, int(row[5]), row[2], row[6],int(row[9].replace(" ", ""))))
>        
>                cptID += 1
>        
>            dataframe = pd.read_csv('departements.csv', sep=';', header=7, encoding = "ISO-8859-1")
>            for row in dataframe.itertuples(index=False):
>                cursor.execute('''INSERT INTO Departements(CodeDepartement, NomDepartement, CodeRegion)
>                                                          VALUES(?,?,?)''', (row[2], row[3], int(row[0])))
>        
>            dataframe = pd.read_csv('regions.csv', sep=';', header=7, encoding = "ISO-8859-1")
>            for row in dataframe.itertuples(index=False):
>                cursor.execute('''INSERT INTO Region(CodeRegion, NomRegion)
>                                                          VALUES(?,?)''', (int(row[0]),row[1]))
>        
>            db.commit()
>  
>            #Selection des 10 premier champs de chaque table 
>            print("Communes :")        
>            cursor.execute('''SELECT IDCommune, CodeCommune, CodeDepartement, NomCommune, Population FROM Communes LIMIT 10''')
>            for row in cursor:
>                print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2],row[3],row[4]))
>            print("Departements :")          
>            cursor.execute('''SELECT CodeDepartement, NomDepartement, CodeRegion FROM Departements LIMIT 10''')
>            for row in cursor:
>                print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
>            print("Regions :")          
>            cursor.execute('''SELECT CodeRegion, NomRegion FROM Region LIMIT 10''')
>            for row in cursor:
>                print('{0} : {1}'.format(row[0], row[1]))
>        
>        # Catch the exception
>        except Exception as e:
>            # Roll back any change if something goes wrong
>            db.rollback()
>            raise e
>        finally:
>            # Close the db connection
>            db.close()

**Console (10 de chaque):**

    Communes :
    0 : 1, 01, L' Abergement-Clï¿½menciat, 780
    1 : 2, 01, L' Abergement-de-Varey, 240
    2 : 4, 01, Ambï¿½rieu-en-Bugey, 14888
    3 : 5, 01, Ambï¿½rieux-en-Dombes, 1666
    4 : 6, 01, Amblï¿½on, 114
    5 : 7, 01, Ambronay, 2618
    6 : 8, 01, Ambutrix, 763
    7 : 9, 01, Andert-et-Condon, 345
    8 : 10, 01, Anglefort, 1127
    9 : 11, 01, Apremont, 402
    Departements :
    01 : Ain, 82
    02 : Aisne, 22
    03 : Allier, 83
    04 : Alpes-de-Haute-Provence, 93
    05 : Hautes-Alpes, 93
    06 : Alpes-Maritimes, 93
    07 : Ardï¿½che, 82
    08 : Ardennes, 21
    09 : Ariï¿½ge, 73
    10 : Aube, 21
    Regions :
    1 : Guadeloupe
    2 : Martinique
    3 : Guyane
    4 : La Rï¿½union
    11 : ï¿½le-de-France
    21 : Champagne-Ardenne
    22 : Picardie
    23 : Haute-Normandie
    24 : Centre
    25 : Basse-Normandie



## 2. Calculer et afficher les populations totales de chaque département et région 

**Code**

>        import sqlite3
>        
>        
>        try:
>        
>            #Creation DB
>            db = sqlite3.connect('mydb')
>            cursor = db.cursor()
>        
>            print('Calcul de la population totale des départements à partir des communes : ')
>            cursor.execute('''SELECT
>                                Communes.CodeDepartement, NomDepartement, SUM(Population)
>                              FROM
>                                Communes INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
>                              GROUP BY
>                                Communes.CodeDepartement, NomDepartement
>                                ''')
>            for row in cursor:
>                print('Nom du departement : "{0}", Population totale : {1}'.format(row[1], row[2]))
>        
>            print('Calcul de la population totale des régions à partir des communes : ')
>            cursor.execute('''SELECT
>                                Departements.CodeRegion, NomRegion, SUM(Population)
>                              FROM
>                                Communes 
>                                INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
>                                INNER JOIN Region ON Departements.CodeRegion = Region.CodeRegion
>                                
>                              GROUP BY
>                                Departements.CodeRegion , NomDepartement
>                                ''')
>            for row in cursor:
>                print('Nom de la région: "{0}", Population totale : {1}'.format(row[1], row[2]))
>        
>        
>        # Catch the exception
>        except Exception as e:
>            # Roll back any change if something goes wrong
>            raise e
>        finally:
>            # Close the db connection
>            db.close()


**Console (10 de chaque)**

    Calcul de la population totale des départements à partir des communes  : 
    Nom du departement : "Ain", Population totale : 636916
    Nom du departement : "Aisne", Population totale : 554512
    Nom du departement : "Allier", Population totale : 353742
    Nom du departement : "Alpes-de-Haute-Provence", Population totale : 166726
    Nom du departement : "Hautes-Alpes", Population totale : 144640
    Nom du departement : "Alpes-Maritimes", Population totale : 1096741
    Nom du departement : "Ardï¿½che", Population totale : 330017
    Nom du departement : "Ardennes", Population totale : 289075
    Nom du departement : "Ariï¿½ge", Population totale : 158379
    Nom du departement : "Aube", Population totale : 314825
    
    
    Calcul de la population totale des régions à partir des communes : 
    Nom de la région: "Guadeloupe", Population totale : 409055
    Nom de la région: "Martinique", Population totale : 391837
    Nom de la région: "Guyane", Population totale : 246507
    Nom de la région: "La Rï¿½union", Population totale : 844741
    Nom de la région: "ï¿½le-de-France", Population totale : 12116367
    Nom de la région: "Champagne-Ardenne", Population totale : 1375674
    Nom de la région: "Picardie", Population totale : 1974614
    Nom de la région: "Haute-Normandie", Population totale : 1892928
    Nom de la région: "Centre", Population totale : 2641391
    Nom de la région: "Basse-Normandie", Population totale : 1523247



A vue d'oeil les populations calculées pour les régions et les départements correspondent exactement à celles figurants sur les csv.

# 3. Déterminer les communes ayant le meme nom et un département différent. Afficher le nom de la commune suivi de la liste des n° de départements 

**Code**

>        print('Liste des villes ayants le même nom (10 premières) : ')
>        cursor.execute('''SELECT
>                            Table1.NomCommune, Table2.NomCommune, GROUP_CONCAT(Table1.CodeDepartement, ',') AS CodeDepartement1,GROUP_CONCAT(Table2.CodeDepartement, ',') AS CodeDepartement2
>                          FROM
>                            Communes AS Table1 ,Communes AS Table2
>                          WHERE
>                            Table1.NomCommune = Table2.NomCommune and Table1.IDCommune <> Table2.IDCommune and Table1.CodeDepartement <> Table2.CodeDepartement
>                          GROUP BY Table1.NomCommune, Table2.NomCommune
>                          LIMIT 10
>                            ''')
>        for row in cursor:
>            li = row[2].split(',') + row[3].split(',') #Création d'une liste à partir des GROUP_CONCAT
>            li = list(set(li)) #Suppression des doublons
>            print(' Ville : "{0}", Départements : {1}'.format(row[0],li))

**Console (10 premiers)**

     Ville : "Abancourt", Départements : ['60', '59']
     Ville : "Aboncourt", Départements : ['57', '54']
     Ville : "Abzac", Départements : ['33', '16']
     Ville : "Achï¿½res", Départements : ['78', '18']
     Ville : "Acqueville", Départements : ['14', '50']
     Ville : "Aiglun", Départements : ['04', '06']
     Ville : "Aigremont", Départements : ['78', '89', '30', '52']
     Ville : "Aigueperse", Départements : ['63', '69']
     Ville : "Aigues-Vives", Départements : ['09', '34', '11', '30']
     Ville : "Ainvelle", Départements : ['88', '70']

# 4. Ecrire une fonction pour sauvegarder la base dans un fichier XML et une autre pour charger la base à partir de ce fichier.

**Code**

>       def exportDBToXML(nomFicXML,nomFicDB) :
>            try:
>                outfile = open(nomFicXML, "w")
>                db = sqlite3.connect(nomFicDB)
>                cursor = db.cursor()
>                outfile.write('<?xml version="1.0" ?>\n')
>                outfile.write('<Tables>\n')
>                outfile.write('<Communes>\n')
>                cursor.execute('''SELECT IDCommune, CodeCommune, CodeDepartement, NomCommune, Population FROM Communes''')
>                for row in cursor:
>                    print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2], row[3], row[4]))
>                    outfile.write('  <row>\n')
>                    outfile.write('    <IDCommune>%s</IDCommune>\n' % row[0])
>                    outfile.write('    <CodeCommune>%s</CodeCommune>\n' % row[1])
>                    outfile.write('    <CodeDepartement>%s</CodeDepartement>\n' % row[2])
>                    outfile.write('    <NomCommune>%s</NomCommune>\n' % row[3])
>                    outfile.write('    <Population>%s</Population>\n' % row[4])
>                    outfile.write('  </row>\n')
>        
>                outfile.write('</Communes>\n')
>        
>                outfile.write('<Departements>\n')
>                cursor.execute('''SELECT CodeDepartement, NomDepartement, CodeRegion FROM Departements LIMIT 10''')
>                for row in cursor:
>                    outfile.write('  <row>\n')
>                    outfile.write('    <CodeDepartement>%s</CodeDepartement>\n' % row[0])
>                    outfile.write('    <NomDepartement>%s</NomDepartement>\n' % row[1])
>                    outfile.write('    <CodeRegion>%s</CodeRegion>\n' % row[2])
>                    outfile.write('  </row>\n')
>                outfile.write('</Departements>\n')
>        
>        
>                outfile.write('<Regions>\n')
>                cursor.execute('''SELECT CodeRegion, NomRegion FROM Region LIMIT 10''')
>                for row in cursor:
>                    outfile.write('  <row>\n')
>                    outfile.write('    <CodeRegion>%s</CodeRegion>\n' % row[0])
>                    outfile.write('    <NomRegion>%s</NomRegion>\n' % row[1])
>                    outfile.write('  </row>\n')
>                outfile.write('</Regions>\n')
>                outfile.write('</Tables>\n')
>            except Exception as e:
>                raise e
>            finally:
>                outfile.close()
>        
>        
>        def exportXMLToDB(nomFicDB,nomFicXML):
>            try :
>                db = sqlite3.connect(nomFicDB)
>                cursor = db.cursor()
>        
>                # Creation des tables
>                cursor.execute('''CREATE TABLE IF NOT EXISTS
>                                          Communes(IDCommune  INTEGER PRIMARY KEY, CodeCommune INTEGER, CodeDepartement TEXT, NomCommune TEXT, Population INTEGER)''')
>                cursor.execute('''CREATE TABLE IF NOT EXISTS
>                                          Departements(CodeDepartement TEXT PRIMARY KEY, NomDepartement TEXT, CodeRegion INTEGER)''')
>                cursor.execute('''CREATE TABLE IF NOT EXISTS
>                                          Region(CodeRegion INTEGER PRIMARY KEY, NomRegion TEXT)''')
>        
>                db.commit()
>                dom = parse(nomFicXML)
>                tables = dom.getElementsByTagName("Tables")
>                communes = tables[0].getElementsByTagName( "Communes" )
>                communesRow = communes[0].getElementsByTagName( "row" )
>                cptID = 0
>                for commune in communesRow :
>                    cursor.execute('''INSERT INTO Communes(IDCommune,CodeCommune, CodeDepartement, NomCommune,Population)
>                                                                      VALUES(?,?,?,?,?)''',
>                                   (cptID,
>        
>                                   int(commune.getElementsByTagName("CodeCommune")[0].firstChild.data),
>                                    commune.getElementsByTagName("CodeDepartement")[0].firstChild.data,
>                                    commune.getElementsByTagName("NomCommune")[0].firstChild.data,
>                                    int(commune.getElementsByTagName("Population")[0].firstChild.data)))
>        
>                    cptID += 1
>        
>                departements = tables[0].getElementsByTagName( "Departements" )
>                departementsRow = departements[0].getElementsByTagName( "row" )
>                for departement in departementsRow:
>                    cursor.execute('''INSERT INTO Departements(CodeDepartement, NomDepartement, CodeRegion)
>                                                                      VALUES(?,?,?)''',
>                                   (departement.getElementsByTagName("CodeDepartement")[0].firstChild.data,
>                                    departement.getElementsByTagName("NomDepartement")[0].firstChild.data,
>                                    int(departement.getElementsByTagName("CodeRegion")[0].firstChild.data)))
>        
>                regions = tables[0].getElementsByTagName( "Regions" )
>                regionsRow = regions[0].getElementsByTagName( "row" )
>                for region in regionsRow:
>                    cursor.execute('''INSERT INTO Region(CodeRegion, NomRegion)
>                                                                      VALUES(?,?)''',
>                                   (int(region.getElementsByTagName("CodeRegion")[0].firstChild.data),
>                                    region.getElementsByTagName("NomRegion")[0].firstChild.data))
>                db.commit()
>        
>                    # Catch the exception
>            except Exception as e:
>                # Roll back any change if something goes wrong
>                db.rollback()
>                raise e
>            finally:
>                # Close the db connection
>                db.close()


Les conversion DB en XML et XML en DB via les fonctions ci-dessus fonctionnent parfaitement.

# 5. A partir du fichier communes-2016.csv et des dernières lignes de zones-2016.csv, ajouter une table NouvellesRegions et un champ à la table Departements. Calculer les populations de ces nouvelles régions avec les populations des anciennes communes.

**Mise à jour de départements**

>        #Ajout des nouveaux découpages de regions dans les départements
>        cursor.execute('ALTER TABLE Departements ADD COLUMN CodeNouvelleRegion INTEGER')
>        dataframe = pd.read_csv('communes-2016.csv', sep=';', header=5, encoding = "ISO-8859-1")
>        for row in dataframe.itertuples(index=False):
>            cursor.execute("UPDATE Departements SET CodeNouvelleRegion = "+str(row[3])+" WHERE CodeDepartement = '"+str(row[2])+"' ")

**Création et remplissage de la table nouvelle Région**

>       #Création table NouvelleRegion
>        cursor.execute('''CREATE TABLE IF NOT EXISTS
>                          NouvelleRegion(CodeNouvelleRegion INTEGER PRIMARY KEY, NomNouvelleRegion TEXT)''')
>        dataframe = pd.read_csv('zones-2016.csv', sep=';', header=5, encoding = "ISO-8859-1")
>        for row in dataframe.itertuples(index=False):
>            if str(row[0]) == "REG":
>                cursor.execute('''INSERT INTO NouvelleRegion(CodeNouvelleRegion, NomNouvelleRegion)
>                                                          VALUES(?,?)''', (int(row[1]), row[2]))

**Affichage des nouvelles populations de régions avec les anciennes communes**

>        print('Calcul de la population totale des nouvelles régions à partir des anciennes communes : ')
>        cursor.execute('''SELECT
>                            Departements.CodeNouvelleRegion, NomNouvelleRegion, SUM(Population)
>                          FROM
>                            Communes
>                            INNER JOIN Departements ON Communes.CodeDepartement = Departements.CodeDepartement
>                            INNER JOIN NouvelleRegion ON Departements.CodeNouvelleRegion = NouvelleRegion.CodeNouvelleRegion
>    
>                          GROUP BY
>                            Departements.CodeNouvelleRegion , NomNouvelleRegion
>                            ''')
>        for row in cursor:
>            print('Nom de la région: "{0}", Population totale : {1}'.format(row[1], row[2]))

**Console**

    Calcul de la population totale des nouvelles régions à partir des anciennes communes : 
    Nom de la région: "Guadeloupe", Population totale : 409055
    Nom de la région: "Martinique", Population totale : 391837
    Nom de la région: "Guyane", Population totale : 246507
    Nom de la région: "La Réunion", Population totale : 844741
    Nom de la région: "Île-de-France", Population totale : 12116367
    Nom de la région: "Centre-Val de Loire", Population totale : 2641391
    Nom de la région: "Bourgogne-Franche-Comté", Population totale : 2907114
    Nom de la région: "Normandie", Population totale : 3416175
    Nom de la région: "Nord-Pas-de-Calais-Picardie", Population totale : 6101843
    Nom de la région: "Alsace-Champagne-Ardenne-Lorraine", Population totale : 5679877
    Nom de la région: "Pays de la Loire", Population totale : 3765802
    Nom de la région: "Bretagne", Population totale : 3361496
    Nom de la région: "Aquitaine-Limousin-Poitou-Charentes", Population totale : 6010982
    Nom de la région: "Languedoc-Roussillon-Midi-Pyrénées", Population totale : 5827627
    Nom de la région: "Auvergne-Rhône-Alpes", Population totale : 7956770
    Nom de la région: "Provence-Alpes-Côte d'Azur", Population totale : 5039311
    Nom de la région: "Corse", Population totale : 325510

