# Python TP9

## Lire les données dans le fichier (colonne E close qui correspond à la dernière valeur de l’intervalle ici 1 minute) et afficher la courbe.

![alt text](pic/myplot.png)

## Mettre en place une évaluation à partir du modèle naïf (basique) copie carbone qui considère que le cours monte s’il vient de monter et réciproquement qu’il va descendre s’il vient de descendre pendant la dernière minute.

    accuracy : 49.860979157608845
    
## Utiliser keras pour mettre en oeuvre un CNN 1-D avec une fenêtre de valeurs passées (taille à choisir, par exemple 120 minutes).

Base d'apprentissage :

    Input : Tableau d'exemple des h (ici 120) minute passé comprenant les 4 caractéristiques : cours en début de minute, max, min et fin de minute.
    Output : 1 si le cours debut de minute inférieur au cours de fin de minute

standardisation et normalisation des données par jeu de données avec sklearn

Base de validation :

    20% de la base d'apprentissage

Fonction de perte :

    Erreur quadratique moyenne

Optimiseur :

    Adam

Metriques :

    Binary_accuracy

Résultat CNN :

    Base d'apprentissage :
    loss: 0.4527 - binary_accuracy: 0.5473 
    Base de validation :
    val_loss: 0.4380 - val_binary_accuracy: 0.5620

