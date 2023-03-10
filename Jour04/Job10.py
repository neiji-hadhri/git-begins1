L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91] 
n=1
for i in L:
    if i  in range(25, 90):
        n = n * i
print(n)