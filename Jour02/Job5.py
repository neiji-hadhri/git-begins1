def calcule(num1, operator, num2):
    if operator == "+":
        resultat = num1 + num2
        print("Le résulat de {} {} {} = {}".format(num1, operator, num2, resultat))

    elif operator == "-":
        resultat = num1 - num2
        print("Le résulat de {} {} {} = {}".format(num1, operator, num2, resultat))
    
    elif operator == "/":
        resultat = num1 / num2
        print("Le résulat de {} {} {} = {}".format(num1, operator, num2, resultat))

    elif operator == "%":
        resultat = num1 % num2
        print("Le résulat de {} {} {} = {}".format(num1, operator, num2, resultat))

    else :
        print("Le type de calcul n'est pas valable, vous pouvez utiliser que '+', '-', '/', '%' ")
        
calcule(2, "+", 29)
calcule(10, "-", 3)
calcule(17, "/", 3)
calcule(5, "%", 2)
calcule(5, "#", 7)
