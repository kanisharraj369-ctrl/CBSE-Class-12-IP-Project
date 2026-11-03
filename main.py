"""
PROJECT     : E-COMMERCE MANAGEMENT SYSTEM
CLASS       : XII - INFORMATICS PRACTICES
DESCRIPTION : A menu-driven Python program to manage products, cart,
              customers, orders and sales of a simple online store.
              Uses Lists, Dictionaries, Functions and Matplotlib.
"""

import matplotlib.pyplot as plt

# --------------------------------------------------------------
# GLOBAL DATA
# --------------------------------------------------------------

products = [
    {"id": 101, "name": "Laptop", "category": "Electronics", "price": 45000, "stock": 10},
    {"id": 102, "name": "Mobile Phone", "category": "Electronics", "price": 15000, "stock": 20},
    {"id": 103, "name": "Study Table", "category": "Furniture", "price": 3500, "stock": 15},
    {"id": 104, "name": "Office Chair", "category": "Furniture", "price": 2500, "stock": 12},
    {"id": 105, "name": "Story Book", "category": "Books", "price": 250, "stock": 50},
    {"id": 106, "name": "Notebook Set", "category": "Books", "price": 150, "stock": 60},
    {"id": 107, "name": "Sports Shoes", "category": "Fashion", "price": 2200, "stock": 25},
    {"id": 108, "name": "T-Shirt", "category": "Fashion", "price": 600, "stock": 40},
]

cart = []
customer = {"name": "", "phone": "", "address": ""}

# Sample sales data used only for graphs (category-wise units).
category_sales = {
    "Electronics": 320,
    "Furniture": 150,
    "Books": 210,
    "Fashion": 180,
}

# Sample month-wise sales data (in thousand rupees).
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
month_sales = [120, 135, 150, 130, 160, 175]

# Sample past order values used for the histogram.
past_order_values = [
    500, 1200, 3000, 4500, 2200, 800, 6000, 15000,
    2500, 3200, 1800, 9000, 700, 5200, 4100, 2600
]

# Stores orders placed during the current run of the program.
orders = []


# --------------------------------------------------------------
# FUNCTION DEFINITIONS
# --------------------------------------------------------------

def display_products():
    """Displays all products available in the store."""
    print("\n------ PRODUCT LIST ------")
    print("ID\tName\t\tCategory\tPrice\tStock")
    for product in products:
        print(
            product["id"], "\t",
            product["name"], "\t\t",
            product["category"], "\t",
            product["price"], "\t",
            product["stock"]
        )


def search_product():
    """Searches for a product by name."""
    key = input("Enter product name to search: ").strip()
    found = False

    for product in products:
        if key.lower() in product["name"].lower():
            print("Found:", product)
            found = True

    if not found:
        print("No product found with this name.")


