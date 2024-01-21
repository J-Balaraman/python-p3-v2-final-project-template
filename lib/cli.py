
from helpers import (
    exit_program,
    list_genres,
    find_genre_by_name,
    find_genre_by_id,
    create_genre,
    update_genre,
    delete_genre,
    list_books,
    find_book_by_name,
    find_book_by_id,
    create_book,
    update_book,
    delete_book,
    list_books_in_genre
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
    print("2. Find genre by id")
    print("3: Create genre")
    print("4: Update genre")
    print("5: Delete genre")
    print("6: Go Back")
    print("===============================")
    genre_input = input("> ")
    if genre_input == "0":
        exit_program()
    elif genre_input == "1":
        find_genre_by_name()
    elif genre_input == "2":
        find_genre_by_id()
    elif genre_input == "3":
        create_genre()
    elif genre_input == "4":
        update_genre()
    elif genre_input == "5":
        delete_genre()
    elif genre_input == '6':
        pass
    else:
        print("Please enter a valid number")

def book_path():
    list_books()
    print("===============================")
    print("What would you like to do?")
    print("0. Exit the program")
    print("1. Find a book by name")
    print("2. Find a book by id")
    print("3: Create a book")
    print("4: Update a book")
    print("5: Delete a book")
    print("6: Go Back")
    print("===============================")
    book_input = input("> ")
    if book_input == "0":
        exit_program()
    elif book_input == "1":
        find_book_by_name()
    elif book_input == "2":
        find_book_by_id()
    elif book_input == "3":
        create_book()
    elif book_input == "4":
        update_book()
    elif book_input == "5":
        delete_book()
    elif book_input == "6":
        pass
    else:
        print("Please enter a valid number")


if __name__ == "__main__":
    main()
