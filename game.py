import random
cnum= random.randrange(1,101)
unum= int(input("Enter your Number-->"))

if cnum>unum:
    print("Computr number : ", cnum)
    print("Your guess number is too low")

elif unum>cnum:
    print("Computr number : ", cnum)
    print("Your guess number is too high")

else:
    print("Computr number : ", cnum)
    print("Your guess number is equal")
    
