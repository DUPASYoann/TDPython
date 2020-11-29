import cgi
form = cgi.FieldStorage()
mot = form.getvalue("mot")

f = open("mots.txt", "a")
f.writelines("\n"+mot)
f.close()


print("Content-type: text/html; charset=utf-8\n")
print ("""
<body>
    <H3>Le mot <mark>"""+mot+"""</mark> à bien été ajouté ! </H3>
    <form action="/index.py" method="post">
    <input type = "submit" name = "send" value = "Retour au menu">
    </form>
</body>    
    """)

