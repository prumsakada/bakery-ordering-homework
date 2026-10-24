from menu import orderItem

def orderItems(subtotal=0.00):
    croissant = 10.00
    chocolateMuffin = 2.50
    bread = 2.00
    while True:
        orderItem()
        select = input("-> Enter Your Optaion: ")
        if select == "1":
            subtotal += croissant
            print("\nCroissant added successfully...")
            print(f"Current Subtotal: ${subtotal}\n")
        elif select == "2" :
            subtotal += chocolateMuffin
            print("\nChocolate Muffin added successfully...")
            print(f"Current Subtotal: ${subtotal}\n")
        elif select == "3" :
            subtotal += bread
            print("\nBread added successfully...")
            print(f"Current Subtotal: ${subtotal}\n")
        elif select == "4" :
            print(f"\n===== Subtotal is: ${subtotal} ===\n")           
        elif select == "0" :
            print("\nThank you for ordering...")
            break
        else :
            print("\n-> Invalid option! Please select ( 0 to 3 )!... <-")

    return subtotal