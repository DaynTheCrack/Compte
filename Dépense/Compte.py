"""Pensez à bien remettre le chemin d'accès relatif à 'DB.txt' """
import os
import pickle
import datetime
import os
import matplotlib.pyplot as plt

# mise à jour des var (mise à zéro)
DateTime = str(datetime.date.today()).split("-") # liste de la date du jour
DateKeyYear = DateTime[0] # création de ma clée unique de l'année
DateKeyMonth = DateTime[0] + "." + DateTime[1] # création de la clée unique du mois
DateKeyDay = DateTime[0] + "." + DateTime[1] + "." + DateTime[2] # création de la clée unique du jour

dictionnaire = {
    "year" : {},
    "month" : {},
    "day" : {},    
} # créaction d'un dictionnaire vide avec année, mois et jour

def grille(dictionnaire):

    compteur = 0 # si c'est la première ligne
    max = 0 # création de la var 

    for key,element in dict(dictionnaire["day"]).items(): # definition du len max 
        if len(key) > max:
            max = len(key)
        if len(str(element)) > max: # element float to str
            max = len(str(element))

    for key,element in dict(dictionnaire["day"]).items():
        
        strelement = str(element)
        Ligne = [] # liste de la ligne vide
        longueurEsp = 3 # nombre d'espaces par default

        if len(key) < max:
            longueurEsp += (max - len(key) + 3) // 2 # nombre d'espaces en debut et en fin
        Ligne.append(str("#"+longueurEsp*" "+key+longueurEsp*" "+"#"))

        longueurEsp = 3

        if len(strelement) < max:
            longueurEsp += (max - len(key) + 3) // 2
        Ligne.append(str(longueurEsp*" "+strelement+"€"+longueurEsp*" "+"#"))

        ligne = len("".join(Ligne)) # longueur de la ligne 

        if compteur == 0:
            print(ligne*"#")
        compteur += 1 # on ajoute 1 pour savoir si c'est la première ligne
        print("".join(Ligne)) # grille
        print(ligne*"#")

    return "Tableau fini !"

def transa(): # nombre de transactions
    nbr_opera = (input("Combien de transactions avez vous efféctué (voir) ?"))
    nbr_opera = nbr_opera.replace(",",".")
    return float(nbr_opera)

def clear(): # Fonction clear
    os.system('cls')

def save(dict): # permet d'enregistrer les dépenses du mois
    with open("TP/Dépense/DB.txt","wb") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(dict)
        return "Enregistrement terminé !"

def read(dict): # permet de lire les dépenses du mois
    with open("TP/Dépense/DB.txt","r") as file: 
        if file.read() != "": # on regarde si le fichier est vide
            with open("TP/Dépense/DB.txt","rb") as fichier: # le fichier n'est pas vide on ajoute
                mon_deplickler = pickle.Unpickler(fichier)
                dict = mon_deplickler.load()
                return dict
        else: # le fichier est vide on le créer
            return dict
    
def graph(dictionnaire): # permet de créer un graph des dépenses sur l'année/mois/jour
    Xyear = [] # mise a zéro des valeurs d'abscises et d'ordonnées
    Yyear = []

    Xmonth = []
    Ymonth = []

    Xday = []
    Yday = []
    
    for key,element in dict(dictionnaire["year"]).items(): # construction de la figure 'year'
        Xyear.append(key)
        Yyear.append(element)
    plt.subplot(3,1,1)
    plt.plot(Xyear,Yyear,"dr")
    plt.plot(Xyear,Yyear)

    for key,element in dict(dictionnaire["month"]).items(): # construction de la figure 'month'
        Xmonth.append(key)
        Ymonth.append(element)
    plt.subplot(3,1,2)
    plt.plot(Xmonth,Ymonth,"dr")
    plt.plot(Xmonth,Ymonth)

    for key,element in dict(dictionnaire["day"]).items(): # construction de la figure 'day'
        Xday.append(key)
        Yday.append(element)
    plt.subplot(3,1,3)
    plt.plot(Xday,Yday,"dr")
    plt.plot(Xday,Yday)

    return plt.show()



def MainProg(fonc,dictionnaire): # Fonction principale du programme
    # initialisation des vars
    compteur = fonc
    prix_total = 0

    # création de la boucle en fonction du nombre de transactions
    while compteur > 0:
        prix = (input("Rentrez le prix !\n>>>"))
        clear()
        prix = prix.replace(",",".")
        prix_total += round(float(prix),2) # on arrondi a deux chiffres après la virgule
        compteur -= 1

    # vérification si clef déjà crée ou pas
    if DateKeyYear not in dict(dictionnaire["year"]).keys():
        dictionnaire["year"][DateKeyYear] = 0 # mise à jour des clées et des valeurs si 'year' n'est pas ref

    if DateKeyMonth not in dict(dictionnaire["month"]).keys():
        dictionnaire["month"][DateKeyMonth] = 0 # mise à jour des clées et des valeurs si 'month' n'est pas ref
    
    if DateKeyDay not in dict(dictionnaire["day"]).keys():
        dictionnaire["day"][DateKeyDay] = 0 # mise à jour des clées et des valeurs si 'day' n'est pas ref

    dictionnaire["year"][DateKeyYear] += prix_total
    dictionnaire["month"][DateKeyMonth] += prix_total
    dictionnaire["day"][DateKeyDay] += prix_total

    # renvoie la le mois/l'année et le prix sur le mois
    print("Tout est bon !")
    save(dictionnaire)
MainProg(transa(),read(dictionnaire)) # on appelle les fonctions
var = read(dictionnaire) # on debug en affichant le résultat
print(var.items())
print(var)
graph(read(dictionnaire))
grille(read(dictionnaire))

"""Faire un interface utilisateur et créer des clées avec les le thème des dépenses et/ou la personne qui vous doit de l'argent"""
