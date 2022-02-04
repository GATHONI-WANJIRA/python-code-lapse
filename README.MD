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
                 
               
        
        Fibonacci series??
        
        
        
 #### 4. Control Flow Tools. 
        
       >>>> IF Statements.
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
     
     
     
 >>>For statements.
    names =['noni' , 'wahu', 'vivo']
      for u in names:
        print (u,(len(u))
          wahu 4





