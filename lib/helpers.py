from models.genre import Genre
from models.book import Book


def exit_program():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)


def find_genre_by_name():
    name = input("Enter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(
        f'Genre {name} not found')


def find_genre_by_id():
    id_ = input("Enter the genre's id: ")
    genre = Genre.find_by_id(id_)
    print(genre) if genre else print(f'Genre {id_} not found')


def create_genre():
    name = input("Enter the genre's name: ")
    try:
        genre = Genre.create(name)
        print(f'Success: {genre}')
    except Exception as exc:
        print("Error creating genre: ", exc)


def update_genre():
    id_ = input("Enter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        try:
            name = input("Enter the genre's new name: ")
            genre.name = name
            
            genre.update()
            print(f'Success: {genre}')
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print(f'Genre {id_} not found')


def delete_genre():
    id_ = input("Enter the genre's id: ")
    if genre := Genre.find_by_id(id_):
        genre.delete()
        print(f'Genre {id_} deleted')
    else:
        print(f'Genre {id_} not found')

def list_books():
    books = Book.get_all()
    for book in books:
        print(book)

def find_book_by_name():
    name = input("Enter the book's name: ")
    book = Book.find_by_name(name)
    print(book) if book else print(
        f'Book {name} not found')


def find_book_by_id():
    id_ = input("Enter the book's id: ")
    book = Book.find_by_id(id_)
    print(book) if book else print(f'Book {id_} not found')


def create_book():
    name = input("Enter the book's name: ")
    author = input("Enter the book's author: ")
    genre_id = input("Enter the book's genre id: ")
    try:
        book = Book.create(name, author, genre_id)
        print(f'Success: {book}')
    except Exception as exc:
        print("Error creating book: ", exc)


def update_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        try:
            name = input("Enter the book's new name: ")
            book.name = name
            author = input("Enter the book's new author:")
            book.author = author
            genre_id = input("Enter the book's new genre id: ")
            book.genre_id = genre_id

            book.update()
            print(f'Success: {book}')
        except Exception as exc:
            print("Error updating book: ", exc)
    else:
        print(f'Book {id_} not found')


def delete_book():
    id_ = input("Enter the book's id: ")
    if book := Book.find_by_id(id_):
        book.delete()
        print(f'book {id_} deleted')
    else:
        print(f'book {id_} not found')


def list_books_in_genre():
    id_ = input("Enter the genre's id: ")
    books = Book.get_all()
    if genre := Genre.find_by_id(id_):
        for book in books:
            if book.genre_id == genre.id:
                print(book)
    else:
        print('Invalid Genre Id')