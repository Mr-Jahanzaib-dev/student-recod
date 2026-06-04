import math
class Warehouse :
    def __init__(self,id,location):
        self.warehouse = {
            "warehouse_id" : id,
            "location" : location,
            "inventory" :{

            }
        }
        
class Products :
    def __init__(self,id,name,weight):
        self.product = {
            "product_id" : id,
            "product_name" :name,
            "product_weight" : weight
        }

class Orders :
    def __init__(self,order_id, customer_location, items,status,assigned_warehouses,total_distance):
        self.order ={
            "order_id" : order_id,
            "customer_location" : customer_location,
            "items" : items,
            "status" : status,
            "assigned_warehouses" : assigned_warehouses,
            "total_distance" : total_distance
        }
class datamanager :
    def check_data(name):
        with open(f"{name}.csv", "r") as file:
            return file.readlines()

    def fetch_warehouse():
        data = datamanager.check_data("warehouse")
        record = []
        if data:
            for line in data:
                parts = line.strip().split(",")
                warehouse_id = parts[0]
                x = parts[1]
                y = parts[2]
                if len(parts) > 3:
                    inventory_string = parts[3]
                else:
                    inventory_string = ""
                inventory = {}
                if inventory_string:
                    for item in inventory_string.split("|"):
                        pid, qty = item.split(":")
                        inventory[pid] = int(qty)
                warehouse = {
                    "warehouse_id": warehouse_id,
                    "location": (int(x),int(y)),
                    "inventory": inventory
                }
                record.append(warehouse)
        return record

    def write_warehouse(record):
        with open("warehouse.csv", "w") as file:
            for warehouse in record:
                inventory_string = ""
                for pid, qty in warehouse['inventory'].items():
                    inventory_string += f"{pid}:{qty}|"
                if inventory_string:
                    inventory_string = inventory_string[:-1]
                x,y = warehouse['location']
                line = f"{warehouse['warehouse_id']},{x},{y},{inventory_string}\n"
                file.write(line)

    def fetch_product():
        data = datamanager.check_data("product")
        record = []
        if data :
            for line in data :
                product_id,product_name,product_weight = line.strip().split(",")
                Products = {
                    "product_id" : product_id,
                    "product_name":product_name,
                    "product_weight":product_weight
                }
                record.append(Products)
        return record

    def write_product(record):
        with open("product.csv", "w") as file:
            for product in record :
                line = f"{product['product_id']},{product['product_name']},{product['product_weight']}\n"
                file.write(line)

    def fetch_place_order():
        data = datamanager.check_data("place_order")
        record = []
        if data:
            for line in data:
                order_id,x,y,items_string,status,assigned_string,total_distance = line.strip().split(",")

                customer_location = (int(x), int(y))
                items = {}

                if items_string:
                    for item in items_string.split("|"):
                        pid, qty = item.split(":")
                        items[pid] = int(qty)
                assigned_warehouses = []
                if assigned_string:
                    assigned_warehouses = assigned_string.split("|")
                ord = Orders(
                    order_id,
                    customer_location,
                    items,
                    status,
                    assigned_warehouses,
                    float(total_distance)
                )
                record.append(ord.order)
        return record

    def write_place_order(record):
        with open("place_order.csv", "w") as file:
            for order in record:
                x, y = order['customer_location']
                items_string = ""
                for pid, qty in order['items'].items():
                    items_string += f"{pid}:{qty}|"
                if items_string:
                    items_string = items_string[:-1]
                assigned_string = "|".join(order['assigned_warehouses'])
                line = (
                    f"{order['order_id']},"
                    f"{x},"
                    f"{y},"
                    f"{items_string},"
                    f"{order['status']},"
                    f"{assigned_string},"
                    f"{order['total_distance']}\n"
                )
                file.write(line)            

