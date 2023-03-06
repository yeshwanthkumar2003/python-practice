users = []
products=[]
merchantusers=[]
locations = {}
pending_products = []
cart=[]
orders=[]

def signup():
    # Function to sign up a new user
    username = input("Enter username: ")
    password = input("Enter password: ")
    users.append({'username': username, 'password': password})
    print("User signed up successfully.")

def login():
    # Function to authenticate the user
    username = input("Enter username: ")
    password = input("Enter password: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            print("User authenticated successfully.")
            return True
    print("Invalid username or password.")
    return False

def search_brand():
    brand=str(input("Enter the brand to search : "))
    matching_products = []
    for product in products:
        if brand.lower() in product['brand'].lower():
            matching_products.append(product)
    if matching_products:
        print(f"Matching products for brand '{brand}':")
        for i, product in enumerate(matching_products):
            print(f"{i+1}. Product Name: {product['product_name']}")
            print(f"   Price: {product['price']}")
            print(f"   Delivery Location: {product['delivery_location']}")
            print(f"   Offers: {product['offers']}")
            print(f"   Warranty: {product['warranty']}")
            print("")
        choice = input("Enter the number of the product you want to add to cart or 'q' to quit: ")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(matching_products):
                selected_product = matching_products[choice-1]
                cart.append(selected_product)
                print(f"Product '{selected_product['product_name']}' added to cart!")
        elif choice.lower() == 'q':
            print("Quitting...")
        else:
            print("Invalid choice. Quitting...")
    else:
        print(f"No matching products found for brand '{brand}'.")
def my_cart():
    if not cart:
        print("Your cart is empty!")
    else:
        print("Your cart:")
        for i, product in enumerate(cart):
            print(f"{i+1}. Product Name: {product['product_name']}")
            print(f"   Price: {product['price']}")
            print(f"   Delivery Location: {product['delivery_location']}")
            print(f"   Offers: {product['offers']}")
            print(f"   Warranty: {product['warranty']}")
            print("")
def order_now():
    print("****Order Now****")
    product_name = input("Enter product name to order: ")
    found = False
    user_location=input("Enter your location")
    for product in products:
        if product['product_name'] == product_name:
            found = True
            if product['delivery_location'] == user_location:
                print("Product available for delivery to selected location.")
                phone_number = input("Enter phone number: ")
                address = input("Enter delivery address: ")
                pincode = input("Enter delivery pincode: ")
                payment_method = input("Enter payment method: ")
                Orderdate = input("Enter the order date :")
                deliverydate = input("Enter the order date :")

                order = {'product_name': product['product_name'], 'price': product['price'],
                         'phone_number': phone_number, 'address': address, 'pincode': pincode,
                         'payment_method': payment_method,'orderdate':Orderdate,'deliverydate':deliverydate,'delivery_location':user_location}
                orders.append(order)
                print("Order placed successfully!")
                break
            else:
                print("Delivery to the selected location is not available.")
    if not found:
        print("Product not found.")


def cancel_order():
    print("****Cancel Order****")
    product_name = input("Enter product name to cancel: ")
    for order in orders:
        if order['product_name'] == product_name:
            orders.remove(order)
            print("Order for product", product_name, "has been cancelled.")
            print("Your payment has been refunded. Thank you for using our service!")
            break
    else:
        print("No order found for product", product_name)

   

def my_order():
    print("****My Orders****")
    for order in orders:
        print("Product Name:", order['product_name'])
        print("Price:", order['price'])
        print("Delivery Location:", order['delivery_location'])
        print("Delivery Date:", order['deliverydate'])
        print("Order Date:", order['orderdate'])
        print("Payment Method:", order['payment_method'])
        print("------------------------")


def usermodule():
    print("Welcome to Amazon!")
    while True:
        print("1. search the Brand")
        print("2. my cart")
        print("3. Order now")
        print("4. my orders")
        print("5. cancel orders")
        print("6. Exit")
        choice = input("Enter choice number: ")
        if choice == "1":
            search_brand()
        elif choice == "2":
            my_cart()
        elif choice == "3":
            order_now()
        elif choice == "4":
            my_order()
        elif choice == "5":
            cancel_order()
        elif choice == '6':
            print("Thank you for using amazon!")
            main()
        else:
            print("Invalid choice")

# def approve_products():
#     for product in pending_products:
#         if 'approved' not in product or not product['approved']:
#             product['approved'] = True
#             products.append(product)
#             pending_products.remove(product)
#             print(f"{product['product_name']} approved and added to products list!")
#     if not pending_products:
#         print("No pending products to approve.")

def approve_products():
    while pending_products:
        print("Pending Products:")
        for index, product in enumerate(pending_products):
            print(f"{index+1}: {product['product_name']}")
        choice = input("Enter the number of the product you want to approve or 'q' to quit: ")
        if choice == 'q':
            break
        try:
            index = int(choice) - 1
            if index < 0 or index >= len(pending_products):
                print("Invalid input. Please enter a valid product number or 'q' to quit.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid product number or 'q' to quit.")
            continue
        product = pending_products[index]
        approval = input(f"Do you want to approve '{product['product_name']}'? (y/n): ")
        if approval.lower() == 'y':
            product['approved'] = True
            products.append(product)
            pending_products.remove(product)
            print(f"{product['product_name']} approved and added to products list!")
        elif approval.lower() == 'n':
            pending_products.remove(product)
            print(f"{product['product_name']} declined and removed from pending products list.")
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    if not pending_products:
        print("No pending products to approve.")

def add_product():

    product_name=str(input("Enter the product name: "))
    brand=str(input("Enter the brand name: "))
    price=str(input("Enter the price : "))
    delivery_location=str(input("Enter the delivery_location: "))
    offers=str(input("Enter the offers: "))
    warranty=str(input("Enter the wararnty: "))
    material=str(input("Enter the material used"))
    


    product = {
        'brand':brand,
        'product_name': product_name,
        'price': price,
        'delivery_location': delivery_location,
        'offers': offers,
        'warranty': warranty,
        'material':material,
        'approved': False
    }
    products.append(product)
    print("Product added successfully!")
def admin_module():
    while True:
        print("1. Approve products")
        print("2. Add products")
        print("3. Remove products")
        print("4. show approved Products")
        print("5. show products pending for approval")
        print("6. Show location")
        print("7. alter location")
        print("8. Exit")
        choice = input("Enter choice number: ")
        if choice == "1":
            approve_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            remove_product()
        elif choice == "4":
            show_products()
        elif choice == '5':
            show_pendproducts()
        elif choice == "6":
            show_delivery_locations()
        elif choice == '7':
            alter_location()
            print("--------")
        elif choice == "8":
            print("Thank you for using Amazon!")
            main()
        else:
            print("Invalid choice")


def add_pendproduct():

    product_name=str(input("Enter the product name: "))
    brand=str(input("Enter the brand name: "))
    price=str(input("Enter the price : "))
    delivery_location=str(input("Enter the delivery_location: "))
    offers=str(input("Enter the offers: "))
    warranty=str(input("Enter the wararnty: "))
    material=str(input("Enter the material used"))
    


    product = {
        'brand':brand,
        'product_name': product_name,
        'price': price,
        'delivery_location': delivery_location,
        'offers': offers,
        'warranty': warranty,
        'material':material,
        'approved': False
    }
    pending_products.append(product)
    print("Product added successfully!")


def remove_appproduct():
    product_name=str(input("Enter the product name : "))
    for product in pending_products:
        if product['product_name'] == product_name:
            pending_products.remove(product)
            print(f"{product_name} removed successfully!")
    print(f"Product with name {product_name} not found.")



def remove_product():
    product_name=str(input("Enter the product name : "))
    for product in products:
        if product['product_name'] == product_name:
            products.remove(product)
            print(f"{product_name} removed successfully!")
    print(f"Product with name {product_name} not found.")
# Example usage:


def show_products():
    print("List of Products:")
    for product in products:
        print(f"Product Name: {product['product_name']}")
        print(f"brand: {product['brand']}")
        print(f"Price: {product['price']}")
        print(f"Delivery Location: {product['delivery_location']}")
        print(f"Offers: {product['offers']}")
        print(f"Warranty: {product['warranty']}")
        print("")

def show_pendproducts():
    print("List of Products:")
    for product in pending_products:
        print(f"Product Name: {product['product_name']}")
        print(f"brand: {product['brand']}")
        print(f"Price: {product['price']}")
        print(f"Delivery Location: {product['delivery_location']}")
        print(f"Offers: {product['offers']}")
        print(f"Warranty: {product['warranty']}")
        print("")
def show_delivery_locations():
    locations = {}
    for product in products:
        if product['delivery_location'] not in locations:
            locations[product['delivery_location']] = []
        locations[product['delivery_location']].append(product['product_name'])
    print("Delivery Locations:")
    for location in locations:
        print(f"{location}:")
        for product_name in locations[location]:
            print(f"- {product_name}")
        print("")
def alter_location():
    product_name=str(input("Enter the product name: "))
    new_location=str(input("Enter the new location: "))

    for product in products:
        if product['product_name'] == product_name:
            old_location = product['delivery_location']
            product['delivery_location'] = new_location
            print(f"Delivery location of {product_name} changed from {old_location} to {new_location}")
            return
    print(f"Product with name {product_name} not found.")
def merchant_module():
    while True:
        print("1. Add products for approval")
        print("2. Remove products from approval")
        print("3. Show approved products")
        print("4. Show delivery location")
        print("5. remove products")
        print("6. alter location")
        print("7. show pending products ")
        print("8. Exit")
        choice = input("Enter choice number: ")
        if choice == "1":
            add_pendproduct()
        elif choice == "2":
            remove_appproduct()
        elif choice == "3":
            show_products()
        elif choice == "4":
            show_delivery_locations()
        elif choice == '5':
            remove_product()
        elif choice == '6':
            alter_location()
        elif choice == '7':
            show_pendproducts()
            print("--------")
        elif choice == '8':
            print("Thank you for using Amazon!")
            main()
        else:
            print("Invalid choice")
current_user_id = None

def main():
    global usage
    usage = str(input("Enter you are admin or user or merchant :"))
    if(usage=='user'):
         username = input("Enter username: ")
         password = input("Enter password: ")
         users.append({'username': username, 'password': password})
         print("User signed up successfully.")
         username = input("Enter username: ")
         password = input("Enter password: ")
         for user in users:
          if user['username'] == username and user['password'] == password:
            print("User authenticated successfully.")
            usermodule()
            
         print("Invalid username or password.")
         

    elif(usage=='admin'):

        name=str(input("Enter the admin name : "))
        adpassword=str(input("Enter the admin password : "))
        if name == "admin" and adpassword == "1234":
            print("Admin authenticated successfully!")
            admin_module()
        else:
            print("Invalid username or password. Please try again.")
    
    elif(usage=='merchant'):

        merchantusername = input("Enter username: ")
        merchantpassword = input("Enter password: ")
        merchantusers.append({'merchantusername': merchantusername, 'merchantpassword': merchantpassword})
        print("User signed up successfully.")
        merchantusername = input("Enter username: ")
        merchantpassword = input("Enter password: ")
        for meruser in merchantusers:
            if meruser['merchantusername'] == merchantusername and meruser['merchantpassword'] == merchantpassword:
                print("User authenticated successfully.")
                merchant_module()
            
            print("Invalid username or password.")
    
    
    else:
        print("Invalid usage")
main()


