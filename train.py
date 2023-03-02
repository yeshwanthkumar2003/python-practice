from datetime import datetime
# initialize seat status and waiting list
seats = {"A1": None, "A2": None, "A3": None, "A4": None, "A5": None}
waiting_list = []
accounts = {'yeshwanth': {'password':'1234' ,'history':[]},
            'varun':{'password':'5678','history':[]},
            'vini':{'password':'1507','history':[]}}
boarding_points=["coimbatore","Trichy","chennai","salem","Erode"]
destination_points=["coimbatore","Trichy","chennai","salem","Erode"]
# user authentication
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
# check seats availability
def check_availability():
    available_seats = [seat for seat in seats if seats[seat] is None]
    print("Available seats:", available_seats)

# # book a seat
# def book_seat():
#     name = input("Enter name: ")
#     age = int(input("Enter age: "))
#     boarding_point = input("Enter boarding point: ")
#     destination_point = input("Enter destination point: ")
#     if boarding_point in boarding_points and destination_point in destination_points:
#         check_availability()
#         seat = input("Enter seat no: ")
#         if seat in seats and seats[seat] is None:
#             # assign seat to user
#             seats[seat] = {"name": name, "age": age, "boarding_point": boarding_point, "destination_point": destination_point}
#             print("Seat booked successfully!")
#         else:
#             # add user to waiting list
#             waiting_list.append({"name": name, "age": age, "boarding_point": boarding_point, "destination_point": destination_point})
#             print("Seat not available. Added to waiting list.")


def book_seat():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    boarding_point = input("Enter boarding point: ")
    destination_point = input("Enter destination point: ")
    if boarding_point in boarding_points and destination_point in destination_points:
        check_availability()
        seat = input("Enter seat no: ")
        if seat in seats and seats[seat] is None:
            # get user's arrival time
            arrival_time = input("Enter arrival time (format: dd/mm/yyyy hh:mm:ss): ")
            arrival_time = datetime.strptime(arrival_time, "%d/%m/%Y %H:%M:%S")
            # assign seat to user with arrival and departure time
            seats[seat] = {"name": name, "age": age, "boarding_point": boarding_point, "destination_point": destination_point,
                           "arrival_time": arrival_time, "departure_time": None}
            print("Seat booked successfully!")
        else:
            # add user to waiting list with arrival time
            arrival_time = input("Enter arrival time (format: dd/mm/yyyy hh:mm:ss): ")
            arrival_time = datetime.strptime(arrival_time, "%d/%m/%Y %H:%M:%S")
            waiting_list.append({"name": name, "age": age, "boarding_point": boarding_point, "destination_point": destination_point,
                                  "arrival_time": arrival_time})
            print("Seat not available. Added to waiting list.")
# show booking history
def booking_history():
    for seat, user in seats.items():
        if user is not None:
            print(f"Seat {seat}: {user['name']} ({user['age']}), {user['boarding_point']} to {user['destination_point']},{user['arrival_time']}")
    for user in waiting_list:
        print(f"Waiting list: {user['name']} ({user['age']}), {user['boarding_point']} to {user['destination_point']}")

# cancel a seat

# def cancel_seat(username):
#     seat = input("Enter seat name to cancel: ")
#     if seat in seats and seats[seat] is not None:
#         if seats[seat]['name'] == username:
#             user = seats[seat]
#             seats[seat] = None
#             print(f"Seat {seat} cancelled.")
#             # if waiting list is not empty, assign seat to user with least arrival time
#             if waiting_list:
#                 waiting_list.sort(key=lambda x: x['arrival_time'])
#                 waiting_user = waiting_list.pop(0)
#                 seats[seat] = waiting_user
#                 print(f"Seat assigned to {waiting_user['name']}.")
#         else:
#             print(f"You do not have permission to cancel seat {seat}.")
#     else:
#         print("Invalid seat name.")

#  2nd --> def cancel_seat(username):
#     seat = input("Enter seat name to cancel: ")
#     if seat in seats and seats[seat] is not None:
#         if seats[seat]['name'] == username:
#             user = seats[seat]
#             seats[seat] = None
#             print(f"Seat {seat} cancelled.")
#             # if waiting list is not empty, assign seat to first user
#             if waiting_list:
#                 waiting_list.sort(key=lambda x: (x['arrival_time'], -boarding_points.index(x['boarding_point'])))
#                 waiting_user = waiting_list.pop(0)
#                 seats[seat] = waiting_user
#                 print(f"Seat assigned to {waiting_user['name']}.")
#         else:
#             print(f"You do not have permission to cancel seat {seat}.")
#     else:
#         print("Invalid seat name.")

def cancel_seat(username):
    seat = input("Enter seat name to cancel: ")
    if seat in seats and seats[seat] is not None:
        if seats[seat]['name'] == username:
            user = seats[seat]
            seats[seat] = None
            print(f"Seat {seat} cancelled.")
            # if waiting list is not empty, assign seat to first user
            if waiting_list:
                # sort waiting list by boarding point order and waiting time
                waiting_list.sort(key=lambda x: (boarding_points.index(x['boarding_point']), x['arrival_time']))
                waiting_user = waiting_list.pop(0)
                seats[seat] = waiting_user
                print(f"Seat assigned to {waiting_user['name']} "
                      f"who has been waiting for {waiting_user['arrival_time']} minutes.")
        else:
            print(f"You do not have permission to cancel seat {seat}.")
    else:
        print("Invalid seat name.")

# show waiting listn
def show_waiting_list():
    if waiting_list:
        print("Waiting list:")
        for user in waiting_list:
            print(f"{user['name']} ({user['age']}), {user['boarding_point']} to {user['destination_point']}")
    else:
        print("Waiting list is empty.")
def exit():
    authenticate()
# main function
def main():
    # authenticate user
    if not authenticate():
        return
    while True:
        print("1. Check seats availability")
        print("2. Book a seat")
        print("3. Booking history")
        print("4. Cancel a seat")
        print("5. Show waiting list")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            check_availability()
        elif choice == "2":
            book_seat()
        elif choice == "3":
            booking_history()
        elif choice == "4":
            cancel_seat(username)
        elif choice == "5":
            show_waiting_list()
        elif choice == "6":
            exit()
        else:
            print("Invalid choice. Please try again.")
main()
