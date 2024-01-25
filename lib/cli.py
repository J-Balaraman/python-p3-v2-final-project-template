
from helpers import (
    exit_program,
    list_genres,
    find_genre_by_name,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    find_book_by_name,
    create_book,
    update_book,
    delete_book
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            genre_path()
        elif choice == "2":
            book_path()


def menu():
    print("===============================")
    print("Please select an option:")
    print("To access/change genres, type 1")
    print("To access/change books, type 2")
    print("To exit the program, type 0")
    print("===============================")

def genre_path():
    list_genres()
    print("===============================")
    print("What would you like to do?")
    print("0. Exit the program")
    print("1. Find genre by name")
    print("2: Create genre")
    print("3: Update genre")
    print("4: Delete genre")
    print("5: Go Back")
    print("===============================")
    genre_input = input("> ")
    if genre_input == "0":
        exit_program()
    elif genre_input == "1":
        find_genre_by_name()
    elif genre_input == "2":
        create_genre()
    elif genre_input == "3":
        update_genre()
    elif genre_input == "4":
        delete_genre()
    elif genre_input == '5':
        pass
    else:
        print("Please enter a valid number")

def book_path():
    list_books()
    print("===============================")
    print("What would you like to do?")
    print("0. Exit the program")
    print("1. Find a book by name")
    print("2: Create a book")
    print("3: Update a book")
    print("4: Delete a book")
    print("5: Go Back")
    print("===============================")
    book_input = input("> ")
    if book_input == "0":
        exit_program()
    elif book_input == "1":
        find_book_by_name()
    elif book_input == "2":
        create_book()
    elif book_input == "3":
        update_book()
    elif book_input == "4":
        delete_book()
    elif book_input == "5":
        pass
    else:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
