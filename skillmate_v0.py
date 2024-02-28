import tkinter as tk
from tkinter import messagebox
import mysql.connector

#establish connection to sql database
#ensure credentials are correct
host = "localhost"
user = "root"
password = "CPSC408!"
database = "Skillmate"
conn = mysql.connector.connect(host=host, user=user, password=password, auth_plugin='mysql_native_password', database=database)
cursor = conn.cursor()

#login to website by checking db for existing matching username and password
#returns a -1 if no matching credentials are found
def login(email, password):
    # Use parameterized query to prevent SQL injection
    query = """
        SELECT COUNT(*)
        FROM User
        WHERE Email = %s AND PasswordHash = %s;
    """
    cursor.execute(query, (email, password))
    if cursor.fetchone()[0] == 0:
        return -1
    else:
        # if one is found pulls user_id and returns it
        query = """
            SELECT FirstName
            FROM User
            WHERE Email = %s AND PasswordHash = %s;
        """
        cursor.execute(query, (email, password))
        return cursor.fetchone()[0]

#create account function
def create_account(email, password, firstname, lastname):
    query = f"""
        INSERT INTO User (FirstName, LastName, Email, PasswordHash)
        VALUES ('{firstname}', '{lastname}', '{email}', '{password}');
    """
    cursor.execute(query)
    conn.commit()
    clear_frame()
    logged_in(firstname)

# Create the main window
parent = tk.Tk()
parent.title("Login Form")

#clears current frame of all items
def clear_frame():
    for widget in parent.winfo_children():
        widget.destroy()

def exit():
    parent.destroy()

def logged_in(name):
    #create label with name
    welcome_label = tk.Label(parent, text="Welcome, ", font=("Arial", 60))
    welcome_label.pack()

    name_label = tk.Label(parent, text=name,font=("Arial", 72))
    name_label.pack()

    #create a button to return to login page
    back_button = tk.Button(parent, text="Back", command=loginPage)
    back_button.pack()

    #create an exit button
    exit_button = tk.Button(parent, text="Exit", command=exit)
    exit_button.pack()

def signup_button_click(email, password):
    query = f"""
        SELECT COUNT(*)
        FROM User
        WHERE Email = %(email)s;"""
    cursor.execute(query, {'email' : email})
    if(cursor.fetchone()[0] != 0):
        #ensuring no repeat emails
        signup_display_label = tk.Label(parent, text="Email already has account",font=("Arial", 24))
        signup_display_label.pack()
    else:
        clear_frame()
        # Create and place the firstname label and entry
        firstname_label = tk.Label(parent, text="Firstname:")
        firstname_label.pack()

        firstname_entry = tk.Entry(parent,width=70,font=("Arial", 24))
        firstname_entry.pack()

        # Create and place the lastname label and entry
        lastname_label = tk.Label(parent, text="Lastname:")
        lastname_label.pack()

        lastname_entry = tk.Entry(parent, width=70,font=("Arial", 24))  # Show asterisks for password
        lastname_entry.pack()

        #create button for creating account
        create_account_button = tk.Button(parent,text="Create Account",command=lambda: create_account(email,password,firstname_entry.get(),lastname_entry.get()))
        create_account_button.pack()

def login_button_click(email, password):
        #gets nane from db
        name = login(email, password)

        #checks if person existed
        if name == -1:
            login_display_label = tk.Label(parent, text="Login Failed, User Not Found",font=("Arial", 24))
            login_display_label.pack()
        else:
            clear_frame()
            logged_in(name)



def loginPage():
    clear_frame()

    # Create and place the username label and entry
    username_label = tk.Label(parent, text="Email:")
    username_label.pack()

    username_entry = tk.Entry(parent,width=70,font=("Arial", 48))
    username_entry.pack()

    # Create and place the password label and entry
    password_label = tk.Label(parent, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(parent, show="*", width=70,font=("Arial", 48))  # Show asterisks for password
    password_entry.pack()

    # Create and place the login button
    login_button = tk.Button(parent, text="Login", command=lambda: login_button_click(username_entry.get(), password_entry.get()))
    login_button.pack()

    # Create and place the login button
    signup_button = tk.Button(parent, text="Sign Up", command=lambda: signup_button_click(username_entry.get(),password_entry.get()))
    signup_button.pack()

    #create an exit button
    exit_button = tk.Button(parent, text="Exit", command=exit)
    exit_button.pack()





width, height = parent.winfo_screenwidth(), parent.winfo_screenheight()

parent.geometry('%dx%d+0+0' % (width,height))


loginPage()
# Start the Tkinter event loop
parent.mainloop()
