### Print Numbers 1 to 10:

for i in range(1,11):
    print(i)

#Print Even Numbers:

for i in range(1,11):
    if(i % 2 == 0):
        print(i)

#Print Odd Numbers:

for i in range(1,11):
    if(i % 2 == 0):
     continue
    else:
        print(i)

#Sum of Numbers:
j= 0;
for i in range(1,101):
     j = j+i;


print(j)    

#Factorial Calculation:Calculate the factorial of a number using a for loop.

j=10
fact=1;
for i in range (1,j+1):
    fact= fact*i

print("Factorial Calculation")
print(fact)    
#7 Reverse a String:Reverse the characters of a string using a for loop.

str= "hello Ramacccc"
reverse=""
len=len(str)-1
print(len)
for  i in str:
    reverse=reverse+str[len]
    len=len-1
    print(reverse)

print(reverse)

#Iterate Over a List: Loop through each element in a list and print it.

list= [1,2,3,4,6,7,8]

for i in list:
    print(i)

#Iterate Over a Tuple:Loop through a tuple and display its items.

t_tupple =(2,4,6,8,10)

for i in t_tupple:
    print(i)

#Iterate Over a Set: Loop through a set and print each unique element.



my_set = {1,5,10,15,20,25}

for i in my_set:
    print(i)   

##String & List Manipulations

##Count Characters in a String:Count the frequency of each character in a string.
str = "ccccamaR olleh hero"
da = ""
for i in str:
    if i in da:  # Check if character 'i' is already in 'da'
        continue  # Skip the character if it's already in 'da'
    else:
        da += i  # Add the character to 'da' if it's not already there

print(da)

##Convert List of Strings to Uppercase:

list= ["data","base","design"]
Nwlist=[]
for i in list:
    b= i.upper()
    Nwlist.append(b)

print(Nwlist)

##Convert List of Strings to Lowercase:
    
    
list= ["dSata","baSse","desiSgn"]
Nwlist=[]
for i in list:
    b= i.lower()
    Nwlist.append(b)

print(Nwlist)

##Concatenate List Items into a String:Join a list of strings into a single string.  
list = ["data", "base", "design"]
result = ''.join(list)  # Joins the list items with no spaces
print(result)
# Output: "database design"


#Generate List of Squares:

list=[1,2,4,5,7,9,10]
squire_list=[]
for i in list:
    d=i*i
    squire_list.append(d)

print(squire_list)    


#Generate List of cubes:

list=[1,2,4,5,7,9,10]
squire_list=[]
for i in list:
    d=i*i*i
    squire_list.append(d)

print(squire_list)    


#Print a Multiplication Table:Use nested loops to print the multiplication table for numbers 1 to 10.
a= 5

for i in range(1,21):
      print(a, "*",i,"=",a*i)

