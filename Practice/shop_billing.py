prices = {
    "pen": 10,
    "soap": 20,
    "coffee": 5,
    "tea": 3
}

order = {}
total = 0.0

def display_menu():
    print("\n ---HOME---")
    print("1. Create New Bill")
    print("2. View Current Bill")
    print("0. Exit Program \n")

def get_choice():
    while True: 
        try:
            ch = int(input("Enter you choice: "))
            return ch 
        except ValueError:
            print("Invalid input. Please enter a number.")

def handle_billing():
    global order,total

    if order:
        print("Starting a new bill will clear the previous one.")
        if input("Do you want to start a new bill? (y/n): ").lower() != 'y':
            return
        
    order = {}
    total = 0.0     
    
    print("\n--- New Bill ---")
    print("Available Items:")
    for item,price in prices.items():
        print(f"{item}: ₹{price}")
    print("Enter 'q' to finish the bill.\n")

    while True:
        item = input("Enter item name: ").lower().strip()
        if item == 'q':
            break
        if item in prices:
            price = prices[item]
            order[item] = order.get(item, 0) + 1 
            total += price
            print(f"Added {item}. Running total: ₹{total:.2f}")
        else:
            print(f"Item '{item}' not found. Please check the spelling or enter 'q' to quit.")

    if order:
        print("\n--- Final Bill ---")
        for item, quantity in order.items():
            price_per_unit = prices[item]
            print(f"{item.capitalize()}: {quantity} x ${price_per_unit:.2f} = ${quantity * price_per_unit:.2f}")
        print("-" * 50)
        print(f"Your total bill is: ${total:.2f}")
    else:
        print("Bill cancelled. No items were added.")
        
    print("Thank you for shopping with us!")        

def view_bill():
    if not order:
        print("\nThe current bill is empty.")
        return

    print("\n--- Current Order Details ---")
    for item, quantity in order.items():
        price_per_unit = prices[item]
        print(f"{item.capitalize()}: {quantity} x ₹{price_per_unit:.2f} = ₹{quantity * price_per_unit:.2f}")
    print("-" * 50)
    print(f"Current Total: ₹{total:.2f}")

def main_loop():
    while True:
        display_menu()
        choice = get_choice()
        
        if choice == 1:
            handle_billing()
        elif choice == 2:
            view_bill()
        elif choice == 0:
            print("\nHave a great day!")
            break
        else:
            print("Please select 1, 2, or 0.")

main_loop()            