class functionalities :
    def add_warehouse() :
        get_data = datamanager.fetch_warehouse() 
        while True :
            id = input("\nPlease Enter the Warehouse ID :")
            found = False 
            for warehouse in get_data :
                if warehouse['warehouse_id'] == id :
                    found = True
                    break
            if found :
                print("\n\"Please Enter the Unique ID\"\n")
            else :
                if id.upper()[0] == 'W' and id[1:].isdigit():
                    break
                else:
                    print("\n\"Please Enter Warehouse ID in this Format W1,W2\"\n ")
        while True :        
            try :
                x = int(input("\nPlease Enter the x Location :"))
                y = int(input("\nPlease Enter the y Location :"))
                break  
            except ValueError:
                print("\n\"Please Enter the location in Number form \"\n")
        war = Warehouse(id,(x,y))
        get_data.append(war.warehouse)
        datamanager.write_warehouse(get_data)
        print("\n\"warehouse Added Successfully\"\n")  

        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.add_warehouse()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")  

    def add_product() :
        get_data = datamanager.fetch_product() 
        while True :
            id = input("\nPlease Enter the product ID :")
            found = False 
            for product in get_data :
                if product['product_id'] == id :
                    found = True
                    break
            if found :
                print("\n\"Please Enter the Unique ID\"\n")
            else :
                if id.upper()[0] == 'P' and id[1:].isdigit():
                    break
                else:
                    print("\n\"Please Enter Product ID in this Format P1,P2\"\n ")
        while True :        
           name = input("\nPLease Enther the Name of the Product  :")
           if name.isalpha():
            break
           else :
            print("\nPlease Enther The Name in Alphbatic form\n") 
        while True :
            try :
                weight = int(input("\nPlease Enter The Weight Of the Product :"))
                break
            except ValueError:    
                print("Please Enter the weigbht in this Form 12kG , 13KG")    
        weight = f"{weight}kg"
        data = Products(id,name,weight)
        get_data.append(data.product)
        datamanager.write_product(get_data)                            
        print("\n\"Product Added Successfully\"\n") 

        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.add_product()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def stock_product() :
        warehouse_data = datamanager.fetch_warehouse() 
        product_data = datamanager.fetch_product()
        while True :
            id = input("\nPlease Enter the Warehouse ID :")
            if id.upper()[0] == 'W' and id[1:].isdigit():
                warehouse_found = False
                for warehouse in warehouse_data :
                    if warehouse['warehouse_id'].lower() == id.lower() :
                        warehouse_found = True
                        while True :
                            product_id = input("Please Enter the Product Id :")   
                            if product_id.upper()[0] == 'P' and product_id[0] != " " and product_id[1:].isdigit():
                                try :
                                    quantity = int(input("Please Enter the product Quantity :"))
                                    product_found = False
                                    for product in product_data :
                                        if product['product_id'] == product_id :
                                            if product_id in warehouse['inventory'] :
                                                warehouse['inventory'][product_id] += quantity
                                                product_found = True
                                                break 
                                            else :
                                                warehouse['inventory'][product_id] = quantity
                                                product_found = True
                                                break
                                except ValueError :
                                    print("\n Please Enter the Quantity in Numeric Form \n")                     
                                if product_found :        
                                    break
                                else :
                                    print("\nID note Found Plese Enter Correct Id\n")
                            else :
                                print("\n Please Enter the product Id and Quantity in right Format \n")
                if warehouse_found :
                    break
                else :
                    print("\nPlease Enter the correct warehouse ID\n")    
            else:
                print("\n\"Please Enter Warehouse ID in this Format W1,W2\"\n ")
        datamanager.write_warehouse(warehouse_data)        
        print("\n\"Product quantity  Updated Successfully\"\n")
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.stock_product()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")

    def place_order():
        order_data = datamanager.fetch_place_order()
        product_data = datamanager.fetch_product()
        while True:
            order_id = input("Enter Order ID (O1, O2): ")
            if order_id.upper()[0] == 'O' and order_id[1:].isdigit():
                found = False
                for order in order_data:
                    if order['order_id'].lower() == order_id.lower():
                        found = True
                        break
                if found:
                    print("Order ID already exists.")
                else:
                    break
            else:
                print("Please enter Order ID in format O1, O2")
        while True :  
            try:      
                x = int(input("\nPlease Enter the x Location :"))
                y = int(input("\nPlease Enter the y Location :"))
                break  
            except ValueError:
                print("\n\"Please Enter the location in Number form \"\n")    
        customer_location = x,y
        items = {}
        while True:
            product_id = input("Enter Product ID: ")
            product_found = False
            for product in product_data:
                if product['product_id'].lower() == product_id.lower():
                    product_found = True
                    break
            if not product_found:
                print("Product not found.")
                continue
            try:
                quantity = int(input("Enter Quantity: "))
            except ValueError:
                print("Enter quantity in numeric form.")
                continue
            if product_id in items:
                items[product_id] += quantity
            else:
                items[product_id] = quantity
            choice = input("Add another product? (Y/N): ")
            if choice.lower() == 'n':
                break
        order = Orders(order_id,customer_location,items,"Pending",[],0)       
        order_data.append(order.order)
        datamanager.write_place_order(order_data)
        print("\nrder created successfully!\n")
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.place_order()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")
    
    def allocate_inventory():
        order_data = datamanager.fetch_place_order()
        warehouse_data = datamanager.fetch_warehouse()
        order_id = input("Enter Order ID (O1, O2): ")
        order_found = False
        for order in order_data:
            if order['order_id'].lower() == order_id.lower():
                order_found = True
                allocated = True
                order['assigned_warehouses'] = []
                order['total_distance'] = 0
                for product_id, quantity in order['items'].items():
                    product_allocated = False
                    for warehouse in warehouse_data:
                        if product_id in warehouse['inventory']:
                            if warehouse['inventory'][product_id] >= quantity:
                                warehouse['inventory'][product_id] -= quantity
                                if warehouse['warehouse_id'] not in order['assigned_warehouses']:
                                    order['assigned_warehouses'].append(
                                        warehouse['warehouse_id']
                                    )
                                order['total_distance'] += functionalities.calculate_distance(
                                    warehouse['location'],
                                    order['customer_location']
                                )
                                product_allocated = True
                                break
                    if not product_allocated:
                        allocated = False
                        print(f"Insufficient stock for {product_id}")
                if allocated:
                    order['status'] = "Allocated"
                    print("Order Allocated Successfully")
                else:
                    order['status'] = "Pending"
                break
        if not order_found:
            print("Order Not Found")

        datamanager.write_warehouse(warehouse_data)
        datamanager.write_place_order(order_data)
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.allocate_inventory()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")
    def calculate_distance(loc1, loc2):
        x1, y1 = loc1
        x2, y2 = loc2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(distance, 2)
    
    def restock_product():
        warehouse_data = datamanager.fetch_warehouse() 
        product_data = datamanager.fetch_product()
        for warehouse in warehouse_data :
            while True :
                product_id = input("Please Enter the Product Id :")   
                if product_id.upper()[0] == 'P' and product_id[0] != " " and product_id[1:].isdigit():
                    try :
                        quantity = int(input("Please Enter the product Quantity :"))
                        product_found = False
                        for product in product_data :
                            if product['product_id'] == product_id :
                                if product_id in warehouse['inventory'] :
                                    warehouse['inventory'][product_id] += quantity
                                    product_found = True
                                    break 
                                else :
                                    warehouse['inventory'][product_id] = quantity
                                    product_found = True
                                    break
                    except ValueError :
                        print("\n Please Enter the Quantity in Numeric Form \n")                     
                    if product_found :        
                        break
                    else :
                        print("\nID note Found Plese Enter Correct Id\n")   
        datamanager.write_warehouse(warehouse_data)        
        print("\n\"Product quantity  Updated Successfully\"\n")
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.restock_product()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")
    
    def cancel_order():
        order_data = datamanager.fetch_place_order()
        warehouse_data = datamanager.fetch_warehouse()
        order_id = input("Enter Order ID: ")
        order_found = False
        for order in order_data:
            if order['order_id'].lower() == order_id.lower():
                order_found = True
                if order['status'].lower() == "cancelled":
                    print("Order Already Cancelled")
                    return
                for product_id, quantity in order['items'].items():
                    for warehouse in warehouse_data:
                        if warehouse['warehouse_id'] in order['assigned_warehouses']:
                            if product_id in warehouse['inventory']:
                                warehouse['inventory'][product_id] += quantity
                            else:
                                warehouse['inventory'][product_id] = quantity

                            break
                order['status'] = "Cancelled"
                print("Order Cancelled Successfully")
                break
        if not order_found:
            print("Order Not Found")
        datamanager.write_warehouse(warehouse_data)
        datamanager.write_place_order(order_data)
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.cancel_order()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")
        
    def get_low_stock():
        threshold = int(input("Please Enter the Theshold for the product quantity :"))
        warehouse_data = datamanager.fetch_warehouse()
        for warehouse in warehouse_data:
            for product_id, quantity in warehouse['inventory'].items():
                if quantity < threshold:
                    print(product_id, quantity)    
        while True :
            next = input("\n Enter \"Y\" For Adding More student \"N\" For Main Meu \n  ")
            if next.lower() == 'y' :
                functionalities.get_low_stock()
                break
            elif next.lower() == 'n':
                main_menu()
                break
            else :
                print("\n Please Enter Y or N \n")       
def main_menu ():
    while True:
        print("\n========== WARHOUSE  MANAGEMENT SYSTEM ==========")
        print("1. Add Warehouse")
        print("2. Add Product")
        print("3. Stock Product")
        print("4. Place Order")
        print("5. Allocate Inventory")
        print("6. Restock Product")
        print("7. Cancel Order")
        print("8. Get Low Stock")
        while True:
            try:
                choice = input("Enter your choice: ")
                break
            except:
                print("\n\"Please Enter Your Choice in Numeric form\"\n")
        if choice == '1':
            functionalities.add_warehouse()

        elif choice == '2':
            functionalities.add_product()

        elif choice == '3':
            functionalities.stock_product()

        elif choice == '4' :
            functionalities.place_order()
        elif choice == '5':
            functionalities.allocate_inventory()
        elif choice == '6':
            functionalities.restock_product()
        elif choice == '7':
            functionalities.cancel_order()
        elif choice == '8':
            functionalities.get_low_stock()
        else:
            print("Invalid Choice")
main_menu()