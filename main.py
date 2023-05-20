# Data Management Project by Ibrahim Ismayilov


# Base Project Single User


# Arrays to Store Data In
books = []
shopping_cart = []


# Function to Add a New Set of Data for a Specific Book
def new_book(title, ISBN, genre, author):
    return {"title": title, "ISBN": ISBN, "genre": genre, "author": author}


# Few Random Sets of Data About Specific Books
books.append(new_book("It", 9783453435773, "Horror", "Stephen King"))
books.append(new_book("War", 9788412664812, "Historical Fiction", "Leo Tolstoy"))
books.append(
    new_book(
        "The Catcher in the Rye", 9783462015393, "Young Adult Fiction", "J. D. Salinger"
    )
)
books.append(new_book("The A.B.C Murders", 9781405033633, "Mystery", "Agatha Christie"))
books.append(new_book("Animal Farm", 9788896675434, "Fable", "George Orwell"))


# Array to Store User Info for Login
users = []


# Add New User Info for Login
def newUser(username, password):
    return {"username": username, "password": password, "favs": []}


# Function to Print the Dictionaries in the Books in Organized Fashion
def display_data(anArray):
    for book in anArray:
        print("\n" + book["title"])
        print(book["ISBN"])
        print(book["genre"])
        print(book["author"])


# Linear Search To Find Specific Data
def linear_search(anArray, key, value):
    for i in range(len(anArray)):
        if anArray[i][key] == value:
            return i
    return -1


# Insertion Sort for Option 3
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

    # Function to Filter for a Book by Title
    # def filter_title(filter_title):
    #     for book in books:
    #         if book["title"].lower() == filter_title.lower():
    #             print("1")
    #             print("\n" + book["title"])
    #             print(book["ISBN"])
    #             print(book["genre"])
    #             print(book["author"])
    #     else:
    #         return -1

    # Function to Filter for a Book by ISBN
    # def filter_ISBN(filter_ISBN):
    #     for book in books:
    #         if book["ISBN"] == str(filter_ISBN):
    #             print("\n" + book["title"])
    #             print(book["ISBN"])
    #             print(book["genre"])
    #             print(book["author"])
    #     else:
    #         return -1

    # # Function to Filter for a Book by Genre
    # def filter_genre(filter_genre):
    #     for book in books:
    #         if book["genre"].lower() == filter_genre.lower():
    #             print("\n" + book["title"])
    #             print(book["ISBN"])
    #             print(book["genre"])
    #             print(book["author"])
    #     else:
    #         return -1

    # # Function to Filter for a Book by Author
    # def filter_author(filter_author):
    #     for book in books:
    #         if book["author"] == filter_author:
    #             print("\n" + book["title"])
    #             print(book["ISBN"])
    #             print(book["genre"])
    #             print(book["author"])
    else:
        return -1


def filter(filter_input, data_input):
    filter_input.lower()
    for book in books:
        if book[f"{filter_input}"].lower() == data_input.lower():
            return book
    else:
        return -1


# Function to Determine Which How the User Wants to Filter Data
# def filter_type(user_input, user_input2):
#     if filter_input.lower() == "title":
#         filter_title(user_input2)
#     elif user_input.lower() == "isbn":
#         filter_ISBN(user_input2)
#     elif user_input.lower() == "genre":
#         filter_genre(user_input2)
#     elif user_input.lower() == "author":
#         filter_author(user_input2)


def main_menu(user):
    # Print Main Menu
    print("\nMain Menu")
    print("1. Display All Data")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice in Wonderland (Linear Search)")
    print("3. Spell Check Alice in Wonderland (Binary Search)")
    print("4. Spell Check Alice in Wonderland (Binary Search)")
    print("5. Exit")

    # Get Menu Selection From the User
    selection = input("Enter Menu Selection (1-5): ")

    #   Take Action Based on Menu Selection
    #   Option 1
    if selection == "1":
        # Display the Properties of All Dictionaries in Organized Fashion
        display_data(books)

    # Option 2
    elif selection == "2":
        # Filter by Either Title, ISBN, Genre, or Author
        # Get User Input on What They Want to Filter for
        filter_input = input(
            "Which filter would you like to use? (Title, ISBN, Genre, Author): "
        )

        data_input = input("What would you like to filter for?: ")

        # Run Filter Program Based on The User Inputs
        results = filter(filter_input, data_input)
        if results == -1:
            print(
                f"Unfortunately no matches were found of {data_input} when filtering for {filter_input}."
            )
        else:
            print("\n" + results["title"])
            print(results["ISBN"])
            print(results["genre"])
            print(results["author"])

        # Option 3
    elif selection == "3":
        # Sort Data Based on Title of the Books
        books_copy = books.copy()
        print(insertionSort(books_copy))

    # Option 4
    elif selection == "4":
        user_input = input("Which book would you like to add to your shopping cart? ")
        results = filter("title", user_input)
        if results == -1:
            print(
                "Unfortunately we do not have that book right now and cannot add it to your shopping cart."
            )
        else:
            shopping_cart.append(results)
            print(f"{user_input} was added to your cart.")

    # Option 4
    elif selection == "5":
        user_input = input(
            "Which book would you like to remove from your shopping cart? "
        )
        results = filter("title", user_input)
        if results == -1:
            print(
                "Unfortunately we do not have that book right now and cannot remove it from your shopping cart."
            )
        else:
            shopping_cart.pop(results)
            print(f"{user_input} was removed from your cart.")

    # Option 4
    elif selection == "6":
        display_data(shopping_cart)


# Login Advanced Part
def login_page(login_menu):
    users = load_users()
    loop = True
    while loop:
        user_input = login_menu
        if user_input == "1":
            print("\nRegistration Page")
            username = input("Username: ")
            password = input("Password: ")
            register(users, username, password)
        elif user_input == "2":
            print("\nLogin Page")
            username = input("Username: ")
            password = input("Password: ")
            verify_user(users, username, password)


def login_menu():
    print("\nAdvanced Login System")
    print("1. Press 1 to Log In: ")
    print("2. Press 2 to Register: ")
    user_input = input("Please proceed by picking a number: ")
    return user_input


def register(users, username, password):
    results == linear_search(users, username, "username")
    if results == -1:
        print("\nNew User Successfully Registered.")
        user = newUser(username, password)
        users.append(user)
        saveUser(users)
        main_menu(user)


def load_users():
    with open("users.json", "r") as file_ref:
        return json.load(file_ref)


def saveUser(users):
    with open("users.json", "w") as file_ref:
        json.dump(users, file_ref)


def verify_user(users, username, password):
    results = linear_search(users, username, "username")
    if results == -1:
        print("The username is not in our registry.")
    else:
        if users[results]["password"] == password:
            print("You are now logged in! Enjoy your stay.")
            menu(users(results))
        else:
            print("Your password is wrong. Try again.")


# Starting The Program with the Login Page
login_menu()

# When displaying the arrays, can I do it more efficiently through the use of printing key, value pairs for the dicts?
