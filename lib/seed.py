from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.book import Book

def seed_database():
    Book.drop_table()
    Genre.drop_table()
    Genre.create_table()
    Book.create_table()

    fantasy = Genre.create("Fantasy")
    non_fiction = Genre.create("Non-Fiction")
    realistic_fiction = Genre.create("Realistic Fiction")
    Book.create("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", fantasy.id)
    Book.create("The Giving Tree", "Shel Silverstein", fantasy.id)
    Book.create("Percy Jackson and The Lightning Thief", "Rick Riordan", fantasy.id)
    Book.create("The Immortal Life of Henrietta Lacks", "Rebecca Skloot", non_fiction.id)
    Book.create("The Warmth of Other Suns", "Isabel Wilkerson", non_fiction.id)
    Book.create("The 7 Habits of Highly Effective People", "Stephen Covey", non_fiction.id)


seed_database()
print("Seeded database")