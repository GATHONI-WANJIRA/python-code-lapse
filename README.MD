### Basic writing and formatting syntax.
        ##### All possible sample code is available in its respective file.

#### 1.Using the python interpreter.
> The docs get to outline various ways of starting the python interpreter. 
     (i honestly didn't dwell on this and the commands as well
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
       

    >>> Fibonaci series.
        It is used to add two precede numbers to come up with the  next number in line. (nth number.)
```python 
("Please enter a positive integer.")
elif nterms == 1:
    print ("fibonacci sequence upto" , nterms, ":")
    print (a)nterms = int(input("How many terms ?"))
#first two terms.
a,b= 0,1
count = 0
if nterms <= 0:
    print
else:
    print ("fibonacci sequence:")
    while count < nterms:
        print (a)
        nth = a + b
        a = b
        b = nth
        count += 1
```
  
       
    >>> Strings.
        They are usually enclosed in single or double quotes. (" ") , (' ') .
                    print("you are late to work")
        They can be joined together by use of '+' and repeated by use of '*' .

```python
                   Name = jude
                   action = died.
                   print name  
                   jude died.
``` 

        
        Strings can be indexed by having the first character identified as  index (0) .
       
 ```python
        fruits = ["pears"," oranges","kiwi","apple"]
                        print (fruit [2]
                            kiwi
```
        
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
        
```python
         fruits = ["mangoes", "oranges", "kiwi", "apple"]
         fruits.append.("bananas", "pawpaw)
         print fruits
         ["mangoes", "oranges", "kiwi", "apple" "bananas" "pawpaw"]           
```

                 
        They can also be nested. thus creating lists that contain other lists.
          
```python
           fruits_in_string = ["pears"," oranges","kiwi","apple"]
               fruits_in_lists =  ["mangoes", "oranges", "kiwi", "apple" "bananas""pawpaw"]
                 fruits= fruits_in_string + fruits_in_lists
                  print fruits =  ["pears", "oranges", "kiwi", "apple ,"bananas","pawpaw"]
```
        
        
 #### 4. Control Flow Tools. 
        
   -IF Statements.
         They include IF, ELIF,ELSE.
         
         They are used to write conditional flow code.
         They evaluate if a condition is true or false.
                 
```python     
           def get_capital(country):

             if country == "kenya":
                return "Nairobi"
   
             elif country == "lebanon":
                return "Beruit"
   
             elif country == "DRC":
                return Kinshasa
    
             else: 
               return none
```
     

-The Range () function. 

```python
   For i in range (4): 
   print (i)
         0
         1
         2
         3
 ``` 
         
  The given end point is not part of the generated sequence.
 
 
-Break and continue statements , & else clauses on loops.

 A loop interates over an object until it is complete.
 It can either be a For loop or a While loop as shown below .

```python
     str = "Python"
      for c in str:
       print(c)
         P
         y
         t
         h
         o
         n

```
         
If there is a repitition in a variable the loop will only call the character once. Loops dont arrange the output in the order og the occurrence but rather randomly.

```python
   my_set = set("ABCBA")
  for c in my_set:
  print(c)
  C
  B
  A
```
       
 Loops in dictionaries.
 
```python
         num_dict = {1: "Nairobi", 2: "kisumu", 3: "Eldoret"}
             for k, v in num_dict.items():
                print(f'{k}={v}')
                   1=one
                     2=two
                       3=three
```

Theres a for or while loop where conditions given gets to be excecuted just like in If and Else statements.
 
 ```python
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
```
               
Compilations of For & Else break loops.
 
 ```python
           for n in range (2, 10):
                # print (n)
           for x in range (2, n):
                # print (x)
              if n % x == 0:
                print (n," is not a prime number!")
             break
          else:
            print (n," is a prime number")
```
            
            
            
 Continue statements in loops.

```python

     for num in range (2,10):
        if num % 2 == 0:
          print("this is an even number", num)
          continue
            print("this is an odd number" , num)     
```         
            
            
 ##### 4.5 Pass Statements.
   They are used phrase portions of the code that need no action.They create empty block codes and functions.
   They are useful in creating blank classes and functions for information that will be updated later on.
   
           while True:
              pass  


   
##### 4.6 Match Statements.
 Its takes an expression and compares its value to successive patterns given as one or more case blocks.
 
 ```python
       number =int(input("code"))
        def country_name(code):
         match code:
          case 254:
            return ("Kenya")                                                                   
          case 256:
            return ("Uganda")
          case 247:
            return ("tanzania")
          case _:
            return ("Notfound")
        print (country_name(number))
```
                  
Patterns can look like unpacking assignments, and can be used to bind variables:

```python
var = (8,0)
match var:
  case (0,x)
   print ("on y-axis")
  case (x,0)
   print ("on x-axis")
  case (0,0)
   print ("point of origin")
  

  output
  on x axis
```

#### 4.7 Defining Functions.

Basic defining functions to be elaborated in the next part.

#### 4.8 More on defining functions.

##### 4.8.1 Default Argument Values.

#### 5. DATA STRUCTURES.

 A specialized means of organizing and storing data.
 
##### 5.1 More on lists.
 >>> list.append(x)
  - To add an item to a certain set.
  
 >>> list.insert(i, x)
  - To insert an item .... i= index.. x = item to be added.
  
 >>> list.remove(x) 
 - To remove an item from a certain entry.
 
 >>> list.pop([i]) 
 
 -To remove a certain indexed item and return it later. if not specified it removes the item in the last index.
 
 >>> list.clear()
 
 -To remove all the items in an entry.
 
 >>> list.index(x[, start[, end]])
 
 - To identify items in reference to their identified position. The first x, has zero indexing.
 
 >>> list.count(x)
 
 - Used to return the number of times x appears in an entry.

>>> list.sort 

- Sort the items of the list in place.

>>> list.reverse()

- To reverse the number of elements in place.

>>> list.copy()

- To return a shallow copy of the return list.
 
##### 5.1.1. Using Lists as Stacks





























