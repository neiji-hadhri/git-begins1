def String(type=str, saison=str):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")

    elif type == "fruits" and saison == "ete":
        print("Poire, fraise, cassis")
    
    elif type == "legume" and saison == "hiver":
        print("carotte, topinambour, endive")

    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine,navet")

    else:
        print("Vous n'avez pas indiqué la bonne saison ou le bon type (fruits ou legume)")

String("fruits", "hiver")
String("legume", "ete")
String("legume", "hiver")
String("fruits", "ete")
