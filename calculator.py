def add(n1,n2):
   return n1+n2
def sub(n1,n2):
   return n1-n2
def mul(n1,n2):
   return n1*n2
def div(n1,n2):
   return n1/n2

print("Arithmetic Operations")
choice=1
while(choice!=0):
  print("1. TO PERFORM ADDITION")
  print("2. TO PERFORM SUBTRACTION")
  print("3. TO PERFORM MULTIPLICATION")
  print("4. TO PERFORM DIVISION")
  print("5. Exit")
  choice = int(input("Enter your choice :"))
  if choice==5:
     print("Exit")
     break
  x = int(input(" Enter the first number : "))
  y = int(input(" Enter the second number : "))
  if choice == 1:
     print(x, "+" ,y ,"=" ,add(x,y))
  elif choice == 2:
     print(x, "-" ,y ,"=" ,sub(x,y))
  elif choice == 3:
     print(x, "*" ,y ,"=" ,mul(x,y))
  elif choice == 4:
       res=div(x,y)
       print("%d  / %d = %.2f" %(x,y,res))
  else:
    print("Invalid Choice, try again");