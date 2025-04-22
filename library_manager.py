import json
import os

def load_library():
    if os.path.exists("library.txt"):
        try:
            with open("library.txt", "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading library file: {e}. Starting with empty library.")
            return []
    return []

def save_library(library):
    try:
        with open("library.txt", "w") as file:
            json.dump(library, file, indent=4)
        print("Library saved to file.")
    except IOError as e:
        print(f"Error saving library file: {e}")

def add_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author: ").strip()
    while True:
        try:
            year_input = input("Enter the publication year: ").strip()
            year = int(year_input)
            if year > 0:
                break
            print("Please enter a valid year.")
        except ValueError:
            print("Please enter a valid integer for the year.")
    genre = input("Enter the genre: ").strip()
    while True:
        read_status = input("Have you read this book? (yes/no): ").lower().strip()
        if read_status in ["yes", "no"]:
            break
        print("Please enter 'yes' or 'no'.")
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status == "yes"
    }
    library.append(book)
    print("Book added successfully!")
    save_library(library)

def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip()
    for book in library[:]:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            save_library(library)
            return
    print("Book not found.")

def search_book(library):
    print("Search by:")
    print("1. Title")
    print("2. Author")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        title = input("Enter the title: ").strip()
        matches = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ").strip()
        matches = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("Invalid choice.")
        return
    if matches:
        print("Matching Books:")
        for i, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_books(library):
    if not library:
        print("Your library is empty.")
        return
    print("Your Library:")
    for i, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics(library):
    total_books = len(library)
    if total_books == 0:
        print("Your library is empty.")
        return
    read_books = sum(1 for book in library if book["read"])
    percentage_read = (read_books / total_books) * 100
    print(f"Total books: {total_books}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main():
    library = load_library()
    while True:
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()