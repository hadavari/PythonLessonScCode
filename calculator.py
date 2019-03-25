#--------------Calculator_------------------------------------------
numberOne = int(input("Input the first number"))
numberTwo = int(input("Input the second number"))

print("Choose choices from 1-4")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
choice = input()
if choice == "1":
    print(numberOne + numberTwo)
elif choice == "2":
    print(numberOne - numberTwo)
elif choice == "3":
    print(numberOne * numberTwo)
elif choice == "4":
    print(numberOne / numberTwo)
else:
    print("Please choose a number between 1-4")