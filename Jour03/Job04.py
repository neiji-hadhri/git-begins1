def nombre():
    i = 1
    while i < 100 :
        i+=1
        if i % 3 == 0 :
            print("Fizz : {}".format(i))
            

        if i % 5 == 0 :
            print("Buzz : {}".format(i))
            if i % 3 == 0 :
                print("FizzBuzz : {}".format(i))    
                
nombre()