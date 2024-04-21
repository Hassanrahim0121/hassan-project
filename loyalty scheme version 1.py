import sqlite3
import datetime
from tkinter import *
from tkinter import messagebox, simpledialog

def database():
    forename = forename_entry.get()
    surname = surname_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    connection = sqlite3.connect('Riget Zoo Adventures.db')
    information_table = '''CREATE TABLE IF NOT EXISTS User_information (forename TEXT, surname TEXT, email TEXT, password TEXT)'''
    connection.execute(information_table)

    adding_into_table = '''INSERT INTO User_information (forename, surname, email, password) VALUES (?, ?, ?, ?)'''
    data = (forename, surname, email, password)

    storing = connection.cursor()
    storing.execute(adding_into_table, data)
    
    connection.commit()
    connection.close
    messagebox.showinfo("success","you have signed up")
    hotel_booking_page()

def signup_page():
    global forename_entry, surname_entry, email_entry, password_entry
    signup_window = Toplevel(root)
    signup_window.title("Riget Zoo Adventures Sign Up Form")

    signup_window.geometry("500x500")
    signup_label = Label(signup_window, text="Sign Up", font=("Oswald", 15, "bold"))
    signup_label.grid(row=1, column=0, sticky=W)

    forename_label = Label(signup_window, text="Enter your Forename", font=("Oswald", 12, "bold"))
    forename_label.grid(row=2, column=0, sticky=W)
    forename_entry = Entry(signup_window, width=30)
    forename_entry.grid(row=3, column=0, sticky=W)

    surname_label = Label(signup_window, text="Enter your Surname", font=("Oswald", 12, "bold"))
    surname_label.grid(row=4, column=0, sticky=W)
    surname_entry = Entry(signup_window, width=30)
    surname_entry.grid(row=5, column=0, sticky=W)

    email_label = Label(signup_window, text="Enter your Email", font=("Oswald", 12, "bold"))
    email_label.grid(row=6, column=0, sticky=W)
    email_entry = Entry(signup_window, width=30)
    email_entry.grid(row=7, column=0, sticky=W)

    password_label = Label(signup_window, text="Enter your Password", font=("Oswald", 12, "bold"))
    password_label.grid(row=8, column=0, sticky=W)
    password_entry = Entry(signup_window, width=30)
    password_entry.grid(row=9, column=0, sticky=W)

    submit_button = Button(signup_window, text="Submit", font=("Oswald", 12, "bold"), command=database)
    submit_button.grid(row=10, column=0, sticky=W)

def login_page():
    global login_email_entry, login_password_entry
    login_window = Toplevel(root)
    login_window.title("Riget Zoo Adventures Login Form")
    login_window.geometry("500x500")
    login_label = Label(login_window, text="Login", font=("Oswald", 15, "bold"))
    login_label.grid(row=1, column=0, sticky=W)

    email_label = Label(login_window, text="Enter your Email", font=("Oswald", 12, "bold"))
    email_label.grid(row=2, column=0, sticky=W)
    login_email_entry = Entry(login_window, width=30)
    login_email_entry.grid(row=3, column=0, sticky=W)

    password_label = Label(login_window, text="Enter your Password", font=("Oswald", 12, "bold"))
    password_label.grid(row=4, column=0, sticky=W)
    login_password_entry = Entry(login_window, width=30, show="*")
    login_password_entry.grid(row=5, column=0, sticky=W)

    login_button = Button(login_window, text="login", font=("Oswald", 12, "bold"), command=login_check)
    login_button.grid(row=6, column=0, sticky=W)

def login_check():
    email = login_email_entry.get()
    password = login_password_entry.get()
    connection = sqlite3.connect('Riget Zoo Adventures.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM  User_information WHERE email=? AND password=?''', (email, password))
    check = cursor.fetchone()
    if check:
        messagebox.showinfo("Success", "You have successfully logged in")
        zoo_booking_page()
    else:
        messagebox.showerror("Error", "The email or password is incorrect")
    connection.commit()
    connection.close()

