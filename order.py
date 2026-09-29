
from billing import display_bill

def generate_order_id(order_number):
    return "CE" + str(order_number).zfill(3)


def place_order(cart, menu, order_number, orders):
    if len(cart) == 0:
        print("\nYour cart is empty.")
        print("Please add items before placing an order.")

        return None

    order_id = generate_order_id(order_number)
    print("\nPreparing your bill...")
    total = display_bill(
        cart,
        menu,
        order_id
    )

    print("========== ORDER SUMMARY ==========")
    print("Order ID:", order_id)
    print("-----------------------------------")
    item_details = {}

    for item_key in cart:
        item= menu[item_key]
        item_name =item["name"]
        cafe =item["cafe"]
        price= item["price"]
        quantity =cart[item_key]
        item_total= price* quantity
        print(
            item_name,
            "input",
            quantity,
            "= ₹",
            item_total
        )
        print("Cafe:",cafe)
        item_details[item_key]={
            "name": item_name,
            "cafe": cafe,
            "price": price
        }
    print("-----------------------------------")
    print("Total Amount: ₹", total)
    print("===================================")

    orders[order_id] = {
        "items": cart.copy(),
        "item_details": item_details,
        "total": total,
        "status": "Order Placed"
    }
    
    print("\nOrder placed successfully!")
    print("Your Order ID is:", order_id)

    return order_id