name="JOhn"
converted= name.lower()
print(converted)

#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one = "The Dog Breed is German Shepherd"
converted= sentence_one[8:23]
print(converted)

#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two = "Defeats for the Clinton forces, this was her moment of triumph"
converted= sentence_two[16:30]
print(converted)

#“The lazy dog; ran so fast; it hit the wall.” 
sentence_three= "The lazy dog; ran so fast; it hit the wall."
converted=sentence_three.split("; ") 
print(converted)
print(len(converted))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n"
last_name="   Do,e"
first_name= first_name.strip()
converted=first_name.replace(".","")
last_name= last_name.strip()
converted1=last_name.replace(",","")
full_name=converted + " " +converted1
print(full_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
converted= r.replace(",","").replace("[","").replace("]",'').replace('"','')
print(converted)

#floats and integers
#1
#Convert a float to an integer with an inbuilt function in Python
temp = 56.8926 
print(round(temp))
converted=round(temp,2)
print(converted)

#temp = 56.8926 to 56.893 
temp = 56.8926 
print(round(temp))
converted=round(temp,2)
print(converted)
converted1=round(temp,3)
print(converted1)

#temp=56.8926 to 8.926 
#NB: Use string  slice & concatenation, but have result as float 
temp = 56.8926 
temp1= str(temp)
converted=temp1[3:4]
converted1=temp1[4:7]
new_str=converted+"."+converted1
print(converted)
print(new_str)
