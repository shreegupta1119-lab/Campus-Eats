#cart.py
def add_to_cart(cart,item,qty):
    if item in cart:
        cart[item]=cart[item] +qty
    else:
        cart[item] = qty
    print(qty,"item(s) added to cart!")

def remove_from_cart(cart,item, menu):
    if item in cart:
        print(menu[item]["name"] ,"removed from cart!")
        del cart[item]
    else:
        print("Item is not in your cart.")

def update_quantity(cart,item, qty,menu):
    if item in cart:
        if qty >0:
            cart[item]= qty
            print(menu[item]["name"],"quantity updated!")
        else:
            del cart[item]
            print(menu[item]["name"],"removed from cart!")
    else:
        print("Item is not in your cart.")


def calc_total(cart, menu):
    total= 0
    for item in cart:
        total=total+( menu[item]["price"] *cart[item])
    return total

def display_cart(cart,menu):
    if not cart:
        print("Your cart is empty.")
        return
    print("\n========== YOUR CART ==========")

    for item in cart:
        print("\nItem:", menu[item]["name"])
        print("Cafe:", menu[item]["cafe"])
        print("Price: ₹", menu[item]["price"])
        print("Quantity:", cart[item])
        print("Item Total: ₹", menu[item]["price"] *cart[item])

    print("-------------------------------")
    print("Total = ₹", calc_total(cart,menu))
    print("===============================")