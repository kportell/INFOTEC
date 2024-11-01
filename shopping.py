#########################
#  Kents Shopping List  #
#########################

def shopping_cart():
# Read items from prices.txt
    items = {}
    try:
        with open('prices.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    name, price = parts
                    items[name] = float(price)
    except FileNotFoundError:
        print("Error: 'prices.txt' file not found.")
        return

# Print items and prices from prices.txt
    print("Available items:")
    for name, price in items.items():
        print(f"{name}: ${price:.2f}")

# User input loop
    order = []
    while True:
        user_input = input("Enter item and quantity (format: name,quantity) or 'done' to finish: ").strip()
        if user_input.lower() == 'done':
            break

        try:
            item_name, quantity = user_input.split(',')
            quantity = int(quantity)
            if quantity < 0:
                print("Quantity cannot be negative, please enter a positive number")
                continue
            if item_name in items:
                unit_price = items[item_name]
                order.append((item_name, unit_price, quantity))
            else:
                print("Item not found. Please enter a valid item.")
        except ValueError:
            print("Invalid format. Please enter in the format 'name,quantity'.")

# Save to cart.txt and return total cost 
    total_amount = 0
    with open('cart.txt', 'w') as file:
        file.write("Name,Unit Price,Quantity,Total Price\n")
        for item_name, unit_price, quantity in order:
            total_price = unit_price * quantity
            total_amount += total_price
            file.write(f"{item_name},{unit_price:.2f},{quantity},{total_price:.2f}\n")

# Print total amount
    print(f"\nTotal amount to pay: ${total_amount:.2f}")
    print("Order has been saved to 'cart.txt'.")


def main():
    shopping_cart()
main()










            

        
