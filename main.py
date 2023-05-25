# Data Management Project by Ibrahim Ismayilov


# Base Project Single User


# Importing JSON Module for Advanced Login Program
import json


# Array to Store Book Data
books = []


# Function to Add a New Set of Data for a New Book
def new_book(title, publisher, genre, author):
    return {"title": title, "publisher": publisher, "genre": genre, "author": author}


# Few Random Sets of Data About Specific Books
books.append(new_book("It", "Viking", "Horror", "Stephen King"))
books.append(
    new_book(
        "War and Peace", "The Russian Messenger", "Historical Fiction", "Leo Tolstoy"
    )
)
books.append(
    new_book(
        "The Catcher in the Rye",
        "Little, Brown",
        "Young Adult Fiction",
        "J. D. Salinger",
    )
)
books.append(
    new_book("The A.B.C Murders", "Collins Crime Club", "Mystery", "Agatha Christie")
)
books.append(new_book("Animal Farm", "Secker and Warburg", "Fable", "George Orwell"))
books.append(
    new_book(
        "Harry Potter and the Sorcerer's Stone",
        "Scholastic Corporation",
        "Fantasy",
        "J. K. Rowling",
    )
)
books.append(
    new_book("Lord of the Flies", "Faber and Faber", "Novel", "William Golding")
)


# Function to Print the Dictionaries in the Books in Organized Fashion
def display_data(anArray):
    for book in anArray:
        print("\n" + book["title"])
        print(book["publisher"])
        print(book["genre"])
        print(book["author"])


# Insertion Sort for Option 3 in Main Menu
def insertionSort(anArray):
    for i in range(1, len(anArray)):
        # Save the insert value
        insertVal = anArray[i]
        # Save the insert position
        insertPos = i
        # Modify the insert position and overwrite it if it does not belong
        while insertPos > 0 and insertVal["title"] < anArray[insertPos - 1]["title"]:
            anArray[insertPos] = anArray[insertPos - 1]
            insertPos -= 1
        # Insert the value in its proper position and overwrite the duplicate if there was any change in the positions
        anArray[insertPos] = insertVal
    return anArray


# Linear Search To Find Specific Data
def linear_search(anArray, key, value):
    for i in range(len(anArray)):
        if anArray[i][key].lower() == value.lower():
            return i
    return -1


def main_menu(users, user):
    loop = True
    while loop:
        # Print Main Menu
        print("\nMain Menu")
        print("1. Display All Data")
        print("2. Filter Data (Title, Publisher, Genre, Author)")
        print("3. Sort Data by Book Title")
        print("4. Select Book to Add to Shopping Cart")
        print("5. Select Book to Remove from Shopping Cart")
        print("6. Display Shopping Cart")
        print("7. Log Out and Exit Program")

        # Get Menu Selection From the User
        selection = input("Enter Menu Selection (1-5): ")

        # Take Action Based on Menu Selection
        # Option 1
        if selection == "1":
            # Display the Properties of All Dictionaries in Organized Fashion
            display_data(books)

        # Option 2
        elif selection == "2":
            # Filter by Either Title, Publisher, Genre, or Author
            print("\nFilter by Either Title, Publisher, Genre, or Author")
            # Get User Input on How They Would Like to Filteri
            filter_input = input(
                "Which filter would you like to use? (Title, Publisher, Genre, Author): "
            )

            # Get User Input for What to Filter
            data_input = input("What would you like to filter for?: ")

            # Run Filter Program Based on The User Inputs
            results = linear_search(books, filter_input, data_input)

            # If The Filter Did Not Find What The User Requested
            if results == -1:
                print(
                    f"Unfortunately no matches were found of {data_input} when filtering for {filter_input}."
                )
            # If The Filter Did Find Data the User Requested
            else:
                print("")
                for x in books[results]:
                    print(books[results][x])

        # Option 3
        elif selection == "3":
            # Sort and Display Data Based on Title of the Books
            print("\nSort the Books by Title")
            books_copy = insertionSort(books.copy())
            display_data(books_copy)

        # Option 4
        elif selection == "4":
            # Add a Book To User's Shopping Cart
            # Get User Input on Which Book to Add
            user_input = input(
                "\nWhich book would you like to add to your shopping cart? "
            )
            results = linear_search(books, "title", user_input)
            # If the My Program Does Not Have the Book
            if results == -1:
                print(
                    "\nUnfortunately we do not have that book right now and cannot add it to your shopping cart."
                )
            else:
                # If My Program Does Have Such a Book
                # Add Book from Their Shopping Cart
                user["shopping_cart"].append(books[results])
                # Save User Shopping Cart Preferences
                save_users(users)
                print("\n" + f"{user_input} was added to your cart.")

        # Option 5
        elif selection == "5":
            # Get User Input on Which Book to Remove
            user_input = input(
                "\nWhich book would you like to remove from your shopping cart? "
            )
            results = linear_search(user["shopping_cart"], "title", user_input)
            # If the User Does Not Have the Book
            if results == -1:
                print("\nYou do not have that book in your shopping cart.")
            else:
                # If the User Has the Book in Shopping Cart
                # Remove Book from Their Shopping Cart
                user["shopping_cart"].pop(results)
                # Save User Shopping Cart Preferences
                save_users(users)
                print("\n" + f"{user_input} was removed from your cart.")

        # Option 6
        elif selection == "6":
            # Display Set of Data About Books in Their Shopping Cart
            display_data(user["shopping_cart"])

        # Option 7
        elif selection == "7":
            # Exit Program and Log Out
            print("\nExit Program")
            return -1


# Function to Create New User with Their Specific Set of Data
def create_new_user(username, password):
    return {"username": username, "password": password, "shopping_cart": []}


# Function to Load Array in the JSON File to a Local Array in login_page()
def load_users():
    with open("users.json", "r") as file_ref:
        return json.load(file_ref)


# Function to Save Users in the Array Created in login_page() to the JSON file
def save_users(users):
    # Open a file and use json.dump to write data to file as JSON
    with open("users.json", "w") as file_ref:
        json.dump(users, file_ref)


# Login Page User Must Proceed Through in order to Access Menu
def login_page():
    users = load_users()
    loop = True
    while loop:
        print("\nAdvanced Login Program")
        print("A. Press A to Log In: ")
        print("B. Press B to Register: ")
        user_input = input("Please proceed by picking a letter: ")
        if user_input.lower() == "a":
            print("\nLogin Page")
            username = input("Username: ")
            password = input("Password: ")
            check_user(users, username, password)
        elif user_input.lower() == "b":
            print("\nRegistration")
            username = input("New Username: ")
            password = input("New Password: ")
            conf_password = input("Confirm Password: ")
            register_user(users, username, password, conf_password)


# Check User Function to Check User Username and Password When Logging In
def check_user(users, username, password):
    search_result = linear_search(users, "username", username)
    if search_result == -1:
        print("The username is not in our system.")
    else:
        if users[search_result]["password"] == password:
            print("You are now logged in! Enjoy your stay")
            main_menu(users, users[search_result])
        else:
            print("Wrong Password!")


# Register User Function to Create New Set of Data for New User If They Provide Correct Inputs
def register_user(users, username, password, conf_password):
    search_result = linear_search(users, "username", username)
    if search_result == -1:
        if password == conf_password:
            new_user = create_new_user(username, password)
            users.append(new_user)
            save_users(users)
            main_menu(users, new_user)
        else:
            print("The passwords do not match.")
    else:
        print("The username is already in our system. You must pick a new username.")


# Starting The Login Page and the Program
login_page()
