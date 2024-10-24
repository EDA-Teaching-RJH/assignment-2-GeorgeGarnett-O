### Part Two -- your code goes here. 
import random 

number_variable = input(random.randint(1, 100))
number_variable = random.randint(1, 100)

determinant = int(input("the corect number from the number variable randomizer"))
loop = True 

while loop == True:

if determinant > number_variable :
    determinant = int(input("number from the number variable randomizer"))
    if determinant > number_variable :
        print  ("too high a number")
    elif determinant < number_variable : 
        print  ("too low of a number")
    elif determiant == numbr_variable: 
        print  ( "correct number") 
        loop = False 

   print  ("too high a number")
elif determinant < number_variable : 
   print  ("too low a number")
elif determinant == number_variable: 
   print  ( "correct number")