#Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
marks=int(input("enter marks; "))
if (marks>79 and marks<100):
  print("A")
elif (marks<=79 and marks>=60):
  print("B")
elif (marks<60 and marks>=50):
  print("C")
elif (marks<50 and marks>=40):
  print("D")
elif (marks<40 and marks>=1):
  print("E")
else:
  print("ERROR")
  

#ATTEMPT TWO
  
marks=int(input("enter marks; "))
if (marks>=0 and marks<=100):
    if(marks>79 and marks<100):
      value="A"
    elif (marks<=79 and marks>=60):
      value="B"
    elif (marks<60 and marks>=50):
      value="C"
    elif (marks<50 and marks>=40):
      value="D"
    else:
      value="E"
else:
  value="ERROR"

print(value)

#attempt3
marks=int(input("enter marks; "))
if (marks<0 or marks>100):
   value="ERROR"   
else:
  if(marks>=79 and marks<=100):
      value="A"
  elif (marks<=79 and marks>=60):
      value="B"
  elif (marks<60 and marks>=50):
      value="C"
  elif (marks<50 and marks>=40):
      value="D"
  else:
      value="E"

  

print(value)


    
  
  