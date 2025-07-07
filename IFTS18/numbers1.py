#Code that shows if the first number is bigger, smaller, or equal to the other

print("Let's see if the first number is bigger, smaller or equal to the other")
num1=int(input("Write the first number please:"))
num2=int(input("Now write the next number:"))
if num1 > num2:
    print(f"{num1} is bigger than {num2}")
elif num1 < num2:
    print(f"{num1} is smaller than {num2}")
else:
    print ("Both numbers are equal")
