L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
Maximum = L[0]
Minimum = L[0]
for i in L :
    if i > Maximum:
        Maximum = i

    if i < Minimum:
        Minimum = i
resultat = Maximum + Minimum

print("Le nombre minimum est {}".format(Minimum))
print("Le nombre maximum est {}".format(Maximum))
print("{} + {} = {}".format(Minimum, Maximum, resultat))