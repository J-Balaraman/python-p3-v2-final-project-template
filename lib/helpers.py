from models.genre import Genre
from models.book import Book


def exit_program():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(f"{genre.name}")


def find_genre_by_name():
    while True:
        name = input("Enter the genre's name: ")
        if name.strip():
            break
        else:
            print("Invalid input. Please enter a non-empty genre name.")

    genre = Genre.find_by_name(name)
    print(f"{genre.name}") if genre else print(f'Genre {name} not found')


def find_genre_by_id():
    while True:
        try:
            id_ = int(input("Enter the genre's id: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for genre ID.")

    genre = Genre.find_by_id(id_)
    print(f"{genre.name}") if genre else print(f'Genre {id_} not found')


def create_genre():
    while True:
        try:
            name = input("Enter the genre's name: ")
            if name.strip():
                genre = Genre.create(name)
                print(f'Success: {f"Genre: {genre.name}"}')
                break
            else:
                print("Invalid input. Please enter a non-empty genre name.")
        except Exception as exc:
            print("Error creating genre: ", exc)



def update_genre():
    while True:
        try:
            name_ = input("Enter the genre's name: ")
            if genre := Genre.find_by_name(name_):
                try:
                    name = input("Enter the genre's new name: ")
                    genre.name = name
                    
                    genre.update()
                    print(f'Success: {f"Genre: {genre.name}"}')
                except Exception as exc:
                    print("Error updating genre: ", exc)
            else:
                print(f'Genre {name_} not found')
            break
        except ValueError:
            print("Invalid input. Please enter the genre's name")


def delete_genre():
    while True:
        try:
            name_ = input("Enter the genre's name: ")
            if genre := Genre.find_by_name(name_):
                genre.delete()
                print(f'Genre {name_} deleted')
            else:
                print(f'Genre {name_} not found')
            break
        except ValueError:
            print("Invalid input. Please enter the genre's name")

def list_books():
    books = Book.get_all()
    for book in books:
        print(f"{book.name}, {book.author}, Genre #{book.genre_id}")

def find_book_by_name():
    while True:
        try:
            name = input("Enter the book's name: ")
            if name.strip():
                book = Book.find_by_name(name)
                print(f"{book.name}, {book.author}, Genre #{book.genre_id}") if book else print(
                    f'Book {name} not found')
                break
        except ValueError:
            print("Invalid input. Please enter a non empty book name")


def find_book_by_id():
    while True:
        try:
            id_ = int(input("Enter the book's id: "))
            book = Book.find_by_id(id_)
            print(f"Book #{book.id}: {book.name}, {book.author}, Genre #{book.genre_id}") if book else print(f'Book {id_} not found')
            break
        except ValueError:
            print("Invalid input. Please enter an integer")

def create_book():
    while True:
        try:
            name = input("Enter the book's name: ")
            author = input("Enter the book's author: ")
            genre_id = int(input("Enter the book's genre id: "))
            if name.strip() and author.strip():
                try:
                    book = Book.create(name, author, genre_id)
                    print(f'Success: {f"{book.name}, {book.author}, Genre #{book.genre_id}"}')
                except Exception as exc:
                    print("Error creating book: ", exc)
                break
        except ValueError:
            print("There has been a problem with the provided data. Please re-enter it into the proper fields, ensuring that the book title and author fields have content other then whitespace in them, and that the genre id is an integer.")


def update_book():
    while True:
        try:
            name_ = input("Enter the book's name: ")
            if book := Book.find_by_name(name_):
                try:
                    name = input("Enter the book's new name: ")
                    book.name = name
                    author = input("Enter the book's new author: ")
                    book.author = author
                    genre_id = input("Enter the book's new genre id: ")
                    book.genre_id = genre_id
        
                    book.update()
                    print(f'Success: {f"{book.name}, {book.author}, Genre #{book.genre_id}"}')
                except Exception as exc:
                    print("Error updating book: ", exc)
            else:
                print(f'Book {name_} not found')
            break
        except ValueError:
            print("Invalid input. Please enter the book's name")

def delete_book():
    while True:
        try:
            name_ = input("Enter the book's name: ")
            if book := Book.find_by_name(name_):
                book.delete()
                print(f'book {name_} deleted')
            else:
                print(f'book {name_} not found')
            break
        except ValueError:
            print("Invalid input. Please enter the book's name")