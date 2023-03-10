def liste():
    inventaire = ["bouclier", "pistolet", "potion", "pompe"]
    
    inventaire[0], inventaire[3] = inventaire[3], inventaire[0]
    print(inventaire[:])

liste()