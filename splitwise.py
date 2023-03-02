users = {}
expenses = []

class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.friends = {}
        self.balance = 0
        self.notifications = []
    def add_friend(self, friend_name):
        self.friends[friend_name] = 0

    def add_expense(self, amount, split_between):
        split_count = len(split_between)
        split_amount = amount / split_count
        self.balance -= amount
        for friend_name in split_between:
            self.friends[friend_name] += split_amount
            friend = users[friend_name]
            friend.notifications.append(f"{self.name} added an expense of {amount} and split it with you")

    def print_balances(self):
        print(f"\nYour balance: {self.balance}","\nReason: ",place)
        for friend_name, balance in self.friends.items():
            print(f"{friend_name}: {balance}")

def signup():
    name = input("\nEnter your name: ")
    password = input("Enter your password: ")
    if name in users:
        print("That name is already taken. Please choose another name.")
    else:
        user = User(name, password)
        users[name] = user
        print(f"Signup successful. Welcome, {name}! ")
        menu()
        print("Please login for the console")


def login():
    name = input("\nEnter your name: ")
    password = input("Enter your password: ")
    if name in users and users[name].password == password:
        print(f"\nWelcome back, {name}!")
        return users[name]
    else:
        print("Invalid login credentials.")
        return None

def add_friend(user):
    friend_name = input("\nEnter your friend's name: ")
    if friend_name in users:
        user.add_friend(friend_name)
        print(f"{friend_name} added as friend.")
    else:
        print("User not found.")

def add_expense(user):
    amount = float(input("\nEnter the expense amount: "))
    global place
    place = str(input("\nEnter the reason for spending the money"))
    split_between = input("Enter the names of the friends to split the expense (comma-separated): ").split(",")
    split_between = [name.strip() for name in split_between]
    user.add_expense(amount, split_between)
    print("Expense added successfully.")


# def pay(user):
#     friend_name = input("\nEnter your friend's name: ")
#     amount = float(input("Enter the amount to pay: "))
#     if friend_name in user.friends:
#         if user.friends[friend_name] >= amount:
#             user.friends[friend_name] -= amount
#             user.balance += amount
#             print(f"You paid {friend_name} {amount}.")
#         else:
#             print("insufficient money")
#     else:
#         print("That friend is not in your list of friends.")
def pay_separately(user):
    while True:
        friend_name = input("\nEnter your friend's name or 'done' to finish: ")
        if friend_name == 'done':
            break
        elif friend_name in user.friends:
            amount = float(input("Enter the amount to pay: "))
            if user.friends[friend_name] >= amount:
                user.friends[friend_name] -= amount
                user.balance += amount
                print(f"You paid {friend_name} {amount}.")
            else:
                print(f"{friend_name} dont have enough balance to make this payment")
        else:
            print("That friend is not in your list of friends.")

def pay(user):
    friend_name = input("\nEnter your friend's name: ")
    amount = float(input("Enter the amount to pay: "))
    if friend_name in user.friends:
        if user.friends[friend_name] >= amount:
            user.friends[friend_name] -= amount
            user.balance += amount
            print(f" {friend_name} paid you  {amount}.")
        else:
            print("Insufficient balance.")
    else:
        print("That friend is not in your list of friends.")

    # Check if there are any other friends that are part of the group payment
    group_payment = input("Is this a group payment? (y/n) ").lower()
    while group_payment == "y":
        other_friend_name = input("\nEnter another friend's name: ")
        if other_friend_name in user.friends:
            amount_to_split = float(input("Enter the amount to split: "))
            if user.friends[other_friend_name] >= amount_to_split:
                user.friends[other_friend_name] -= amount_to_split
                user.balance += amount_to_split
                print(f"{other_friend_name} paid You {amount_to_split}.")
            else:
                print("Insufficient balance.")
        else:
            print("That friend is not in your list of friends.")
        group_payment = input("Is there another friend? (y/n) ").lower()


def menu():
    print("\nWelcome to te splitwise console :)")
    print("  1. signup - create a new account")
    print("  2. login - log in to your account")
menu()

def console():
    print("\nWelcome to Splitwise Console ")
    print("  3. addfriend ")
    print("  4. addexpense ")
    print("  5. list expences")
    print("  6. recieve payment")
    print("  7. help ")
    print("  8. pay seperately ")
    print("  10. exit ")
  

def exit():
    menu()


def run_command(command, user):
    if command == "1":
        signup()
    elif command == "2":
        user = login()
    elif command == "3":
        add_friend(user)
    elif command == "4":
        add_expense(user)
    elif command == "5":
        user.print_balances()
    elif command == "6":
        pay(user)
    elif command == "7":
        run_command()
    elif command == "8":
        pay_separately(user)
    elif command == "9":
        menu()
    else:
        print("Invalid command. Type 'help' for a list of commands.")

    return user

# Main loop
user = None
while True:
    if user is None:
        print("\nSignup for creating the user")
    else:
        print(f"\nLogged in as {user.name}")
        console()
    
    command = input("\n> ").lower()
    user = run_command(command, user)