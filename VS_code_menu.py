# Define data structures
price_set = {"apple": 1, "banana": 1, "pear": 1, "orange": 1,
    "broccoli": 1, "carrot": 1, "cucumber": 1, "rutabaga": 1,
    "water": 1, "soda": 1, "juice": 1, "milk": 1
}

stock = {
    "apple": 10, "banana": 20, "pear": 15, "orange": 10,
    "broccoli": 15, "carrot": 20, "cucumber": 25, "rutabaga": 10,
    "water": 20, "soda": 5, "juice": 10, "milk": 10
}

fruits = ["apple", "banana", "pear", "orange"]
vegetables = ["broccoli", "carrot", "cucumber", "rutabaga"]
drinks = ["water", "soda", "juice", "milk"]

# Function to display the menu
def menu_selection():
    print(f"Welcome to The Munch Truck")
    print(f"Please choose your order from the menu below:")
    
    for i, fruit in enumerate(fruits, start=1):
        print(f"{i}. {fruit} - ${price_set[fruit]}")
    
    for a, vegetable in enumerate(vegetables, start=5):
        print(f"{a}. {vegetable} - ${price_set[vegetable]}")
    
    for c, drink in enumerate(drinks, start=9):
        print(f"{c}. {drink} - ${price_set[drink]}")

# Function to handle the ordering process
def handle_order():
    items_blank = []
    total = 0
    
    while True:
        try:
            choice = int(input("Enter the number of the item you would like to order: "))
            
            if 1 <= choice <= len(fruits):
                item = fruits[choice - 1]
            elif 5 <= choice <= 4 + len(vegetables):
                item = vegetables[choice - 5]
            elif 9 <= choice <= 8 + len(drinks):
                item = drinks[choice - 9]
            else:
                print("Invalid choice. Please select a valid item number.")
                continue
            
            if stock[item] > 0:
                quantity = int(input(f"How many {item}s would you like? "))
                if quantity <= stock[item]:
                    total += price_set[item] * quantity
                    items_blank.append((item, price_set[item], quantity))
                    stock[item] -= quantity
                else:
                    print(f"Sorry, we only have {stock[item]} item(s) left.")
            else:
                print(f"Sorry, {item} is out of stock.")
            
            keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").strip().upper()
            if keep_ordering == 'N':
                break
        except ValueError:
            print("You did not choose a valid number. Please try again.")
    
    print("\nThis is what we are preparing for you:\n")
    print("Item name               | Price | Quantity")
    print("----------------------------------------")
    for item, price, quantity in items_blank:
        print(f"{item:20} | ${price:5} | {quantity:8}")
    print(f"Total amount: ${total}")

# Display the menu and start ordering
menu_selection()
handle_order()