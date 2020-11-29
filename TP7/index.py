#!/usr/bin/env python
import cgi
import csv

print("Content-type: text/html; charset=utf-8\n")
html = """<!DOCTYPE html>
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