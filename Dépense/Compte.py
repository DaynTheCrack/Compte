import os
import pickle
import datetime

#mise à jour des var (mise à zéro)
DateTime = str(datetime.date.today()).split("-") # liste de la date du jour
DateKey = DateTime[0] + "." + DateTime[1] # création de la clée unique du mois
dictionnaire = dict() # créaction d'un dictionnaire vide

def transa(): # nombre de transactions
    nbr_opera = (input("Combien de transactions avez vous efféctué ?"))
    nbr_opera = nbr_opera.replace(",",".")
    return float(nbr_opera)

def clear(): # Fonction clear
    os.system('cls')

def save(dict): # permet d'enregistrer les dépenses du mois
    with open("PY/TP/Dépense/DB.txt","wb") as fichier:
        mon_pickler = pickle.Pickler(fichier)
        mon_pickler.dump(dict)
        return "Enrigistrement terminé"

def read(dict): # permet de lire les dépenses du mois
    with open("PY/TP/Dépense/DB.txt","r") as file: 
        if file.read() != "": # on regarde si le fichier est vide
            with open("PY/TP/Dépense/DB.txt","rb") as fichier: # le fichier n'est pas vide on ajoute
                mon_deplickler = pickle.Unpickler(fichier)
                dict = mon_deplickler.load()
                return dict
        else: # le fichier est vide on créer
            return dictionnaire

def MainProg(fonc,dictionnaire): # Fonction principale du programme
    # initialisation des vars
    compteur = fonc
    prix_total = 0

    # création de la boucle en fonction du nombre de transactions
    while compteur > 0:
        prix = (input("Rentrez le prix !\n>>>"))
        clear()
        prix = prix.replace(",",".")
        prix_total += float(prix)
        compteur -= 1
    # vérification si clef déjà crée ou pas
    if DateKey not in dictionnaire.keys():
        dictionnaire[DateKey] = 0
    dictionnaire[DateKey] += prix_total

    # renvoie la le mois/l'année et le prix sur le mois
    print("On vous doit : {0} euros {1}".format(str(dictionnaire[DateKey]),DateKey.replace(".","/")))
    save(dictionnaire)
MainProg(transa(),read(dictionnaire)) # on appelle les fonctions
var = read(dictionnaire) # on debug en affichant le résultat
print(var.keys())