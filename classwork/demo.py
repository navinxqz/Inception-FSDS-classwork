# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))
# num3=int(input("Enter third number: "))

# # print(num1, num2, num3)
# if num1<num2 and num1<num3:
#     print(f"{num1} is the smallest number")
# elif num2<num1 and num2<num3:
#     print(f"{num2} is the smallest number")
# else:
#     print(f"{num3} is the smallest number")

menu = input("Hi there! Welcome to ATM \n" \
"Please choose an option: \n" \
"1. Deposit\n" \
"2. Withdraw\n" \
"3. Check Balance\n" \
"4. Exit\n")

if menu == "1":
    amount = float(input("Enter amount to deposit: "))
    print(f"You have deposited ${amount:.2f}")
elif menu == "2":
    amount = float(input("Enter amount to withdraw: "))
    print(f"You have withdrawn ${amount:.2f}")
elif menu == "3":
    balance = 1000.00  # Example balance
    print(f"Your current balance is ${balance:.2f}")
elif menu == "4":
    print("Thank you for using our ATM. Goodbye!")
else:
    print("Invalid option selected. Please try again.")