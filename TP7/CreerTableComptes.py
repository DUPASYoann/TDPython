import sqlite3

try:

    #Creation DB
    db = sqlite3.connect('dbsitetest')
    cursor = db.cursor()

    #Creation des tables
    cursor.execute('''CREATE TABLE IF NOT EXISTS
                      Comptes(Pseudo TEXT PRIMARY KEY, MDP TEXT)''')

    db.commit()

    #Création des comptes

    #Compte Admin
    cursor.execute('''INSERT INTO Comptes(Pseudo, MDP)
                                              VALUES(?,?)''', ("ADMIN","ADMIN"))

    db.commit()

    #Affichage
    print("Comptes :")
    cursor.execute('''SELECT Pseudo, MDP FROM Comptes ''')
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