# -*- coding: utf-8 -*-
#################################################
# Kepler - modélisation - satellites de Jupiter #
#################################################


######################### NE PAS MODIFIER CETTE PARTIE ##################################

import numpy as np   # bibibliotèque numpy
import matplotlib.pyplot as plt # bibliotèque matplotlib.pyplot
import csv # 'csv' : 'coma separated values' (lecture dans les fichiers .csv)

# La fonction 'readCSV' permet de lire une colonne du fichier .csv
# Les valeurs de la colonne 'n' sont ajoutées progressivement dans une liste
# avec remplacement des virgules ',' dans les nombres par des points '.'
def readCSV(fichier,sep,n):  # (nom-fichier, séparateur, numéro-colonne)
    file = open(fichier,"r")  # ouverture du fichier en lecture
    reader = csv.reader(file, delimiter = sep)
    col = []
    for row in reader:
        try:
            notation_point = row[n].replace(",",".") # remplacement de , par .
            col.append(float(notation_point))  # remplissage de la liste
        except:
            pass
    file.close()
    return col   # retourne la liste des nombres exprimés avec des points

##########################################################################################



################ CETTE PARTIE INCLUT DES MODIFICATIONS A APPORTER PAR LE CANDIDAT #########

# Récupération des données des colonnes du fichier sous forme de listes
TListe =  readCSV("Table-Satellites-Galilee.csv", "\t",2)  # A MODIFIER PAR LE CANDIDAT
aListe =  readCSV("Table-Satellites-Galilee.csv", "\t",4)  # A MODIFIER PAR LE CANDIDAT

#  Conversions des listes en tableaux
# (pour anticiper sur les futurs calculs de régression)
T = np.array(TListe) # pour convertir la liste en tableau numpy à une dimension
a = np.array(aListe) # pour convertir la liste en tableau numpy à une dimension

# Modélisation
xreg = (10**4*a)**2  # grandeur en abscisse A MODIFIER PAR LE CANDIDAT
y = T                # grandeur en ordonnée A MODIFIER PAR LE CANDIDAT

##########################################################################################


######################### NE PAS MODIFIER CETTE PARTIE ###################################
### Calculs des différents termes pour la modélisation affine
sumxreg=np.sum(xreg)  # calcul de la somme des xi
sumy=np.sum(y)  # calcul de la somme des yi
sumxregy=np.sum(xreg*y) # calcul de la somme des xi*yi
sumxreg2=np.sum(xreg*xreg)
moyennexreg=np.mean(xreg)
moyenney=np.mean(y)

n = len(xreg) # nombres des points pour la modélisation affine

###   modèle utilisé pour la modélisation affine du type y = k*x + b
###
k=(n*sumxregy-sumxreg*sumy)/(n*sumxreg2-sumxreg**2) # pente
b=moyenney-k*moyennexreg    # ordonnée à l'origine
ymodelise=k*xreg+b  # droite de modélisation

###  Représentation graphique - modélisation affine
plt.figure()
plt.scatter(xreg,y, lw=1)
plt.plot(xreg,ymodelise, 'r--', lw=1)
plt.legend(['modélisation','données'],loc='best',fontsize=14)
plt.ylabel("T² (j²)",fontsize=14)
plt.xlabel("a³ (km³)",fontsize=14)
plt.title("Troisième loi de Kepler - application : \
    \n les satellites de Jupiter",fontsize=16)
plt.grid()
plt.axis(xmin=0)
plt.axis(ymin=0)
plt.show()

####  Coefficient de détermination
covariancenormalise = np.cov(xreg,y)/np.sqrt(np.cov(xreg,xreg)*np.cov(y,y))
r = covariancenormalise[0,1]
r2 = r**2

print("------------------------------------------------------")
print("Modélisation affine du type : y = k*x + b")
print("pente k = ", k ,"(j²/km³)")
print("ordonnée à l'origine b =", b , "(j²)")
print("Coefficient de détermination : r² = ", r2)
print("------------------------------------------------------")
##########################################################################################


