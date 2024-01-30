#Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF.
basic_salary=int(input("enter basic salary; "))
benefits=int(input("enter benefits; "))
gross_salary=basic_salary+benefits
if (gross_salary <= 5999):
        print("nhif 150")
elif (gross_salary > 5999 and gross_salary <= 7999):
        print("nhif 300")
elif (gross_salary > 7999 and gross_salary <= 11999):
        print("nhif 400")
elif (gross_salary > 11999 and gross_salary <= 14999):
        print("nhif 500")
elif (gross_salary > 14999 and gross_salary <= 19999):
        print("nhif 600")
elif (gross_salary > 19999 and gross_salary <= 24999):
        print("nhif 750")
elif (gross_salary > 24999 and gross_salary <= 29999):
        print("nhif 850")
elif (gross_salary > 29999 and gross_salary <= 34999):
        print("nhif 900")
elif (gross_salary > 34999 and gross_salary <= 39999):
        print("nhif 950")
elif (gross_salary > 39999 and gross_salary <= 44999):
        print("nhif 1000")
elif (gross_salary > 44999 and gross_salary <= 49999):
        print("nhif 1100")
elif (gross_salary > 49999 and gross_salary <= 59999):
        print("nhif 1200")
elif (gross_salary > 59999 and gross_salary <= 69999):
        print("nhif 1300")
elif (gross_salary > 69999 and gross_salary <= 79999):
        print("nhif 1400")
elif (gross_salary > 79999 and gross_salary <= 89999):
        print("nhif 1500")
elif (gross_salary > 89999 and gross_salary <= 99999):
        print("nhif 1600")
else:
        print("nhif 1700")

#TASK 16: 
#Compute NSSF using 6% of the Gross Salary. BUT ONLY A MAXIMUM OF 18,000 CAN BE USED IN NSSF. 

if(gross_salary<18000):
        nssf=gross_salary*0.06
else:
  nssf=18000*0.06

print(nssf)

# Compute NHDF using:
 #NHDF = gross_salary *  0.015


