### Basic writing and formatting syntax.
        ##### All possible sample code is available in its respective file.

#### 1.Using the python interpreter.
> The docs get to outline various ways of starting the python interpreter. 
     (i honestg
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

- The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index.

##### 5.1.2. Using Lists as Queues.

-  where the first element added is the first element retrieved (“first-in, first-out”); however, lists are not efficient for this purpose. While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).

To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.


##### 5.1.3. List Comprehensions.

-List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operations applied to each member create a subsequence of those elements that satisfy a certain condition.


##### 5.1.4. Nested List Comprehensions.

-The initial expression in a list comprehension can be any arbitrary expression, including another list comprehension.



##### 5.2. The del statement.

-  The del statement can also be used to remove slices from a list or clear the entire list.There is a way to remove an item from a list given its index instead of its value: the del statement. This differs from the pop() method which returns a value. 


##### 5.3. Tuples and Sequences.

-  They are two examples of sequence data types (see Sequence Types — list, tuple, range). Since Python is an evolving language, other sequence data types may be added. There is also another standard sequence data type: the tuple.

A tuple consists of a number of values separated by commas. Tuples are also immutable.


##### 5.4. Sets.

-Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

Curly braces or the set() function can be used to create sets. Note: to create an empty set you have to use set(), not {}; the latter creates an empty dictionary, a data structure.


##### 5.5. Dictionaries.

-Dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.
It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.

The main operations on a dictionary are storing a value with some key and extracting the value given the key. It is also possible to delete a key:value pair with del. If you store using a key that is already in use, the old value associated with that key is forgotten. It is an error to extract a value using a non-existent key.


##### 5.6. Looping Techniques.

- When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
- When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function
-Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an idiomatic way to loop over unique elements of the sequence in sorted order.



#### 6. Input and Output.

- There are several ways to present the output of a program; data can be printed in a human-readable form, or written to a file for future use.

##### 6.1 Fancier Output Formatting.

-Often you’ll want more control over the formatting of your output than simply printing space-separated values. There are several ways to format output.

To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark. Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.


###### 6.1.1 Formatted String Literals.

- They are also called f-strings for short) let you include the value of Python expressions inside a string by prefixing the string with f or F and writing expressions as {expression}.

An optional format specifier can follow the expression. This allows greater control over how the value is formatted.


###### 6.1.2 The String format() Method.

-The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
-If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.


###### 6.1.3 Manual String Formatting.

- The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually better than the alternative, which would be lying about a value. (If you really want truncation you can always add a slice operation, as in x.ljust(n)[:n].)

There is another method, str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs.


###### 6.1.4 . Old string formatting.

-The % operator (modulo) can also be used for string formatting. Given 'string' % values, instances of % in string are replaced with zero or more elements of values. This operation is commonly known as string interpolation. 


#### 6.2 Reading and Writing Files.

-The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used. mode can be 'r' when the file will only be read, 'w' for only writing (an existing file with the same name will be erased), and 'a' opens the file for appending; any data written to the file is automatically added to the end. 'r+' opens the file for both reading and writing. The mode argument is optional; 'r' will be assumed if it’s omitted.

Normally, files are opened in text mode, that means, you read and write strings from and to the file, which are encoded in a specific encoding. If encoding is not specified, the default is platform dependent (see open()). 'b' appended to the mode opens the file in binary mode: now the data is read and written in the form of bytes objects. This mode should be used for all files that don’t contain text.



##### 6.2.1 Methods of File Objects.

- f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

- If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().

f.write(string) writes the contents of string to the file, returning the number of characters written.


##### 6.2.2 Saving structured data with json.


### 7. Errors and Exceptions.

- There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

#### 7.1 Syntax Errors.

- Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python.

#### 7.2 Exceptions.

- Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal.


#### 7.3 Handling Exceptions.

- It is possible to write programs that handle selected exceptions.

#### 7.4 Raising Exceptions.

- The raise statement allows the programmer to force a specified exception to occur.
The sole argument to raise indicates the exception to be raised. This must be either an exception instance or an exception class (a class that derives from Exception). If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments.
If you need to determine whether an exception was raised but don’t intend to handle it, a simpler form of the raise statement allows you to re-raise the exception.


#### 7.5 Exception Chaining.

-The raise statement allows an optional from which enables chaining exceptions.
This can be useful when you are transforming exceptions. Exception chaining happens automatically when an exception is raised inside an except or finally section. This can be disabled by using from None idiom:


#### 7.6 User-defined Exception.

- Programs may name their own exceptions by creating a new exception class (see Classes for more about Python classes). Exceptions should typically be derived from the Exception class, either directly or indirectly.

Exception classes can be defined which do anything any other class can do, but are usually kept simple, often only offering a number of attributes that allow information about the error to be extracted by handlers for the exception.

Most exceptions are defined with names that end in “Error”, similar to the naming of the standard exceptions.

Many standard modules define their own exceptions to report errors that may occur in functions they define.


#### 7.7 Defining Clean-up Actions.

- If a finally clause is present, the finally clause will execute as the last task before the try statement completes. The finally clause runs whether or not the try statement produces an exception. The following points discuss more complex cases when an exception occurs:

If an exception occurs during execution of the try clause, the exception may be handled by an except clause. If the exception is not handled by an except clause, the exception is re-raised after the finally clause has been executed.

An exception could occur during execution of an except or else clause. Again, the exception is re-raised after the finally clause has been executed.

If the finally clause executes a break, continue or return statement, exceptions are not re-raised.

If the try statement reaches a break, continue or return statement, the finally clause will execute just prior to the break, continue or return statement’s execution.

If a finally clause includes a return statement, the returned value will be the one from the finally clause’s return statement, not the value from the try clause’s return statement.


### 8.0 Classes.

#### 8.1 A Word About Names and Objects.

#### 8.2 Python Scopes and Namespaces.

- A namespace is a mapping from names to objects. Most namespaces are currently implemented as Python dictionaries, but that’s normally not noticeable in any way (except for performance), and it may change in the future. Examples of namespaces are: the set of built-in names (containing functions such as abs(), and built-in exception names); the global names in a module; and the local names in a function invocation. In a sense the set of attributes of an object also form a namespace. The important thing to know about namespaces is that there is absolutely no relation between names in different namespaces; for instance, two different modules may both define a function maximize without confusion — users of the modules must prefix it with the module name.

-Although scopes are determined statically, they are used dynamically. At any time during execution, there are 3 or 4 nested scopes whose namespaces are directly accessible:

the innermost scope, which is searched first, contains the local names
the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope, contains non-local, but also non-global names
the next-to-last scope contains the current module’s global names
the outermost scope (searched last) is the namespace containing built-in names


#### 8.3 A First Look at Classes.

- Classes introduce a little bit of new syntax, three new object types, and some new semantics.

##### 8.3.1 Class Definition Syntax.


