def homepage():
    homepage_window=Toplevel(root)
    homepage_window.title("Riget Zoo Adventures")
    homepage_window.geometry("1000x1000")

    nav_bar = Menu(homepage_window)
    first_menu = Menu(nav_bar, tearoff=0)
    first_menu.add_command(label="Zoo",command=zoo_page)
    nav_bar.add_cascade(label="Zoo", menu=first_menu)

    second_menu = Menu(nav_bar, tearoff=0)
    second_menu.add_command(label="Hotel", command=hotel_page)
    nav_bar.add_cascade(label="Hotel", menu=second_menu)

    third_menu = Menu(nav_bar, tearoff=0)
    third_menu.add_command(label="Education", command=education_page)
    nav_bar.add_cascade(label="Education", menu=third_menu)

    homepage_window.config(menu=nav_bar)

    logo = PhotoImage(file="images/logo.gif")
    logo_label = Label(homepage_window, image=logo)
    logo.image=logo
    logo_label.grid(row=1, columnspan=3, sticky=W)

    home_image = PhotoImage(file="H:/Task 2/Riget Zoo Adventures/home_page_images/tiger.gif")
    home_image_label = Label(homepage_window, image=home_image)
    home_image.image = home_image
    home_image_label.grid(row=2, columnspan=3, sticky=W)

    welcome_label= Label(homepage_window, text="WELCOME TO RIGET ZOO ADVENTURES", font=("Oswald", 16, "bold"))
    welcome_label.grid(row=5, column=0, sticky=W)

    # Adding the paragraph
    paragraph_text = "Riget Zoo Adventures is a safari style zoo that looks after endangered animals.\nWe have facilities that treat animals if they are sick, allow visits to pet and feed animals.\nWe have various attractions like a 4D Cinema and swimming with dolphins.\nWe offer a 5-star hotel that directly connects with the zoo.\nWe offer hotel packages with breakfast included."
    paragraph_label = Label(homepage_window, text=paragraph_text, font=("Oswald", 12))
    paragraph_label.grid(row=6, column=0, columnspan=3, sticky=W, padx=10, pady=10)

    zoo_tickets_button = Button(homepage_window, text="Zoo Tickets", font=("Oswald", 14, "bold"), bg="#ce7a11", command=zoo_booking_page)
    zoo_tickets_button.grid(row=7, column=0, sticky=W)

    hotel_booking_button = Button(homepage_window, text="Hotel Booking", font=("Oswald", 14, "bold"), bg="#30d5c8", command=hotel_booking_page)
    hotel_booking_button.grid(row=7, column=3, sticky=W)

def zoo_booking_page():
    global customer_email_entry, child_ticket_entry, adult_ticket_entry
    zoo_booking_window = Toplevel(root)
    zoo_booking_window.title("Booking zoo tickets")
    zoo_booking_window.geometry("500x500")

    email_label = Label(zoo_booking_window, text="Please Enter your email.", font=("Oswald", 14, "bold"))
    email_label.grid(row=1, column=0, sticky=W)
    customer_email_entry = Entry(zoo_booking_window, width=20)
    customer_email_entry.grid(row=2, column=0, sticky=W)
    child_ticket_label = Label(zoo_booking_window, text="Please Enter the amount of children\nPlease enter a number.", font=("Oswald", 14, "bold"))
    child_ticket_label.grid(row=3, column=0, sticky=W)
    child_ticket_entry = Entry(zoo_booking_window, width=20)
    child_ticket_entry.grid(row=4, column=0, sticky=W)
    adult_ticket_label = Label(zoo_booking_window, text="Please Enter the amount of adults\nPlease enter a number.", font=("Oswald", 14, "bold"))
    adult_ticket_label.grid(row=5, column=0, sticky=W)
    adult_ticket_entry = Entry(zoo_booking_window, width=20)
    adult_ticket_entry.grid(row=6, column=0, sticky=W)
    book_button = Button(zoo_booking_window, text="Book", font=("Oswald", 14, "bold"), command=tickets_booked)
    book_button.grid(row=7, column= 0, sticky=W)

