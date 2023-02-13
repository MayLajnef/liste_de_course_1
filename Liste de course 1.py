#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
choix = ""
liste = []
    
while choix != "5":
    choix = input("Choisissez parmi les 5 options suivantes : \n 1: Ajouter un élément à la liste \n 2: Retirer un élément de la liste \n 3: Affficher la liste \n 4: Vider la liste \n 5: Quitter \n → Votre choix : ")
    if choix == "1":
        ajout = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste.append(ajout)
        print(f"L'élement {ajout} a bien été ajouté à la liste.")
    elif choix == "3":
        if liste == []:
            print("Votre liste ne contient aucun élément.")
        else:
            print("Voici le contenu de votre liste : ")
            for i in range(len(liste)):
                print(f"{i+1}. {liste[i]}")
    elif choix == "2":
        retrait = input("Entrez le nom de l'élément à retirer de la liste de courses : ")
        if retrait in liste:
            liste.remove(retrait)
            print(f"L'élément {retrait} a bien été retiré de la liste.")
        else:
            print(f"L'élément {retrait} n'est pas dans la liste.")
    elif choix == "4":
        liste.clear()
        print("La liste a été vidée de son contenu.")  
    else:
        continue
else:
    print("À bientôt")
    sys.exist()


# In[ ]:




