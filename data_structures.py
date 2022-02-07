print ("Hello world")

for n in range (2, 10):
    # print (n)
    for x in range (2, n):
        # print (x)
    # print ("Nonnie")
       if n % x == 0:
           print (n," is not a prime number!")
           break
    else:
            print (n," is a prime number")


