import mysql.connector
import random

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="9009-Ocean!",
            database="Skillmate",
            auth_plugin='mysql_native_password'
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def login(cursor):
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    query = "SELECT * FROM User WHERE Email = %s AND PasswordHash = %s"
    cursor.execute(query, (email, password))
    result = cursor.fetchone()

    if result:
        print(f"Welcome, {result['FirstName']} {result['LastName']}!")
        return True
    else:
        print("Invalid credentials. Please try again.")
        return False

def print_user_info(user):
    print(f"\nUser Information:")
    print(f"Name: {user['FirstName']} {user['LastName']}")
    print(f"Gender: {user['Gender']}")
    print(f"Email: {user['Email']}")
    print(f"Phone Number: {user['PhoneNumber']}")
    print(f"Bio: {user['Bio']}")
    print(f"Date of Birth: {user['DateOfBirth']}")

def get_random_user(cursor):
    query = "SELECT * FROM User ORDER BY RAND() LIMIT 1"
    cursor.execute(query)
    return cursor.fetchone()

def filter_users(cursor, job_title=None, skill_name=None, education_degree=None, location_city=None):
    query = "SELECT * FROM User"

    if job_title:
        query += f" INNER JOIN WorkExperience ON User.UserID = WorkExperience.UserID WHERE JobTitle = '{job_title}'"

    if skill_name:
        query += f" INNER JOIN Skill ON User.UserID = Skill.UserID WHERE SkillName = '{skill_name}'"

    if education_degree:
        query += f" INNER JOIN Education ON User.UserID = Education.UserID WHERE Degree = '{education_degree}'"

    if location_city:
        query += f" INNER JOIN Location ON User.UserID = Location.UserID WHERE City = '{location_city}'"

    cursor.execute(query)
    return cursor.fetchall()

def main_menu():
    print("Welcome to the User Filtering System!")
    print("1. Log in")
    print("2. Exit")

def user_menu():
    print("\nUser Menu:")
    print("1. Show me a random user")
    print("2. Filter users")
    print("3. Log out")

def main():
    while True:
        main_menu()
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            # Log in
            conn = connect_to_database()
            if conn:
                cursor = conn.cursor(dictionary=True)
                
                while True:
                    if login(cursor):
                        while True:
                            user_menu()
                            user_choice = input("Enter your choice (1-3): ")

                            if user_choice == '1':
                                # Show random user
                                random_user = get_random_user(cursor)
                                print_user_info(random_user)
                            
                            elif user_choice == '2':
                                # Filter users
                                job_title = input("Enter job title to filter by (or press Enter to skip): ")
                                skill_name = input("Enter skill name to filter by (or press Enter to skip): ")
                                education_degree = input("Enter education degree to filter by (or press Enter to skip): ")
                                location_city = input("Enter location city to filter by (or press Enter to skip): ")

                                filtered_users = filter_users(cursor, job_title, skill_name, education_degree, location_city)
                                for user in filtered_users:
                                    print_user_info(user)

                            elif user_choice == '3':
                                # Log out
                                conn.close()
                                print("Logged out successfully!\n")
                                break

                            else:
                                print("Invalid choice. Please enter a valid option.")
                        break

        elif choice == '2':
            # Exit
            print("Exiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
