print("Content-type: text/html; charset=utf-8\n")
print("""<H3>Veuillez vous identifier, SVP :</H3>

<FORM ACTION = "index.py">
Pseudo : <INPUT NAME = "pseudo"> <BR> 
Mot de passe : <INPUT NAME = "mdp"> <BR>
<INPUT TYPE = "submit" VALUE = "OK">
</FORM>""")