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


