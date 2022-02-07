p = 2
w = 4
n = p+w
print (n)

#this gets to happen to all the other mathematical syntax expression just interchanging respectifully.
k = 10
m = 2 
u = k/m
print (u)

#To eliminate the decimal or the fraction in any division you use double // as illustrated below.

z =10 
g = 2
h = z//g 
print (h)


#to find power of any number use **.
l =10**2
print (l)

#to determine complex sums we use j and J to represent the unknowns like shown below.
v = 10j
a = 2
t= v - a 
print (t)

#To determine type/class of any objects.

# If it is a whole number thats an integer.
marks = (23)
print (type(marks)) 


#if the object is a float the number has a fraction or a decimal.
height = (5.4)
print (type(height))


#if the object is a letter then thats a string.
name = ("nairobi")
print (type(name))



#if the object is a list they have a square bracket indentation with commas in between them.
age = [4,2,3,6,8,9]
print (type(age))



#if the object is a tuple then it has parenthesis indentation with commas in between them
length = (6,7,9,3,5)
print (type(length))

#the addons are not covered in this segments but will definitely be covered by other files.


#we normally index our strings. The first from the left towards the right is indexed 0 while the last one towards the left is indexed as -1.
#eg sunday = 0 , monday = 1, thursday = -1
#you can also get to slice them down from the index that is required.
#eg if you say (days [2:]) it should give you days from index two to the last one.

days = ("Sunday" , "Monday" , "Tuesday" , "Wednesday" , "Thursday" )
print (days[2])
print (days[-2])
print (days[1:])


#there are several inbuilt functions that can get used diffrently.
#eg len to determine the length of any input.it answers how many.


weeks = [3,4,6,8,9]
print (len(weeks))
weeks.append(7)
print (len(weeks))
print (weeks)

