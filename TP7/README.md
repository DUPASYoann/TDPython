# Python TP7

## 1. Créer un serveur web 

**Code: (Server.py)**

>       import cgitb; cgitb.enable()  # Permet d'afficher les logs CGI
>       import http.server
>       PORT = 8001
>       server_address = ('', PORT)
>       server = http.server.HTTPServer
>       handler = http.server.CGIHTTPRequestHandler
>       handler.cgi_directories = ['/']
>       print("Serveur actif sur le port :", PORT)
>       httpd = server(server_address, handler)
>       httpd.serve_forever()


 
**Console:**

    Serveur actif sur le port : 8001

## 2. Créer une page web dans un fichier index.py

**Code: (Index.py)**

>       #!/usr/bin/env python
>       print("Content-type: text/html; charset=utf-8\n")
>       html = """<!DOCTYPE html>
>       <head>
>       <title>TP7</title>
>       </head>
>       <body>
>       <h1> Question 2 TP 7  : </h1>
>       <p>Ceci est le contenu du "index.py" </p>
>       </body>
>       </html>
>       """
>       print(html)

**Console du serveur:**

    127.0.0.1 - - [02/Nov/2020 09:59:03] "GET /index.py HTTP/1.1" 200 -
    127.0.0.1 - - [02/Nov/2020 09:59:03] command: C:\Users\PC_LEO\anaconda3\python.exe -u C:\Users\PC_LEO\TDPython\TP7\index.py ""
    127.0.0.1 - - [02/Nov/2020 09:59:03] CGI script exited OK

**Rendu sur navigateur:**    
![alt text](Q2.png "Rendu sur navigateur")

## 3. Utiliser cette page pour stocker ou récupérer des informations envoyées par le web sur le serveur

**index.py**

>        #!/usr/bin/env python
>        import cgi
>        import csv
>        
>        print("Content-type: text/html; charset=utf-8\n")
>        html = """<!DOCTYPE html>
>        <head>
>         <title>TP7</title>
>        </head>
>        <body>
>         <h1> Q3. du TP7 de python</h1>
>          <h2> Envoyer un mot au serveur </h2>
>           <form action="/Traitements.py" method="post">
>           <input type="text" name="mot" value="" />
>           <input type="submit" name="send" value="Envoyer information au serveur">
>           </form>
>          
>          <h2> Liste des mots envoyés </h2>"""
>        
>        
>        file = open("mots.txt", "r")
>        for line in file:
>            html = html + "<p>" +line+ "<p>"
>        
>        html = html + """
>        </body>
>        </html>
>        """
>        print(html)


**Traitements.py**

>        import cgi
>        form = cgi.FieldStorage()
>        mot = form.getvalue("mot")
>        
>        f = open("mots.txt", "a")
>        f.writelines("\n"+mot)
>       f.close()
>        
>        
>        print("Content-type: text/html; charset=utf-8\n")
>        print ("""
>        <body>
>            <H3>Le mot <mark>"""+mot+"""</mark> à bien été ajouté ! </H3>
>            <form action="/index.py" method="post">
>            <input type = "submit" name = "send" value = "Retour au menu">
>            </form>
>        </body>    
>            """)

**Ajout d'un mot au serveur :**
    
![alt text](Q31.png "Ajout d'un mot au serveur")

**Réponse du serveur :**

![alt text](Q32.png "Traitements")

**Vérification de l'ajout sur la page "index.py" :**

![alt text](Q33.png "Vérification de l'ajout")

## 4. Permettre l’accès aux données qu’aux utilisateurs avec un login+mdp enregistré

**Création d'une base de données avec des comptes enregistrés**

>        import sqlite3
>        
>        try:
>        
>            #Creation DB
>            db = sqlite3.connect('dbsitetest')
>            cursor = db.cursor()
>        
>            #Creation des tables
>            cursor.execute('''CREATE TABLE IF NOT EXISTS
>                              Comptes(Pseudo TEXT PRIMARY KEY, MDP TEXT)''')
>        
>            db.commit()
>        
>            #Création des comptes
>        
>            #Compte Admin
>            cursor.execute('''INSERT INTO Comptes(Pseudo, MDP)
>                                                      VALUES(?,?)''', ("ADMIN","ADMIN"))
>        
>            db.commit()
>        
>            #Affichage
>            print("Comptes :")
>            cursor.execute('''SELECT Pseudo, MDP FROM Comptes ''')
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

**Création d'une page d'authetification**

>       print("Content-type: text/html; charset=utf-8\n")
>       print("""<H3>Veuillez vous identifier, SVP :</H3> 
>        <FORM ACTION = "index.py">
>        Pseudo : <INPUT NAME = "pseudo"> <BR> 
>        Mot de passe : <INPUT NAME = "mdp"> <BR>
>        <INPUT TYPE = "submit" VALUE = "OK">
>        </FORM>""")


**Implémentation d'une fonction de vérification au début de chaque page**

>        def log():
>            obSess = Session()
>            form = cgi.FieldStorage()
>            obSess.pseudo = form.getvalue("pseudo")
>            obSess.mdp = form.getvalue("mdp")
>            db = sqlite3.connect("dbsitetest")
>            cursor = db.cursor()
>            cursor.execute('''SELECT Pseudo, MDP FROM Comptes ''')
>            for row in cursor:
>                 if obSess.pseudo == row[0] and  obSess.mdp==row[1]:
>                     return True
>            return False
>
>        print("Content-type: text/html; charset=utf-8\n")
>        if not log() :
>            print("""<h1>Accès impossible, vous n'etes pas connectés</h1>""")
>        else :
>        ...
>        ## CODE DE LA PAGE ##
>        ...

**Connexion au compte ADMIN précedemment créé**

![alt text](Q4.png "")

![alt text](Q41.png "")

--> Connexion bien reussie

**Connexion à un compte inexistant**

![alt text](Q42.png "")

![alt text](Q43.png "")

--> Erreur de connexion, impossible d'acceder à la page

