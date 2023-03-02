accounts = {'yeshwanth': {'password':'1234' ,'history':[]},
            'varun':{'password':'5678','history':[]}}

availible_seats = ["A1","A2","A3","A4","B1","B2","B3","B4","C1","C2","C3","C4"]
boarding_points=["coimbatore","Trichy","chennai","salem","Erode"]
destination_points=["coimbatore","Trichy","chennai","salem","Erode"]
passenger_details = {}
waiting_list=[]
booked_seats={}


def authenticate():
    print("Welcome to YESH Travels")
    global username
    username =input('Enter your username: ')
    password = input('Enter the passwd: ')
    if username in accounts.keys() and accounts[username]['password'] == password:
        return username
    else:
        print("invalid username.please try again")
        return False
    
def menu():
    print("Welcome to YESH Travels \n1. Check seats\n2. book my seats\n3.history\n4. waiting list\n5. cancellation\n6. Exit")
    choice = input("Enter choice (1-7): ")
    return choice
def check_seat():
    print("\nthe availible seats:" ,availible_seats)
book_seat = {}
passenger_details = {}

def bookmy_seat():
    global username
    seat = input("Enter your seat number: ")
    if seat in availible_seats:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        gender = input("Enter your gender: ")
        boarding=input("Enter your boarding point: ")
        destination = input("Enter your destination point: ")
        if boarding in boarding_points and destination in destination_points:
            availible_seats.remove(seat)
            print("Seat booked successfully")
            print("name: ",name)
            print("age: ",age)
            print("gender: ",gender)
            print("Boarding point is : ",boarding)
            print("Destination point is : ", destination)
            passenger_details[seat] = {"name": name, "age": age, "gender": gender, "boarding": boarding, "destination": destination}
            book_seat[seat] = {"name": name, "age": age, "gender": gender, "boarding": boarding, "destination": destination, "username": username}
        else:
            print("\nChoose valid Boarding point")

    else:
        print("Seat not available.")
        response = input("Do you want to be added to the waiting list? Press 'y' for yes and 'n' for no.")
        if response == 'y':
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            gender = input("Enter your gender: ")
            waiting_list.append({"seat": seat, "name": name, "age": age, "gender": gender})
            print(f"Congratulations! Your seat {seat} has been added to the waiting list. We will notify you soon.")
        else:
            print("Okay, no problem.")




def cancelseat():
    
    
    # Check if user is logged in
    if not username:
        print("You must be logged in to cancel a seat.")
        return
    
    seat = input("Enter seat number to cancel: ")
    
    if seat in book_seat:
        # Check if user is canceling their own seat
        if book_seat[seat]["username"] == username:
            del book_seat[seat]
            availible_seats.append(seat)
            print("Seat cancelled successfully.")
            
            # Check if there are users on the waiting list to assign seat to
            if waiting_list:
                next_passenger = waiting_list.pop(0)
                next_seat = next_passenger["seat"]
                if 'username' in next_passenger:

                book_seat[next_seat] = {"username": next_passenger["username"], "details": next_passenger["details"]}
                print("Seat", next_seat, "assigned to", next_passenger["username"])
                
        else:
            print("You cannot cancel someone else's seat.")
    
    else:
        print("Seat not found.")





# def order_summary():
#     print("Your seat number is"+seat)
def history():
    if passenger_details:
        print("Here is the list of passengers who have booked a seat:")
        for seat, details in passenger_details.items():
            print(f"Seat Number: {seat}\nName: {details['name']}\nAge: {details['age']}\nGender: {details['gender']}")
    else:
        print("No seats have been booked yet.")

def exit():
    return authenticate()

    
while True:
    # choice=input("\ntype 'user'")
    # if choice == 'user':
    #     username = authenticate()
        if authenticate():
            while True:
                choice=menu()
                if choice == '1':
                    check_seat()
                elif choice == '2':
                    bookmy_seat()
                elif choice == '3':
                    history()
                elif choice == '4':
                    print("The waiting list: ",waiting_list)
                elif choice == '5':
                    cancelseat()
                elif choice=='6':
                    exit()
                
                    