#Cafe.py

from menu_data import menu_data
from cart import (
    add_to_cart,
    remove_from_cart,
    update_quantity,
    display_cart
)
from order import place_order


def display_cafes():
    print("========== CAMPUS EATS ==========")
    cafe_names = list(menu_data.keys())
    for index in range(len(cafe_names)):
        print(index + 1, ".", cafe_names[index])
    print("=================================")

def display_cafe_menu(cafe_name):
    print("======================================")
    print("          ", cafe_name)
    print("======================================")

    categories = menu_data[cafe_name]
    item_number = 1
    for category in categories:
        print("---", category, "---")
        items = categories[category]
        for item in items:
            print(
                item_number,
                ".",
                item[0],
                "- ₹",
                item[1]
            )
            item_number = item_number + 1
def get_cafe_items(cafe_name):
    cafe_items= []
    categories =menu_data[cafe_name]
    for category in categories:
        items= categories[category]
        for item in items:
            cafe_items.append(item)
    return cafe_items

def create_all_items():
    all_items= {}
    for cafe in menu_data:
        categories = menu_data[cafe]
        for category in categories:
            items =categories[category]
            for item in items:
                item_name =item[0]
                price =item[1]
                item_key= cafe + " - " + item_name
                all_items[item_key] = {
                    "name": item_name,
                    "price": price,
                    "cafe": cafe,
                    "category": category
                }
    return all_items

def select_cafe():
    display_cafes()
    cafe_choice = input("\nEnter cafe number: ")
    if cafe_choice.isdigit():
        cafe_choice = int(cafe_choice)
        cafe_names = list(menu_data.keys())
        if cafe_choice >= 1 and cafe_choice <= len(cafe_names):
            return cafe_names[cafe_choice - 1]
        else:
            print("Invalid cafe number.")
    else:
        print("Please enter a number.")
    return None
def add_item_from_cafe(cart, all_items):
    cafe_name = select_cafe()
    if cafe_name is None:
        return
    while True:
        display_cafe_menu(cafe_name)
        print("\n0. Back")
        choice = input("\nEnter item number: ")
        if choice == "0":
            break

        if choice.isdigit():
            choice = int(choice)
            cafe_items = get_cafe_items(cafe_name)

            if choice >= 1 and choice <= len(cafe_items):
                selected_item = cafe_items[choice - 1]
                item_name = selected_item[0]
                item_key = cafe_name + " - " + item_name
                quantity = input("Enter quantity: ")

                if quantity.isdigit():
                    quantity = int(quantity)

                    if quantity > 0:
                        add_to_cart(
                            cart,
                            item_key,
                            quantity
                        )
                        print(
                            "",
                            item_name,
                            "from",
                            cafe_name,
                            "added successfully!"
                        )
                        break

                    else:
                        print(
                            "Quantity must be greater than 0."
                        )

                else:
                    print(
                        "Please enter a valid quantity."
                    )

            else:
                print("Invalid item number.")

        else:
            print("Please enter a number.")

def show_order_history(orders):

    if len(orders) == 0:
        print("========== ORDER HISTORY ==========")
        print("No previous orders found.")
        print("===================================")
        return

    print("========== ORDER HISTORY ==========")

    for order_id in orders:
        order = orders[order_id]
        print("\nOrder ID:", order_id)
        print("-----------------------------------")
        print("Items:")

        for item_key in order["items"]:
            quantity = order["items"][item_key]

            if "item_details" in order:
                item_details =order["item_details"][item_key]
                item_name= item_details["name"]
                cafe =item_details["cafe"]
                print(
                    " ",
                    item_name,
                    "x",
                    quantity
                )
                print(
                    "    Cafe:",
                    cafe
                )

            else:
                print(
                    " ",
                    item_key,
                    "x",
                    quantity
                )
        print("Total Amount: ₹", order["total"])
        print("Status:", order["status"])
        print("-----------------------------------")
    print("===================================")


def main():
    cart= {}
    orders = {}
    order_number= 1
    all_items= create_all_items()
    print("======================================")
    print("       WELCOME TO CAMPUS EATS")
    print("    Your Campus Food Ordering System")
    print("======================================")

    while True:
        print("----------- MAIN MENU -----------")
        print("1. View Cafes & Menu")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. Update Quantity")
        print("5. View Cart")
        print("6. Place Order")
        print("7. Order History")
        print("8. Exit")
        print("--------------------------------")
        choice = input("Enter your choice: ")

        if choice == "1":
            cafe_name = select_cafe()
            if cafe_name is not None:
                display_cafe_menu(cafe_name)

        elif choice == "2":
            add_item_from_cafe(
                cart,
                all_items
            )

        elif choice == "3":
            display_cart(
                cart,
                all_items
            )

            if len(cart) >0:
                print("\nItems in your cart:")
                item_number =1
                item_keys =list(cart.keys())

                for item_key in item_keys:
                    item=all_items[item_key]
                    print(
                        item_number,
                        ".",
                        item["name"],
                        "-",
                        item["cafe"]
                    )
                    item_number = item_number + 1
                choice = input(
                    "\nEnter item number to remove: "
                )
                if choice.isdigit():
                    choice = int(choice)

                    if choice >= 1 and choice <= len(item_keys):
                        item_key = item_keys[choice - 1]
                        remove_from_cart(
                            cart,
                            item_key,
                            all_items
                        )
                    else:
                        print("Invalid item number.")
                else:
                    print("Please enter a number.")
        elif choice == "4":
            display_cart(
                cart,
                all_items
            )
            if len(cart) > 0:
                print("\nItems in your cart:")
                item_number = 1
                item_keys = list(cart.keys())
                for item_key in item_keys:
                    item = all_items[item_key]
                    print(
                        item_number,
                        ".",
                        item["name"],
                        "-",
                        item["cafe"]
                    )
                    item_number = item_number + 1
                choice = input(
                    "\nEnter item number: "
                )
                if choice.isdigit():
                    choice = int(choice)
                    if choice >= 1 and choice <= len(item_keys):
                        item_key = item_keys[choice - 1]
                        quantity = input(
                            "Enter new quantity: "
                        )
                        if quantity.isdigit():
                            quantity = int(quantity)
                            update_quantity(
                                cart,
                                item_key,
                                quantity,
                                all_items
                            )
                        else:
                            print(
                                "Please enter a valid quantity."
                            )
                    else:
                        print("Invalid item number.")
                else:
                    print("Please enter a number.")
        elif choice == "5":
            display_cart(
                cart,
                all_items
            )
        elif choice == "6":
            order_id = place_order(
                cart,
                all_items,
                order_number,
                orders
            )

            if order_id is not None:
                order_number = order_number + 1
                cart.clear()

        elif choice == "7":
            show_order_history(
                orders
            )
        elif choice == "8":
            print(
                "\nThank you for using Campus Eats!"
            )
            print(
                "Goodbye! 👋"
            )
            break
        else:
            print(
                "\nInvalid choice. Please try again."
            )
main()




