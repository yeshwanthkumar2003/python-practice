# usages = {'Admin':{'usagepin':'Admin'},
#          'user':{'usagepin':'0'}}

accounts = {'yeshwanth': {'pin': '1234', 'balance': 1000, 'transaction_history': []},
            'kiruthick': {'pin': '5678', 'balance': 5000, 'transaction_history': []},
            'vini': {'pin': '9012', 'balance': 20000, 'transaction_history': []},
            'varun': {'pin': '2023', 'balance': 12000, 'transaction_history': []}}

# def auth():
#     print("welcome to Yesh Bank")
#     usage = input("Enter your usage : ")
#     if usage == 'Admin' or 'admin':
#         return admin(usage)
#     else:
#         authenticate()

# def admin():
#     print("welcome to yesh bank admin portal")

atmbalance = 200000

def authenticate():
    print("Welcome to yesh bank")
    username = input("Enter your username: ")
    pin = input("Enter your PIN: ")
    if username in accounts.keys() and accounts[username]['pin'] == pin:
        return username
    else:
        print("Invalid username or PIN. Please try again.")
        return False


def menu():
    print("Welcome to YESH bank \n1. Check balance\n2. Withdraw\n3. Deposit\n4. Change PIN\n5. Transaction history\n6. Showpin\n7. Exit")
    choice = input("Enter choice (1-7): ")
    return choice

def adminmenu():
    print("Welcome admin to yeshbank ! \n1. Load money into ATM\n2. check ATM Balance \n3. Exit")
    choice = input("Enter choice (1-3): ")
    return choice

# def mainmenu():
#     print("Welcome to the main menu")
#     print("\n1.Admin\n2. User")
#     port=input("enter a port no:")
#     return port




def check_balance(username):
    balance = accounts[username]['balance']
    print(f"Your current balance is: {balance}")

def withdraw(username):
    global atmbalance
    amount = float(input("Enter amount to withdraw: "))
    balance = accounts[username]['balance']
    if amount > balance:
        print("Insufficient funds.")
    else:
        accounts[username]['balance'] -= amount
        accounts[username]['transaction_history'].append(f"Withdrawn {amount} from account.")
        print(f"Withdrawn {amount} from account.")
        atmbalance -= amount




def deposit(username):
    amount = float(input("Enter amount to deposit: "))
    accounts[username]['balance'] += amount
    accounts[username]['transaction_history'].append(f"Deposited {amount} into account.")
    print(f"Deposited {amount} into account.")


def change_pin(username):
    new_pin = input("Enter new PIN: ")
    accounts[username]['pin'] = new_pin
    print("PIN changed successfully.")

def showpin(username):
    print(accounts[username]['pin'])

def transaction_history(username):
    history = accounts[username]['transaction_history']
    print("Transaction history:")
    for transaction in history:
        print(transaction)

# /def adminportal(usage):
#     print("welcome to the admin portal")
# def loadamount(usage):
#     print("load a amount")


# usage = auth()
# if usage:
#     while True:
#         port = auth()
#         if port == '1':
#             print("Welcome to Admin portal")
#         if port == '2':
#             authenticate()
def loadmoney():
    global atmbalance
    amount = float(input("Enter the amount of money to be loaded: "))
    denominations = [2000, 500, 200, 100, 50, 20, 10]
    notes = {}
    for d in denominations:
        count = int(input(f"Enter the number of {d} notes: "))
        notes[d] = count
    total = sum(denomination*count for denomination, count in notes.items())
    if total != amount:
        print("Invalid specified amount")
    else:
        atmbalance += amount
        print(f"{amount} loaded into the ATM.")

   


def checkmoney():
    global atmbalance
    print(f"The ATM balance is: {atmbalance}")


while True:
    choice=input("Welcome to YESH Bank ! \nYou are Admin or User: ")
    if choice == 'user':
        username = authenticate()
        if username:
            while True:
                choice = menu()
                if choice == '1':
                    check_balance(username)
                elif choice == '2':
                    withdraw(username)
                elif choice == '3':
                    deposit(username)
                elif choice == '4':
                    change_pin(username)
                elif choice == '5':
                    transaction_history(username)
                elif choice == '6':
                    showpin(username)
                elif choice == '7':
                    print("Thank you for using yesh bank")
                    break
                else:
                    print("Invalid choice. Please try again.")
    elif choice == 'admin':
        adminpin=input("Enter admin pin: ")
        if adminpin == 'admin':
            while True:
                choice = adminmenu()
                if choice == '1':
                    loadmoney()
                elif choice == '2':
                    checkmoney()
                elif choice == '3':
                    break
                else:
                    print("Invalid choice.Please try again")
        else:
            print("Invalid admin PIN.please try again")
    else:
        print("Invalid choice.please try again")
        continue
    exit_choice = input("Do you want to exit?")
    if exit_choice == 'yes':
        break

    print("Thank you for using yeshbank")



