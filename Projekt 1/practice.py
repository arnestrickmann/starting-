print("Hello, World!")

age = 40
if age >4:
    print ("Your admission cost is 0$.")

elif age >8:
    print ("Your admission cost is 25$.")

else:
    print ("Your admission cost is 40$.")


#more consise solution:
age = 12
if age >4:
    price = 0

if age >8:
    price = 25

else:
    price = 40

print (f"Your admission cost is ${price}.")

#function 
def greet (first_name, last_name):
    print (f"Hi, {first_name}, {last_name}.")
    print ("Welcome aboard.")

greet ("Arne", "Strickmann")
greet ("Marje", "Tilly")


def allowed_dating_age (my_age):
    girls_age = my_age/2+7
    return girls_age 

maltes_limit = allowed_dating_age (22)
schneiders_limit = allowed_dating_age (21)

print ("malte can date girls", maltes_limit, "or older")
print ("schneider can date girls", schneiders_limit, "or older")


#task 7.1 in replit (13.10.22 in class)

import math 

def ceiling(x:float):
    if x == int(x):
        return int(x)
    else: 
        return int(x)+1

def century_from_year (year: int):
    tmp = year / 100.0
    print (tmp)
    return math.ceil(tmp)


print(century_from_year(1901))
print(century_from_year(2001))
print(century_from_year(2010))
print(century_from_year(1801))


#sorting a list 

numbers = ["1", "2", "3"]
string = ["asc", "desc", "none"]

string = "asc"

def function (numbers, string):
    if string == "asc":
        print (numbers.sort)
    

#Convert a decimal number into a binary 

def DecimalToBinary(num):
    if num >=1:
        DecimalToBinary(num//2)
    print (num%2, end = '')

if __name__ == '__main__':
    dec_val = 24

    DecimalToBinary(dec_val)

#chonsonant or vowel? 
ch = input("Enter the character:")
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print("Vowel")
else: 
    print("chonsonant")

#counting the vowels in a string 
inputString = str(input("Please type a sentence:"))
a = "a"
A = "A"
e = "e"
E = "E"
i = "i"
I = "I"
o = "o"
O = "O"
u = "u"
U = "U"

acount = 0 
ecount = 0
icount = 0
ocount = 0
ucount = 0

if A or a in str:
    acount = acount+1

if E or e in str:
    ecount = ecount+1

if I or i in str:
    icount = icount+1

if O or o in str:
    ocount = ocount+1

if U or u in str:
    ucount = ucount+1
 
print (acount, ecount, icount, ocount, ucount)

#classes 
#what features does a person have? 

class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight 
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

#we can now start using this class somewhere else in our code
user = Person(21, 84, 1.83, "Arne", "Strickmann", "You know nothing, Arne Strickmann")

print(user.catch_phrase)
