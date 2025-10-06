def convert_currency():
    currency_dic = {}
    
    try:
        with open("3.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                data = line.split("\t")
                try:
                    currency_dic[data[0].strip()] = float(data[1].strip())
                except ValueError:
                    print("Warning: Could not convert rate")
    except FileNotFoundError:
        print("Error: File not found.")
        return
    except Exception as e:
        print(f"An unexpected error occurred during file reading: {e}")
        return

    amount = None
    while amount is None:
        try:
            amount = float(input("Enter amount for conversion (in ₹): "))
            if amount < 0:
                print("Amount must be non-negative.")
                amount = None
        except ValueError:
            print("Invalid input. Please enter a valid number for the amount.")
            
    print("\n--- Available Options ---")
    for code in currency_dic.keys():
        print(f"• {code}")

    currency = None
    while currency is None:
        user_input = input("\nPlease enter one of the currency codes above: ").strip()
        if user_input in currency_dic:
            currency = user_input
        else:
            print(f"Invalid currency code '{user_input}'. Please try again.")

    exchange_rate = currency_dic[currency]
    converted_amount = amount * exchange_rate
    print(f"₹{amount:,.2f} equals to {converted_amount:,.2f} {currency}")

convert_currency()
