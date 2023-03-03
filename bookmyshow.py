# Define global variables to store data
users = []
theater = []
movies = []
showtimes = []
bookings = []
admin_users=[]
# User module

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
def add_theater():
    theater_name = input("Enter theater name: ")
    theater_location = input("Enter theater location: ")
    theater_capacity = int(input("Enter theater capacity: "))
    theater.append({'name': theater_name, 'location': theater_location, 'capacity': theater_capacity})
    print("Theater added successfully.")

def show_theaters():
    if len(theater) == 0:
        print("There are no theaters currently.")
    else:
        print("Theaters:")
        for i in range(len(theater)):
            print(f"{i+1}. {theater[i]['name']} - {theater[i]['location']} ({theater[i]['capacity']} seats)")

def add_showtime():
    # Display list of theaters to choose from
    print("Choose a theater to add showtimes:")
    for i in range(len(theater)):
        print(f"{i+1}. {theater[i]['name']} - {theater[i]['location']}")
    
    # Prompt user to enter valid theater number
    while True:
        try:
            theater_index = int(input("Enter theater number: ")) - 1
            if theater_index < 0 or theater_index >= len(theater):
                raise ValueError
            break
        except ValueError:
            print("Invalid theater number. Please enter a valid number.")
    
    # Prompt user to input showtime details
    movie_name = input("Enter movie name: ")
    showtime = input("Enter showtime (HH:MM AM/PM): ")
    
    # Create dictionary with showtime details and append to theater's showtimes list
    showtime_dict = {'movie': movie_name, 'showtime': showtime}
    theater[theater_index].setdefault('showtimes', []).append(showtime_dict)
    
    print("Showtime added successfully.")
def show_showtimes():
    if len(theater) == 0:
        print("There are no theaters currently.")
    else:
        print("Showtimes:")
        for i in range(len(theater)):
            if 'showtimes' in theater[i]:
                print(f"{theater[i]['name']} ({theater[i]['location']}):")
                for showtime in theater[i]['showtimes']:
                    print(f"- {showtime['movie']} at {showtime['showtime']}")

def book_seat():
    # Display list of theaters to choose from
    print("Choose a theater to book seats:")
    for i in range(len(theater)):
        print(f"{i+1}. {theater[i]['name']} - {theater[i]['location']}")
    
    # Prompt user to enter valid theater number
    while True:
        try:
            theater_index = int(input("Enter theater number: ")) - 1
            if theater_index < 0 or theater_index >= len(theater):
                raise ValueError
            break
        except ValueError:
            print("Invalid theater number. Please enter a valid number.")
    
    # Check if theater has any showtimes scheduled
    if 'showtimes' not in theater[theater_index]:
        print("There are no showtimes scheduled for this theater.")
        return
    
    # Display list of showtimes to choose from
    print("Choose a showtime to book seats:")
    for i, showtime in enumerate(theater[theater_index]['showtimes']):
        print(f"{i+1}. {showtime['movie']} at {showtime['showtime']}")
    
    # Prompt user to enter valid showtime number
    while True:
        try:
            showtime_index = int(input("Enter showtime number: ")) - 1
            if showtime_index < 0 or showtime_index >= len(theater[theater_index]['showtimes']):
                raise ValueError
            break
        except ValueError:
            print("Invalid showtime number. Please enter a valid number.")
    
    # Prompt user to enter number of seats to book
    while True:
        try:
            num_seats = int(input("Enter number of seats to book: "))
            if num_seats <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid number of seats. Please enter a positive integer.")
    
    # Check if there are enough seats available
    capacity = theater[theater_index]['capacity']
    booked_seats = len(theater[theater_index]['showtimes'][showtime_index].get('booked_seats', []))
    remaining_seats = capacity - booked_seats
    if num_seats > remaining_seats:
        print(f"Sorry, there are only {remaining_seats} seats remaining for this showtime.")
        return
    print("The seat arrangements\n  1 2 3 4 5 6 7 8 9 10\n 11 12 13 14 15 16 17 18 19 20")
    # Prompt user to enter seat numbers to book
    booked_seat_numbers = []
    for i in range(num_seats):
        while True:
            try:
                seat_number = int(input(f"Enter seat number {i+1}: "))
                if seat_number < 1 or seat_number > capacity:
                    raise ValueError
                if seat_number in booked_seat_numbers:
                    print("Seat number already booked. Please choose a different seat.")
                else:
                    booked_seat_numbers.append(seat_number)
                    break
            except ValueError:
                print("Invalid seat number. Please enter a valid number.")
    
    # Add booked seats to showtime's booked seats list
    theater[theater_index]['showtimes'][showtime_index].setdefault('booked_seats', []).extend(booked_seat_numbers)
    
    # Print confirmation message
    print(f"{num_seats} seats booked successfully for {theater[theater_index]['showtimes'][showtime_index]['movie']} at {theater[theater_index]['showtimes'][showtime_index]['showtime']} in {theater[theater_index]['name']}.")
