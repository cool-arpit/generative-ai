# WAP to calculate total cost of items in a shopping cart

cart = [
    {
        'item': 'APPLE',
        'cost': 5,
        'Quantity': 20
    },
    {
        'item': 'BANANA',
        'cost': 7,
        'Quantity': 15
    },
    {
        'item': 'LYCHEE',
        'cost': 10,
        'Quantity': 10
    }
]

def cart_total(cart_items):
    Total_cost = 0
    for item in cart_items:
        Total_cost += item['cost']*item['Quantity']

    print("THE TOTAL COST OF CART IS : " , Total_cost)

cart_total(cart)
