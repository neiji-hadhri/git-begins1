liste = [10,20,30,20,10,50,60,40,80,50,40]
nou_liste = []

for i in liste:
    if i not in nou_liste:
        nou_liste.append(i)

print(nou_liste)