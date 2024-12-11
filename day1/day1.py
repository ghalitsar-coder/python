
# //* PART 7

# number_to_check = int(input("Enter the number to check"))

# if (number_to_check % 2 == 0 ) :
#     print(f"{number_to_check} is an even number")
# else : 
#     print(f"{number_to_check} is an odd number")


    
# //* PART 8

# weight = 80
# height = 1.77

# bmi = weight / (height ** 2)

# if bmi  < 18.5:
#     print("underweight")
# elif bmi >= 18.5 and bmi < 25:
#     print("normal weight")
# else : 
#     print("overweight")


# //* PART 9


# height_to_check = int(input("Enter your height ")) 

# bill =0
# if height_to_check > 120:
#     print(" You can ride")
#     age = int(input("enter your age "))
#     if age < 12:
#         print("its $5")
#         bill += 5
#     elif age >=12 and age < 25:
#         print("its $10")
#         bill += 10
#     elif 45 <= age <=  55:
#         print("its $0")
#         bill += 0
#     else :
#         print("its $15")
#         bill += 15
        
#     extra_photos = input("Extra Photos ? y/Yes , n/No ")
#     if extra_photos in ['y','Yes']:
#         print("its +$3")
#         bill += 3

# else:
#     print("Yout Cannot ride the rollercoaster")
    
    
# if bill != 0 :
#     print(f"Your total bill is ${bill}")
# else :
#     print("No need to pay")

#  //* PART 10

# print("Welcome to pizza delivery")
# size = input("What size of pizza do you want ?  S , M or L ") # S =15 , M =20   , L =30
# pepperoni = input("Do you want extra pepperoni on your pizza ? y or n ") # y+s = 2 , y+m,l = 3
# extra_cheese =  input("Do you want extra cheese ? y for Yes and n for No") # y=1

# bill =  0

# if extra_cheese == "y":
#         bill +=1

# if size.upper() == 'S':
#     bill+=15
#     if pepperoni == "y":
#         bill+=2
   
# elif size.upper() == "M":
#     bill +=20 
#     if pepperoni == "y":
#         bill+=3;
# elif size.upper() == "L":
#     bill +=25
#     if pepperoni == "y":
#         bill+=3;
# else:
#     print("Invalid size. Please choose S, M or L")
    
# print(f"Your total bill is {bill}")


# //* PART 10

print("Welcome to  Treasure island , dont die!")
first_path = input("where do you want to go on , left or right ? ") # left=w , right=l


    
if first_path.lower() == "left":
    second_path =  input("theres a river along the path do you want to wait for boat , swim or wait ? ") #swim=l , wait=w
    if second_path.lower() == "wait":
        third_path = input("Which door do u want to pick ? red, green , blue ") # red=l ,green=w ,blue=l
        if third_path.lower() == "green":
            print("You found treasure!")
        else:
            print("Game over!")
    else :
        print("Game over!")
else :
    print("Game over!")