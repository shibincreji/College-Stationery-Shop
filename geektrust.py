products = {
    "TSHIRT": {"Category": "Clothing", "Original Price": 1000, "Discount": 10},
    "JACKET": {"Category": "Clothing", "Original Price": 2000, "Discount": 5},
    "CAP": {"Category": "Clothing", "Original Price": 500, "Discount": 20},
    "NOTEBOOK": {"Category": "Stationery", "Original Price": 200, "Discount": 20},
    "PENS": {"Category": "Stationery", "Original Price": 300, "Discount": 10},
    "MARKERS": {"Category": "Stationery", "Original Price": 500, "Discount": 5}
}


def calculate_amt(purchase_item):
    total_amt = 0
    total_discount = 0

    # Calculate total amount
    for product, quantity in purchase_item.items():
        if products[product]["Category"] == "Clothing" and quantity > 2:
            continue
        elif products[product]["Category"] == "Stationery" and quantity > 3:
            continue

        total_amt += products[product]["Original Price"] * quantity

    # Apply discounts
    if total_amt < 1000:
        total_amt

    if total_amt >= 1000:
        for product, quantity in purchase_item.items():
            discount = products[product]["Original Price"] * \
                products[product]["Discount"] / 100
            total_discount += discount * quantity
            total_amt -= discount * quantity

    if total_amt >= 3000:
        discount = total_amt * 5 / 100
        total_discount += discount
        total_amt -= discount

    # Calculate sales tax
    sales_tax = total_amt * 10 / 100
    total_amt += sales_tax

    print("Total Amount is:", total_amt)
    print("Total Discount is:", total_discount)


# Take the user input
purchase_item = {}
while True:
    command = input("Command: ")
    if command == "ADD":
        product = input("Enter the Product: ")
        if product.lower() == "done":
            break
        if product not in products:
            print("Product is not available")
            continue

        quantity = int(input("Enter the quantity: "))
        if product == "NOTEBOOK" or "PENS" or "MARKERS":
            if quantity > 3:
                print("Maximum quantity has reached")
        elif product == "TSHIRT" or "CAP" or "JACKET":
            if quantity > 2:
                print("Maximum quantity has reached")
        purchase_item[product] = quantity
    else:
        break

# Calculate bill
calculate_amt(purchase_item)
