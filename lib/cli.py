
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
            list_genres()
        elif choice == "2":
            find_genre_by_name()
        elif choice == "3":
            find_genre_by_id()
        elif choice == "4":
            create_genre()
        elif choice == "5":
            update_genre()
        elif choice == "6":
            delete_genre()
        elif choice == "7":
            list_books()
        elif choice == "8":
            find_book_by_name()
        elif choice == "9":
            find_book_by_id()
        elif choice == "10":
            create_book()
        elif choice == "11":
            update_book()
        elif choice == "12":
            delete_book()
        elif choice == "13":
            list_books_in_genre()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all genres")
    print("2. Find genre by name")
    print("3. Find genre by id")
    print("4: Create genre")
    print("5: Update genre")
    print("6: Delete genre")
    print("7. List all books")
    print("8. Find book by name")
    print("9. Find book by id")
    print("10: Create book")
    print("11: Update book")
    print("12: Delete book")
    print("13: List all books in a genre")


if __name__ == "__main__":
    main()
