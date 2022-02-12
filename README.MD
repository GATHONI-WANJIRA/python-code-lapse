### Basic writing and formatting syntax.
        ##### All possible sample code is available in its respective file.
        



<!--Hapa wadau nayo ni sir jah aniokoe bana -->

#### 1.Using the python interpreter.
> The docs get to outline various ways of starting the python interpreter. 
     (i honestly didn't dwell on this and the commands as well since in the past i've not used them in any way)
     The commands included
                        : python-c command [arg]
                        
2. #### Invoking the interpreter.
(Same content as intro to the python interpreter.Looking forward to relate with this two.)
     
> Interpreter & its Environment.
   
   >>>>Source Coding & Encoding.
   -To declare an encoding other than the default one is to be used, this special line of code should be added to the first line of the file;
    * coding: encoding *
   (where encoding is a valid codecs eg =cp1252) Also check the file to see the initial syntax without MD effect.
   -Incase the source code starts with a ##### UNIX "_shebang_" line ,the declaration should be added  as the second line of the file.
   
   

 3. #### Informal introduction to python.   
     comments in python are written by use of '#' before a line of code, in a white space, but never in a string literal.
     
    >>> Using python as a calculator.
      Numbers expression syntax still work like in other launguages and can be used for grouping.(+,=,*,/,) .
      
 
      
       Integers are numbers without the fractions eg 2,3,4,5, and are type 'int'.Numbers with fractions like 5.8,2.0 are identified as type float.
       To avoid getting any fractional result one can use (//).
       For calculation of power use (**) 
       
             2**2 = 4
       
       Word [0(included):2(excluded] 
       
       [:2] from position 0 (included) to 2 (excluded)
       [4:] from 4 (included to the end)
        
        The inbuilt function len() is supposed to return the length of a string.
       
       python also has built in support for complex numbers and uses 'j' or 'J' suffix to indicate the imaginary part eg (6+5j)
       
       
    >>> Strings.
        They are usually enclosed in single or double quotes. (" ") , (' ') .
                    print("you are late to work"
        They can be joined together by use of '+' and repeated by use of '*' .
                   Name = jude
                   action = died.
                   print name + action
                   jude died.
        
        Strings can be indexed by having the first character identified as  index (0) .
                        fruits = ["pears"," oranges","kiwi","apple"]
                        print (fruit [2]
                            kiwi
        
        Negative indices start from -1 since 0, is the same as -0 hence only acknowledging 0 from the left.
                           print (fruit[-2])
                                  kiwi
        
        You can also slice the characters to obtain sub strings eg [0:2]
                        print (fruits[1:]
                        oranges,kiwi,apple
                        
                        
        The length in built function.
               print ((len(fruits))
                    4
                    
        They are immutable.
              their initial positions cannot be changed.
        
        
    >>> Lists.
        They are written inside square brackets and separated with comas, eg [1,2,6,9,] , provided they are of the same type.
        They can also be indexed taking the first position as a 0.
        (apply the same concept of lists above in string)
        
        Unlike strings they are mutable.
        You can also add new items to the list using ; append () method.
        
                 fruits = ["mangoes", "oranges", "kiwi", "apple"]
                   fruits.append.("bananas", "pawpaw)
                   print fruits
                    ["mangoes", "oranges", "kiwi", "apple" "bananas" "pawpaw"]
                 
        They can also be nested. thus creating lists that contain other lists.
                 fruits_in_string = ["pears"," oranges","kiwi","apple"]
                    fruits_in_lists =  ["mangoes", "oranges", "kiwi", "apple" "bananas""pawpaw"]
                       fruits= fruits_in_string + fruits_in_lists
                       print fruits =  ["pears", "oranges", "kiwi", "apple", "mangoes", "bananas""pawpaw"]
                 
               
        
        
        
        
        
 #### 4. Control Flow Tools. 
        
   -IF Statements.
         They include IF, ELIF,ELSE.
         
         They are used to write conditional flow code.
         They evaluate if a condition is true or false.
                 
                
           def get_capital(country):

             if country == "kenya":
                return "Nairobi"
   
             elif country == "lebanon":
                return "Beruit"
   
             elif country == "DRC":
                return Kinshasa
    
             else: 
               return none
     

-The Range () function. 

    For i in range (4): 
      print (i)
         0
         1
         2
         3
          
  The given end point is not part of the generated sequence.
 
 
-Break and continue statements , & else clauses on loops.

 A loop interates over an object until it is complete.
 It can either be a For loop or a While loop as shown below .
 
     str = "Python"
      for c in str:
       print(c)
         P
         y
         t
         h
         o
         n
         
If there is a repitition in a variable the loop will only call the character once. Loops dont arrange the output in the order og the occurrence but rather randomly.

              my_set = set("ABCBA")
                 for c in my_set:
                  print(c)
                    C
                    B
                    A
         
 Loops in dictionaries.
    
                 num_dict = {1: "Nairobi", 2: "kisumu", 3: "Eldoret"}
                   for k, v in num_dict.items():
                     print(f'{k}={v}')
                       1=one
                       2=two
                       3=three

Theres a for or while loop where conditions given gets to be excecuted just like in If and Else statements.
 
              Fruits = ["mango", 'cherry", "apple"]
                 for fruit in fruits 
                  print (fruit)
                    mango
                    apple
                    cherry
                    
               Count = 4
                while count > 4
                 print ("run the code")
                else:
                 print ("Dont run the code")
               
Compilations of For & Else break loops.
 
           for n in range (2, 10):
                # print (n)
           for x in range (2, n):
                # print (x)
              if n % x == 0:
                print (n," is not a prime number!")
             break
          else:
            print (n," is a prime number")
            
            
            
 Continue statements in loops.

     for num in range (2,10):
        if num % 2 == 0:
          print("this is an even number", num)
          continue
            print("this is an odd number" , num)     
            
            
            
 4.5 Pass Statements.
   They are used phrase portions of the code that need no action.They create empty block codes and functions.
   They are useful in creating blank classes and functions for information that will be updated later on.
   
           while True:
              pass  
   
4.6Match Statements.
 Its takes an expression and compares its value to successive patterns given as one or more case blocks.
 

                  


