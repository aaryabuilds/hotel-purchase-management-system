purchase_orders = []
def approval_required(total_cost):
    if total_cost <= 10000:
        return "Supervisor"
    elif total_cost <= 50000:
        return "Department Manager"
    else:
        return "Finance Head"

def purchase_invoice(employee_name, item_name, quantity, unit_price):
    total_cost = quantity*unit_price
    print("\n--- PURCHASE ORDER SUMMARY ---")
    print(f"Employee Name: {employee_name}")
    print(f"Item Name: {item_name}")
    print(f"Quantity: {quantity}")
    print(f"Unit Price: ₹{unit_price}")
    print(f"Total Cost: ₹{total_cost}")
    print(f"Approval Required: {approval_required(total_cost)}")
    
    if total_cost > 100000:
        print("Warning : High-Value Purchase")
    print()

def purchase_order():
    employee_name = input("Enter the Employee Name: ").strip()
    item_name = input("Enter the name of the item: ").strip()

    try:
        quantity = int(input("Enter the quantity of the item: "))
        unit_price = float(input("Enter the price of 1 unit: "))

        if not employee_name or not item_name or quantity <= 0 or unit_price <= 0:
            print("Please enter a valid details.")
            return
        else:
            purchase_invoice(employee_name, item_name, quantity, unit_price)

        order = {
            "id": len(purchase_orders) + 1,
            "employee": employee_name,
            "item": item_name,
            "quantity": quantity,
            "unit_price": unit_price,
            "total_cost": quantity * unit_price,
            "approval": approval_required(quantity * unit_price)
        }

        purchase_orders.append(order)

    except ValueError:
        print("Invalid Input")


def view_orders():
    if not purchase_orders:
        print("No purchase order found")
        return

    else:
        print("==== ALL PURCHASE ORDERS ====")
        for order in purchase_orders:   
            print(f"REQUEST ID: {order['id']}")
            print(f"EMPLOYEE NAME: {order['employee']}")
            print(f"ITEM NAME: {order['item']}")
            print(f"TOTAL: {order['total_cost']}")
            print(f"AAPROVAL REQUIRED: {order['approval']}")
        

def switch_case(option):
    match option:
        case 1:
            purchase_order()                
        case 2:
            view_orders()
        case 3:
            print("Visit Us Again")
        case _:
            print("Invalid Choice")  

while True:
    print("\n==== HOTEL PURCHASE SYSTEM ====")
    print("1. Create A Purchase Request")
    print("2. View All Orders")
    print("3. Exit")

    option = input("Enter your choice: ")

    if option == "3":
        print("Visit Us Again")
        break

    try:
        switch_case(int(option))
    except ValueError:
        print("Invalid Choice")