def tickets_booked():
    email = customer_email_entry.get()
    child_ticket = child_ticket_entry.get()
    adult_ticket = adult_ticket_entry.get()

    connection = sqlite3.connect('Riget Zoo Adventures.db')
    information_table = '''CREATE TABLE IF NOT EXISTS Zoo_Booking (email TEXT, child_ticket INTEGER, adult_ticket INTEGER)'''
    connection.execute(information_table)

    adding_into_table = '''INSERT INTO Zoo_Booking (email, child_ticket, adult_ticket) VALUES (?, ?, ?)'''
    data = (email, child_ticket, adult_ticket)

    storing = connection.cursor()
    storing.execute(adding_into_table, data)

    connection.commit()
    connection.close()
    zoo_tickets_payment()

def zoo_tickets_payment():
    connection = sqlite3.connect('Riget Zoo Adventures.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Zoo_Booking ORDER BY ROWID DESC LIMIT 1''')
    booking_info = cursor.fetchone()
    connection.close()

    if booking_info:
        total_price = (int(booking_info[1]) * 10) + (int(booking_info[2]) * 20)

        payment_window = Toplevel(root)
        payment_window.title("Zoo Tickets Payment")
        payment_window.geometry("500x500")

        total_price_label = Label(payment_window, text=f"Total Price: ${total_price}", font=("Oswald", 12))
        total_price_label.pack()

        card_number = simpledialog.askstring("Card Details", "Enter Card Number:")
        if card_number is None:
            messagebox.showinfo("Payment Status", "Payment Cancelled")
            payment_window.destroy()
            return

        expiration_date = simpledialog.askstring("Card Details", "Enter Expiration Date (MM/YYYY):")
        cvv = simpledialog.askstring("Card Details", "Enter CVV:")

        messagebox.showinfo("Payment Status", f"You have paid ${total_price}.")
        payment_window.destroy()

        zoo_tickets_receipt(root, total_price)  # Call zoo_tickets_receipt with total_price after payment
    else:
        messagebox.showerror("Error", "No booking information found.")

