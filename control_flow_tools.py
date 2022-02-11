#If, elif, and else statements.

def get_capital_city(country):
    if country == "kenya":
        return "Nairobi"
    elif country == "DRC":
        return "kinshasa"
    elif country == "lebanon":
        return "Beruit"
    else: 
         return "None"

         #for loops.
names = ["noni", "wahu", "vivo"]  
for w in names:
    print (w, len(w))

    # While loops.
Days = 5
while Days > 4:
    print ("enough")
else: 
    print ("add some more")


#compilation of For and else break loops.
for n in range (2, 10):
    # print (n)
    for x in range (2, n):
        # print (x)

       if n % x == 0:
           print (n," is not a prime number!")
           break
    else:
            print (n," is a prime number")

for num in range (2,10):
    if num % 2 == 0:
        print("this is an even number", num)
        continue
    print("this is an odd number" , num)




#Continue statements.
for num in range (2,10):
     if num % 2 == 0:
         print("this is an even number", num)
         continue
     print("this is an odd number" , num)
    
