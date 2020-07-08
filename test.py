def compteVoyelle(mot):
    # créer le compteur de voyelles
    compteur_voyelle = 0

    # faire une boucle et compter sur un mot chaque voyelle
    for lettre in mot:
        if lettre in ['a', 'e', 'i', 'o', 'u']:
            # ajouter + 1 au compteur_voyelle
             compteur_voyelle = compteur_voyelle + 1

    # en fin de boucle renvoyer le compteur
    return compteur_voyelle


mot1 = input("Entrer un mot: ")
voyelle = compteVoyelle(mot1)
print("résultat: il y a ", voyelle, " voyelles dans votre mot." )