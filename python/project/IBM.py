weight = float(input("Enter your weight in kg:"))
height= float(input("Enter your height in meters:"))

height=height/100
BMI = weight/(height*2)
print(BMI)

if(BMI <16):
    print("You are severrly underweight"), BMI

elif(BMI > 16 and BMI < 18.5):
    print("you are underweight"), BMI 

elif(BMI >= 18.5 and BMI < 24):
    print("you are highly"), BMI 

elif (BMI>= 25 and  BMI < 30): 
    print("you  are overweight"), BMI 

elif(BMI >=30):
    print("you are obese"), BMI