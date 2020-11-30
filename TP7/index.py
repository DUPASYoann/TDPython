#!/usr/bin/env python
import cgi
import csv
import sqlite3

from requests import Session

def log():
    obSess = Session()
    form = cgi.FieldStorage()
    obSess.pseudo = form.getvalue("pseudo")
    obSess.mdp = form.getvalue("mdp")
    db = sqlite3.connect("dbsitetest")
    cursor = db.cursor()
    cursor.execute('''SELECT Pseudo, MDP FROM Comptes ''')
    for row in cursor:
         if obSess.pseudo == row[0] and  obSess.mdp==row[1]:
             return True
    return False


print("Content-type: text/html; charset=utf-8\n")

if not log() :
    print("""<h1>Accès impossible, vous n'etes pas connectés</h1>""")
else :
    html = ""
    html = html + """<!DOCTYPE html>
    <head>
     <title>TP7</title>
    </head>
    <body>
     <h1> Q3. du TP7 de python</h1>
      <h2> Envoyer un mot au serveur </h2>
      <form action="/Traitements.py" method="post">
      <input type="text" name="mot" value="" />
      <input type="submit" name="send" value="Envoyer information au serveur">
      </form>
      
      <h2> Liste des mots envoyés </h2>"""


    file = open("mots.txt", "r")
    for line in file:
        html = html + "<p>" +line+ "<p>"

    html = html + """
    </body>
    </html>
    """
    print(html)