def find_product_by_id(product_id):
    """Returns the product matching the given ID, otherwise None."""
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def add_to_cart():
    """Adds a product to the cart after checking available stock."""
    display_products()

    try:
        product_id = int(input("Enter Product ID to add to cart: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    product = find_product_by_id(product_id)

    if product is None:
        print("Product not found.")
        return

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if quantity > product["stock"]:
        print("Sorry, only", product["stock"], "units are available.")
        return

    cart_item = {
        "id": product["id"],
        "name": product["name"],
        "price": product["price"],
        "qty": quantity
    }

    cart.append(cart_item)
    product["stock"] = product["stock"] - quantity
    print(product["name"], "added to cart successfully.")


def view_cart():
    """Displays all items currently in the cart."""
    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n------ YOUR CART ------")
    print("Name\t\tPrice\tQty\tSubtotal")

    for item in cart:
        subtotal = item["price"] * item["qty"]
        print(item["name"], "\t", item["price"], "\t", item["qty"], "\t", subtotal)


def calculate_bill():
    """Calculates the cart total and applies the applicable discount."""
    if len(cart) == 0:
        print("\nCart is empty. Add products first.")
        return 0

    total = 0
    for item in cart:
        total = total + (item["price"] * item["qty"])

    discount = 0
    if total >= 20000:
        discount = total * 0.10
    elif total >= 10000:
        discount = total * 0.05

    final_amount = total - discount

    print("\n------ BILL SUMMARY ------")
    print("Total Amount     : Rs.", total)
    print("Discount Applied : Rs.", round(discount, 2))
    print("Final Amount     : Rs.", round(final_amount, 2))

    return round(final_amount, 2)


def enter_customer_details():
    """Takes and stores customer information in a dictionary."""
    customer["name"] = input("Enter your name: ")
    customer["phone"] = input("Enter your phone number: ")
    customer["address"] = input("Enter your address: ")
    print("Customer details saved successfully.")


def display_customer_details():
    """Displays the stored customer information."""
    if customer["name"] == "":
        print("\nNo customer details found. Please enter details first.")
    else:
        print("\n------ CUSTOMER DETAILS ------")
        print("Name    :", customer["name"])
        print("Phone   :", customer["phone"])
        print("Address :", customer["address"])


def place_order():
    """Places an order using the current cart and customer details."""
    if customer["name"] == "":
        print("\nPlease enter customer details before placing an order.")
        return

    if len(cart) == 0:
        print("\nCart is empty. Add products before placing an order.")
        return

    final_amount = calculate_bill()
    order_number = len(orders) + 1

    order = {
        "order_no": order_number,
        "customer": customer["name"],
        "items": list(cart),
        "amount": final_amount
    }

    orders.append(order)
    print("\nOrder placed successfully! Your Order No. is", order_number)

    # Empty the cart after placing the order.
    cart.clear()


def display_orders():
    """Displays details of all orders placed during this run."""
    if len(orders) == 0:
        print("\nNo orders have been placed yet.")
        return

    print("\n------ ORDER DETAILS ------")
    for order in orders:
        print("\nOrder No :", order["order_no"])
        print("Customer :", order["customer"])
        print("Amount   : Rs.", order["amount"])
        print("Items    :")

        for item in order["items"]:
            print("   -", item["name"], "x", item["qty"])


def display_sales_info():
    """Displays sample category-wise sales information."""
    print("\n------ CATEGORY-WISE SALES (Sample Data) ------")
    for category in category_sales:
        print(category, ":", category_sales[category], "units")


def show_bar_chart():
    """Displays a bar chart of category-wise sales."""
    categories = list(category_sales.keys())
    sales = list(category_sales.values())

    plt.bar(categories, sales, color="skyblue")
    plt.title("Category-wise Sales")
    plt.xlabel("Product Category")
    plt.ylabel("Units Sold")
    plt.savefig("bar_chart.png")
    plt.show()


def show_line_graph():
    """Displays a line graph of month-wise sales."""
    plt.plot(
        month_names, month_sales,
        color="green", marker="o",
        label="Sales (in '000 Rs.)"
    )
    plt.title("Month-wise Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales (in thousand Rs.)")
    plt.legend()
    plt.savefig("line_graph.png")
    plt.show()


def show_histogram():
    """Displays a histogram of sample order values."""
    plt.hist(past_order_values, bins=5, color="orange", edgecolor="black")
    plt.title("Distribution of Order Values")
    plt.xlabel("Order Value (Rs.)")
    plt.ylabel("Number of Orders")
    plt.savefig("histogram.png")
    plt.show()


def graph_menu():
    """Displays the graph sub-menu."""
    print("\n---- GRAPH MENU ----")
    print("1. Bar Chart (Category-wise Sales)")
    print("2. Line Graph (Month-wise Sales)")
    print("3. Histogram (Order Value Distribution)")
    print("4. Back to Main Menu")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_bar_chart()
    elif choice == "2":
        show_line_graph()
    elif choice == "3":
        show_histogram()
    elif choice == "4":
        return
    else:
        print("Invalid choice.")


# --------------------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------------------

def main():
    while True:
        print("\n===================================")
        print("     E-COMMERCE MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Display Products")
        print("2. Search Product")
        print("3. Add Product to Cart")
        print("4. View Cart")
        print("5. Calculate Total Bill")
        print("6. Enter Customer Details")
        print("7. Display Customer Details")
        print("8. Place Order")
        print("9. Display Order Details")
        print("10. Display Sales Information")
        print("11. Show Graphs")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            search_product()
        elif choice == "3":
            add_to_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            calculate_bill()
        elif choice == "6":
            enter_customer_details()
        elif choice == "7":
            display_customer_details()
        elif choice == "8":
            place_order()
        elif choice == "9":
            display_orders()
        elif choice == "10":
            display_sales_info()
        elif choice == "11":
            graph_menu()
        elif choice == "12":
            print("Thank you for shopping with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 12.")


# Program execution starts here.
if __name__ == "__main__":
    main()
