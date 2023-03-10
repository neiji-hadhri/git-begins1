alph = "abcdefghijklmnopqrstuvwxyz" * 10
ligne = 1
i = 0
  
while i + ligne <= len(alph): 
    print(alph[i: i+ligne]) 
    i+= ligne
    ligne+=1 
	
