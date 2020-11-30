# Python TP6

## Créer un tableau de dimension 3 avec un shape de (4, 3, 2) remplit avec des nombres aléatoires. Vous afficherez les attributs du tableau : ndim, shape, size, dtype, itemsize, data.

     ndim : 3
     shape : (4, 3, 2)
     size : 24
     type : int32
     data : 
        [[[0 0]
          [1 0]
          [0 1]]
         [[0 1]
          [0 1]
          [1 1]]
         [[0 0]
          [1 1]
          [0 1]]
         [[1 0]
          [0 0]
          [0 1]]]

## er 2 matrices 3x3 initialisées avec les entiers de 0 à 8 pour la 1e et de 2 à 10 pour la 2e puis calculer le produit des 2 (différence entre * et dot). Transposer une matrice.

     tableau 1 :
      [[0 1 2]
       [3 4 5]
       [6 7 8]]
     tableau 2 :
      [[ 2  3  4]
       [ 5  6  7]
       [ 8  9 10]]
     multiplication :
      [[ 0  3  8]
       [15 24 35]
       [48 63 80]]
     produit scalaire :
      [[ 21  24  27]
       [ 66  78  90]
       [111 132 153]]
     transposé :
      [[0 3 6]
       [1 4 7]
       [2 5 8]]
      
## Calculer le déterminant et l’inverse d’une matrice. Résoudre un système d’équations linéaires. Calculer les valeurs et vecteurs propres d’une matrice.

    tableau :
     [[2, 2, 1], [1, 3, 1], [6, 2, 1]]
    determinant :
     -4.0
    inverse :
     [[-0.25  0.    0.25]
      [-1.25  1.    0.25]
      [ 4.   -2.   -1.  ]]
    solution equation :
     [ 0.5  1.5 -3. ]
    vecteur propres :
     (array([ 5.70156212, -0.70156212,  1.        ]), array([[-0.45197014, -0.20368041,  0.16903085],
            [-0.45197014, -0.20368041, -0.50709255],
            [-0.76905526,  0.95761609,  0.84515425]]))
    valeurs propres :
     [ 5.70156212 -0.70156212  1.        ]
     
## Approcher un ensemble de points par une courbe (optimize.curve_fit ou interpolate.interp1d).

![alt text](pic/myplot.png)

## Lire une image jpeg et afficher l’image originale et réduite en taille. La bibliothèque Scipy ne traite plus les images alors utiliser Pillow (qui est un fork de PIL).

![alt text](raclette.jpg)