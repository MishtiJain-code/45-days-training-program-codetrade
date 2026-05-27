 #try cath block helps here to reflect a disclamer meesage in case wrong input is entered

try:
  n=int(input("Enter number"))
  if(n%2==0):
      print("No is even")
  elif(n==0):
      print("It is zero")
  else:
        print("No is odd")
except ValueError:
  print("Invalid Value!, Plz enter correct value")