def get_ticket():
    # Display list of theaters to choose from
    print("Choose a theater to view booked seats:")
    for i in range(len(theater)):
        print(f"{i+1}. {theater[i]['name']} - {theater[i]['location']}")
    
    # Prompt user to enter valid theater number
    while True:
        try:
            theater_index = int(input("Enter theater number: ")) - 1
            if theater_index < 0 or theater_index >= len(theater):
                raise ValueError
            break
        except ValueError:
            print("Invalid theater number. Please enter a valid number.")
    
    # Check if theater has any showtimes scheduled
    if 'showtimes' not in theater[theater_index]:
        print("There are no showtimes scheduled for this theater.")
        return
    
    # Display list of showtimes to choose from
    print("Choose a showtime to view booked seats:")
    for i, showtime in enumerate(theater[theater_index]['showtimes']):
        print(f"{i+1}. {showtime['movie']} at {showtime['showtime']}")
    
    # Prompt user to enter valid showtime number
    while True:
        try:
            showtime_index = int(input("Enter showtime number: ")) - 1
            if showtime_index < 0 or showtime_index >= len(theater[theater_index]['showtimes']):
                raise ValueError
            break
        except ValueError:
            print("Invalid showtime number. Please enter a valid number.")
    
    # Print ticket information
    movie = theater[theater_index]['showtimes'][showtime_index]['movie']
    showtime = theater[theater_index]['showtimes'][showtime_index]['showtime']
    theater_name = theater[theater_index]['name']
    theater_location = theater[theater_index]['location']
    booked_seats = theater[theater_index]['showtimes'][showtime_index].get('booked_seats', [])
    
    print(f"\n---- TICKET ----")
    print(f"Movie: {movie}")
    print(f"Showtime: {showtime}")
    print(f"Theater: {theater_name} - {theater_location}")
    print(f"Seats: {', '.join(str(seat) for seat in booked_seats)}")
    print(f"---------------\n")
def cancel_tickets():
    # Display list of theaters to choose from
    print("Choose a theater to cancel booked seats:")
    for i in range(len(theater)):
        print(f"{i+1}. {theater[i]['name']} - {theater[i]['location']}")
    
    # Prompt user to enter valid theater number
    while True:
        try:
            theater_index = int(input("Enter theater number: ")) - 1
            if theater_index < 0 or theater_index >= len(theater):
                raise ValueError
            break
        except ValueError:
            print("Invalid theater number. Please enter a valid number.")
    
    # Check if theater has any showtimes scheduled
    if 'showtimes' not in theater[theater_index]:
        print("There are no showtimes scheduled for this theater.")
        return
    
    # Display list of showtimes to choose from
    print("Choose a showtime to cancel booked seats:")
    for i, showtime in enumerate(theater[theater_index]['showtimes']):
        print(f"{i+1}. {showtime['movie']} at {showtime['showtime']}")
    
    # Prompt user to enter valid showtime number
    while True:
        try:
            showtime_index = int(input("Enter showtime number: ")) - 1
            if showtime_index < 0 or showtime_index >= len(theater[theater_index]['showtimes']):
                raise ValueError
            break
        except ValueError:
            print("Invalid showtime number. Please enter a valid number.")
    
    # Check if there are any booked seats for the showtime
    if 'booked_seats' not in theater[theater_index]['showtimes'][showtime_index]:
        print("There are no booked seats for this showtime.")
        return
    
    # Display list of booked seats to choose from
    booked_seats = theater[theater_index]['showtimes'][showtime_index]['booked_seats']
    print("Choose a seat number to cancel:")
    for i, seat in enumerate(booked_seats):
        print(f"{i+1}. Seat {seat}")
    
    # Prompt user to enter valid seat number
    while True:
        try:
            seat_index = int(input("Enter seat number: ")) - 1
            if seat_index < 0 or seat_index >= len(booked_seats):
                raise ValueError
            break
        except ValueError:
            print("Invalid seat number. Please enter a valid number.")
    
    # Cancel the selected seat
    canceled_seat = booked_seats.pop(seat_index)
    print(f"Seat {canceled_seat} has been canceled.")
    print("Your payment rufunded")

# Main program
def usermodule():
    print("Welcome to Book My Show!")
    while True:
        print("1. Sign up")
        print("2. Login")
        print("3. Show theaters")
        print("4. Show showtimes")
        print("5. Book a seat")
        print("6. get a ticket")
        print("7. Cancel a seat")
        print("8. Exit")
        choice = input("Enter choice number: ")
        if choice == "1":
            signup()
        elif choice == "2":
            login()
        elif choice == "3":
            show_theaters()
        elif choice == "4":
            show_showtimes()
        elif choice =='5':
            book_seat()
        elif choice =='6':
            get_ticket()
        elif choice =='7':
            cancel_tickets()
        elif choice == '8':
            print("Thank you for using Book My Show!")
            main()
        else:
            print("Invalid choice")


def admin_module():
    while True:
        print("1. Add theaters")
        print("2. Add showtimes")
        print("3. show showtimes")
        print("4. Show theater")
        print("5. Exit")
        choice = input("Enter choice number: ")
        if choice == "1":
            add_theater()
        elif choice == "2":
            add_showtime()
        elif choice == "3":
            show_showtimes()
        elif choice == "4":
            show_theaters()
            print("--------")
        elif choice == "5":
            print("Thank you for using Book My Show!")
            main()
        else:
            print("Invalid choice")
current_user_id = None

def main():
    global usage
    usage = str(input("Enter you are admin or user:"))
    if(usage=='user'):
        usermodule()
    elif(usage=='admin'):

        name=str(input("Enter the admin name : "))
        adpassword=str(input("Enter the admin password : "))
        if name == "admin" and adpassword == "1234":
            print("Admin authenticated successfully!")
            admin_module()
        else:
            print("Invalid username or password. Please try again.")
    else:
        print("Invalid usage")
main()

