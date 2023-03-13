def rectangle(hauteur, largeur):

    print("|" + "-" * hauteur + "|" )
    i = 2
    while i<largeur :
        print("|" + " " * hauteur + "|")
        i+=1

        print("|"+"-" * hauteur + "|")

rectangle(10,3)