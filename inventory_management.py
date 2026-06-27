# Inventory Management System

inventory = {}


# Add Product
def add_product():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:
        print("Product ID Already Exists!")
        return

    name = input("Enter Product Name: ")
    category = input("Enter Category: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    reorder_level = int(input("Enter Reorder Level: "))

    inventory[product_id] = {
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "reorder_level": reorder_level
    }

    print("Product Added Successfully!")


# Stock In
def stock_in():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:

        qty = int(input("Enter Quantity to Add: "))

        inventory[product_id]["quantity"] += qty

        print("Stock Updated Successfully!")

    else:
        print("Product Not Found")


# Stock Out
def stock_out():

    product_id = input("Enter Product ID: ")

    if product_id in inventory:

        qty = int(input("Enter Quantity to Remove: "))

        if qty <= inventory[product_id]["quantity"]:

            inventory[product_id]["quantity"] -= qty

            print("Stock Removed Successfully!")

        else:
            print("Not Enough Stock!")

    else:
        print("Product Not Found")


# View Inventory
def view_inventory():

    if len(inventory) == 0:
        print("No Products Available")
        return

    print("\n===== INVENTORY =====")

    for pid, product in inventory.items():

        print("\nProduct ID :", pid)
        print("Name :", product["name"])
        print("Category :", product["category"])
        print("Price :", product["price"])
        print("Quantity :", product["quantity"])
        print("Reorder Level :", product["reorder_level"])


# Low Stock Alert
def low_stock_alert():

    print("\n===== LOW STOCK PRODUCTS =====")

    found = False

    for pid, product in inventory.items():

        if product["quantity"] <= product["reorder_level"]:

            found = True

            print(pid, "-", product["name"])

    if found == False:
        print("No Low Stock Products")


# Generate Report
def generate_report():

    total_products = len(inventory)

    total_value = 0

    for product in inventory.values():

        total_value += (
            product["price"] * product["quantity"]
        )

    print("\n===== INVENTORY REPORT =====")
    print("Total Products :", total_products)
    print("Total Stock Value :", total_value)


# Main Menu
while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. Stock In")
    print("3. Stock Out")
    print("4. View Inventory")
    print("5. Low Stock Alert")
    print("6. Report")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        stock_in()

    elif choice == "3":
        stock_out()

    elif choice == "4":
        view_inventory()

    elif choice == "5":
        low_stock_alert()

    elif choice == "6":
        generate_report()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")