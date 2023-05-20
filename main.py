# Data Management Project by Ibrahim Ismayilov

# Base Project Single User

# Arrays to store data in
books = []
shopping_cart = []


# Function to add a new set of data for a specific book
def new_book(title, ISBN, genre, author):
    return {"title": title, "ISBN": ISBN, "genre": genre, "author": author}


# Few random sets of data about specific books
books.append(new_book("It", 9783453435773, "Horror", "Stephen King"))
books.append(
    new_book("War and Peace", 9788412664812, "Historical Fiction", "Leo Tolstoy")
)
books.append(
    new_book(
        "The Catcher in the Rye", 9783462015393, "Young Adult Fiction", "J. D. Salinger"
    )
)


# Array to store user info for login
users = []


# Add new user info for login
def newUser(username, password):
    return {"username": username, "password": password, "favs": []}


loop = True
# Menu loop
while loop:
    # Print main menu
    print("\n1. Display All Data")
    print("2. Spell Check a Word (Binary Search)")
    print("3. Spell Check Alice in Wonderland (Linear Search)")
    print("3. Spell Check Alice in Wonderland (Binary Search)")
    print("4. Spell Check Alice in Wonderland (Binary Search)")
    print("5. Exit")

    # Get menu selection from the user
    selection = input("Enter Menu Selection (1-5): ")

    #   Take action based on menu selection
    #   Option 1
    if selection == "1":
        # Display all data
        # Iterate over all key/value pairs in the dictionaries and printing them appropriately
        for book in books:
            print("\n" + book["title"])
            print(book["ISBN"])
            print(book["genre"])
            print(book["author"])


# When displaying the arrays, can I do it more efficiently through the use of print key, value pairs?
