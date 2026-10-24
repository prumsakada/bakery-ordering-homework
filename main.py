from menu import mainMenu
from function import orderItems
from menu import checkout
import os

def main():
    os.system("clear")
    subtotal = 0.00
    while True:
        mainMenu()
        select = input("-> Enter Your Optaion: ")
        if select == "1":
            subtotal = orderItems(subtotal)
        elif select == "2":
            if subtotal == 0.00:
                print("\n-> your order is empty!")
                print("-> Please order an item first...\n")
            else:
                print(f"\n===== Subtotal is: ${subtotal} =====\n")
            continue
        elif select == "3":
            checkout(subtotal)
            continue
        elif select == "0":
            print("\nThank you for visiting our bakery!")
            print("See you later...\n")
            break
        else:
            print("\n-> Invalid option! Please select ( 0 to 3 )!... <-")




if __name__ == "__main__":
    main()
