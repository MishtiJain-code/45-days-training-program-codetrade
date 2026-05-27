#random:-random randint()-for taking random int vaue
#random.random():-for taking random float value
#random.choice():-to make choice of random value
#random.shuffle:-to make random shuffle of list
import random
num=random.randint(1,100)
attempts=0
while(attempts<7):
    a=int(input("Choose a number"))
    attempts+=1
    if(a>num):
      print("Too High")
    elif(a==num):
        print("Number Found")
        break
    elif(a<num):
       print("Number is too low")
    else:
       print("Number not found")

print(f"Attempts : {attempts}")
        