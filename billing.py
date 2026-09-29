# billing.py

def calc_bill(cart,menu):
    subtotal = 0
    for itemkey in cart:

        qty= cart[itemkey]
        price= menu[itemkey]["price"]
        itemtotal =price* qty
        subtotal= subtotal +itemtotal

    return subtotal

def display_bill(cart, menu, order_id):

    if len(cart) == 0:
        print("\nYour cart is empty.")
        return 0

    print("\n======================================")
    print("          CAMPUS EATS BILL")
    print("======================================")
    print("Order ID:", order_id)
    print("--------------------------------------")

    subtotal = 0

    for itemkey in cart:
        item =menu[itemkey]
        itemname= item["name"]
        cafe =item["cafe"]
        price=item["price"]
        qty= cart[itemkey]

        itemtotal= price*qty

        print("\nItem:",itemname)
        print("Cafe:",cafe)
        print("Price: ₹",price)
        print("Quantity:", qty)
        print("Item Total: ₹",itemtotal)

        subtotal=subtotal +itemtotal
    print("--------------------------------------")
    print("Subtotal: ₹", subtotal)
    print("--------------------------------------")
    print("TOTAL: ₹", subtotal)
    print("======================================")
    print("       Thank you for ordering!")
    print("======================================")

    return subtotal