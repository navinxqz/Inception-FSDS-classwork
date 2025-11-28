menu = {
    "Pasta": 250,
    "Pizza": 300,
    "Burger": 150,
    "Salad": 100,
    "Coffee": 50
}
print(
    """
    Welcome to the Restaurant!

    Here is our menu:
    Pasta - 250
    Pizza - 300
    Burger - 150
    Salad - 100
    Coffee - 50
    """
)
total_price = 0
item1=input("Enter the first item you want to order: ")
if item1 in menu:
    total_price += menu[item1]
    print(f"{item1} added to your order. Price: {total_price} TK")
else:
    print(f"Sorry, we don't have {item1} on the menu.")

c = input("Do you want to order another item? (yes/no): ")
if c.lower() == 'yes':
    item2 = input("Enter the second item you want to order: ")
    if item2 in menu:
        total_price += menu[item2]
        print(f"{item2} added to your order. Total Price: {total_price} TK")
    else:
        print(f"Sorry, we don't have {item2} on the menu.")
print(f"Your final total is: {total_price} TK. Thank you.")