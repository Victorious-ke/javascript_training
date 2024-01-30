# num1=float(input("enter num1; "))
# num2=float(input("enter num2; "))
# num3=float(input("enter num3; "))
# if(num1>num2 and num1>num3):
#   print(f "{num1} is greater")
# elif(num2>num1 and num2>num3):
#   print(f "{num2} is greater")
# else:
#   print(f "{num3} is greater")

#temparature
temp=float(input("enter temp; "))
if(temp>30):
    pnt="the temp is too high"
elif(temp>=15 and temp<=30):
   pnt="normal temp"
elif(temp>=0 and temp<15):
   pnt="low temp"
else:
  pnt="extremly cold"

print(pnt)

#voting
age=int(input("enter age: "))
if(age>=18):
   print("is eligible")
else:
   print("not eligible")

  #divisible by 7
num=int(input('enter number: '))
if(num%7==0):
      
      print("divisble by 7")  
else:
  print("not divisble by 7")