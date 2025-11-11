import os

# Mauvaise pratique : exécution de commande système avec input direct
user_input = input("Entrez une commande système : ")
os.system(user_input)