def zoo_tickets_receipt(root, total_price):
    points = 20
    # Fetch data from the database to display in the receipt
    connection = sqlite3.connect('Riget Zoo Adventures.db')
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM Zoo_Booking ORDER BY ROWID DESC LIMIT 1''')  # Get the latest booking
    booking_info = cursor.fetchone()
    connection.close()

    if booking_info:
        # Create the receipt message
        receipt_message = "Zoo Tickets Receipt\n\n"
        receipt_message += f"Email: {booking_info[0]}\n"
        if len(booking_info) >= 4:  # Ensure there are enough elements in the tuple
            receipt_message += f"Child Tickets: {booking_info[1]}\n"
        if len(booking_info) >= 5:  # Ensure there are enough elements in the tuple
            receipt_message += f"Adult Tickets: {booking_info[2]}\n"
        receipt_message += f"Total Price: ${total_price}\n"
        receipt_message += f"Points Earned: {points}\n"

        # Show the receipt message in a messagebox
        messagebox.showinfo("Zoo Tickets Receipt", receipt_message)
    else:
        messagebox.showerror("Error", "No booking information found.")
    
def storing_hotel_book():
    email = email_entry.get()
    checkin_date = start_date.get()
    check_out_date = end_date.get()
    num_of_rooms = int(num_rooms.get())
    num_of_days = int(num_days.get())

    connection = sqlite3.connect('Riget Zoo Adventures.db')
    booking_table = '''CREATE TABLE IF NOT EXISTS Booking_hotel (email TEXT, check_in_date TEXT, check_out_date TEXT, number_of_room INTEGER, number_of_days INTEGER)'''
    connection.execute(booking_table)

    adding_to_table = '''INSERT INTO Booking_hotel (email, check_in_date, check_out_date, number_of_room, number_of_days) VALUES (?, ?, ?, ?, ?)'''
    information = (email, checkin_date, check_out_date, num_of_rooms, num_of_days)
    store = connection.cursor()
    store.execute(adding_to_table, information)
    connection.commit()
    connection.close()
    hotel_payments(num_of_rooms, num_of_days)

def hotel_payments(num_of_rooms, num_of_days):
    total_price = (num_of_days * 50) + (num_of_rooms * 100)
    card_details = get_card_details()
    if card_details:
        print_receipt(total_price)

def get_card_details():
    card_number = simpledialog.askstring("Card Payment", "Enter Card Number:")
    exp_date = simpledialog.askstring("Card Payment", "Enter Expiration Date (MM/YY):")
    cvv = simpledialog.askstring("Card Payment", "Enter CVV:")
    return card_number, exp_date, cvv

def print_receipt(total_price):
    points = 20
    receipt = f"Riget Zoo Adventures Hotel Receipt\n\n"
    receipt += f"Booking Details:\n"
    receipt += f"Email: {email_entry.get()}\n"
    receipt += f"Check-in Date: {start_date.get()}\n"
    receipt += f"Check-out Date: {end_date.get()}\n"
    receipt += f"Number of Rooms: {num_rooms.get()}\n"
    receipt += f"Number of Days: {num_days.get()}\n\n"
    receipt += f"Total Paid: ${total_price}\n"
    receipt += f"Points Earned: {points}\n"

    messagebox.showinfo("Riget Zoo Adventure Receipt", receipt)


def hotel_booking_page():
    global email_entry, end_date, start_date, num_rooms, num_days
    hotel_booking = Toplevel(root)
    email_label = Label(hotel_booking, text="Enter the email")
    email_label.grid(row=1, column=0, sticky=W)
    email_entry = Entry(hotel_booking, width=30)
    email_entry.grid(row=2, column=0, sticky=W)
    check_in_date_label = Label(hotel_booking, text="Check-in date")
    check_in_date_label.grid(row=3, column=0, sticky=W)
    start_date = Entry(hotel_booking, width=30)
    start_date.grid(row=4, column=0, sticky=W)
    check_out_date_label = Label(hotel_booking, text="Check-out date")
    check_out_date_label.grid(row=5, column=0, sticky=W)
    end_date = Entry(hotel_booking, width=30)
    end_date.grid(row=6, column=0, sticky=W)
    num_room_label = Label(hotel_booking, text="Enter number of rooms")
    num_room_label.grid(row=7, column=0, sticky=W)
    num_rooms = Entry(hotel_booking, width=30)
    num_rooms.grid(row=8, column=0, sticky=W)
    num_days_label = Label(hotel_booking, text="Enter number of days")
    num_days_label.grid(row=9, column=0, sticky=W)
    num_days = Entry(hotel_booking, width=30)
    num_days.grid(row=10, column=0, sticky=W)
    submit = Button(hotel_booking, text="Book Hotel", command=storing_hotel_book)
    submit.grid(row=11, column=0, sticky=W)



root = Tk()
root.title("Riget Zoo Adventures")
root.geometry("500x500")

welcome_label = Label(root, text="Welcome to Riget Zoo Adventures", font=("Oswald", 15, "bold"))
welcome_label.grid(row=1, column=0, sticky=W)
choice_label = Label(root, text="Please choose an option", font=("Oswald", 15, "bold"))
choice_label.grid(row=2, column=0, sticky=W)
signup_button = Button(root, text="Sign up", font=("Oswald", 14, "bold"), width=6, command=signup_page)
signup_button.grid(row=3, column=0, sticky=W)
login_button = Button(root, text="Login", font=("Oswald", 14, "bold"), width=6, command=login_page)
login_button.grid(row=4, column=0, sticky=W)
root.mainloop()
