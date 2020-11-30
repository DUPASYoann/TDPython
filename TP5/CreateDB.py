import sqlite3
import pandas as pd

try:

    #Creation DB
    db = sqlite3.connect('mydb')
    cursor = db.cursor()

    #Creation des tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Communes(IDCommune  INTEGER PRIMARY KEY, CodeCommune INTEGER, CodeDepartement TEXT, NomCommune TEXT, Population INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Departements(CodeDepartement TEXT PRIMARY KEY, NomDepartement TEXT, CodeRegion INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Region(CodeRegion INTEGER PRIMARY KEY, NomRegion TEXT)''')

    db.commit()


    cptID = 0
    dataframe = pd.read_csv('communes.csv', sep=';', header=7, encoding = "ISO-8859-1")
    for row in dataframe.itertuples(index=False):
        cursor.execute('''INSERT INTO Communes(IDCommune,CodeCommune, CodeDepartement, NomCommune,Population)
                                                  VALUES(?,?,?,?,?)''', (cptID, int(row[5]), row[2], row[6],int(row[9].replace(" ", ""))))

        cptID += 1

    dataframe = pd.read_csv('departements.csv', sep=';', header=7, encoding = "ISO-8859-1")
    for row in dataframe.itertuples(index=False):
        cursor.execute('''INSERT INTO Departements(CodeDepartement, NomDepartement, CodeRegion)
                                                  VALUES(?,?,?)''', (row[2], row[3], int(row[0])))

    dataframe = pd.read_csv('regions.csv', sep=';', header=7, encoding = "ISO-8859-1")
    for row in dataframe.itertuples(index=False):
        cursor.execute('''INSERT INTO Region(CodeRegion, NomRegion)
                                                  VALUES(?,?)''', (int(row[0]),row[1]))

    db.commit()
    print("Communes :")
    cursor.execute('''SELECT IDCommune, CodeCommune, CodeDepartement, NomCommune, Population FROM Communes LIMIT 10''')
    for row in cursor:
        print('{0} : {1}, {2}, {3}, {4}'.format(row[0], row[1], row[2],row[3],row[4]))
    print("Departements :")
    cursor.execute('''SELECT CodeDepartement, NomDepartement, CodeRegion FROM Departements LIMIT 10''')
    for row in cursor:
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))
    print("Regions :")
    cursor.execute('''SELECT CodeRegion, NomRegion FROM Region LIMIT 10''')
    for row in cursor:
        print('{0} : {1}'.format(row[0], row[1]))

# Catch the exception
except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()