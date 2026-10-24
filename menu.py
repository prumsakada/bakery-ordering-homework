
def mainMenu():
    print("\n=========================")
    print(" Welcome To Our Bakery ")
    print("=========================")
    print("1. Order Item")
    print("2. View Total")
    print("3. Checkout")
    print("0. Exit")
    print("=========================\n")

def orderItem():
    print("\n=========BARKER MENU==========")
    print("1. Croissant           $10.00")
    print("2. Chocolate Muffin    $2.50")
    print("3. Bread               $2.00")
    print("4. Subtotal ")
    print("0. Back to Main Menu")
    print("==============================\n")

def checkout(subtotal):
    print("\n=========CHECKOUT==========")
    print(f"Subtotal: ${subtotal}")
    discount = float(input("Enter discount(%): "))
    total = subtotal - (subtotal * discount / 100)
    print(f"Discount: {discount}%")
    print("-----------------------------")
    payment = float(input("Enter cash received($): "))
    if payment < total:
        print("Insufficient payment. Please try again.")
    else:
        change = payment - total
        print("\n=========Payment==========")
        print(f"Payment: ${payment:.2f}")
        print(f"Change: ${change:.2f}")
        print(f"Total: ${total:.2f}")
        print("Thank you for your purchase!")
    print("===============================\n")
