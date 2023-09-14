from datetime import datetime
import time


class Book:
    def __init__(self, isbn, title, author, yearofpublication, publisher, imageurl_s, imageurl_m, imageurl_l):
        self.imageurl_l = imageurl_l
        self.imageurl_m = imageurl_m
        self.imageurl_s = imageurl_s
        self.yearofpublication = yearofpublication
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.ratingslist = []


class Bookrating:
    def __init__(self, isbn, rating, serial_no):
        self.isbn = isbn
        self.rating = rating
        self.serial_no = serial_no


class user:
    def __init__(self, serial_no, adress, area_code):
        self.adress = adress
        self.area_code = area_code
        self.serial_no = serial_no
        self.bookissued = {}
        self.dateissued = {}

    def issue_book(self, isbn, issuedate, serial_no):
        if serial_no in self.bookissued:
            # Key exists, append the new value to the list
            self.bookissued[serial_no].append(isbn)
        else:
            # Key doesn't exist, create a new key-value pair with the key and a list containing the new value
            self.bookissued[serial_no] = [isbn]
        if isbn not in self.dateissued:
            self.dateissued[isbn] = [issuedate]
        print(self.bookissued)
        print(self.dateissued)

    def return_books(self, isbn, serial_no):
        print("book returning start...")
        self.bookissued[serial_no].remove(isbn)
        del self.dateissued[isbn]
        print(self.bookissued)
        print(self.dateissued)
        print("book returning..... end")


class Case_study_methods:

    def __init__(self):
        self.books = {}
        self.ratings = {}
        self.users = {}

    def add_book(self, isbn, title, author, year_of_publication, publisher, image_url_s, image_url_m, image_url_l):
        # storig the book object with isbn as primary key
        self.books[isbn] = Book(isbn, title, author, year_of_publication, publisher, image_url_s, image_url_m,
                                image_url_l)

    def display_book_title(self, isbn):
        if isbn in self.books:
            return self.books[isbn].title
        else:
            return "isbn not present"

    def del_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            return "Deleted sucessfully"
        else:
            return "Book not found"

    def update_bookname(self, isbn, new_title):
        if isbn in self.books:
            oldtitle = self.books[isbn].title
            self.books[isbn].title = new_title
            return f"sucessflly update the book title from {oldtitle} to {new_title}"
        else:
            return "book not found for update"

    def check_title(self, title_to_check):
        for i in self.books:
            if self.books[i].title == title_to_check:
                return f"yes the title is present in isbn {self.books[i]}"
        return "title not present"

    def check_isbn(self, isbn):
        # Check availability of a book by ISBN
        if isbn in self.books:
            return "isbn is present"
        else:
            return "isbn is not present"

    def add_user(self, serial_no, adress, area_code):
        if serial_no not in self.users:
            self.users[serial_no] = user(serial_no, adress, area_code)
            return "user added sucessfully"
        else:
            return f"user already exist with serial number {serial_no}"

    def change_user(self, serial_no, adress, area_code):
        if serial_no in self.users:
            self.users[serial_no].adress = adress
            self.users[serial_no].area_code = area_code
            return "user has changed sucessfully"
        else:
            return "user not found"

    def display_user(self, serial_no):
        if serial_no in self.users:
            i = self.users[serial_no]
            print(i.serial_no, i.adress, i.area_code)
        else:
            print("serial no is not valid")

    def issue(self, isbn, serial_no, issuedate):
        if isbn in self.books and serial_no in self.users:
            if isbn not in self.users[serial_no].bookissued:
                self.users[serial_no].issue_book(isbn, issuedate, serial_no)
                return "Booked issue sucessfully"
            else:
                return "book is already issued"
        else:
            return "isbn or serial no is not present in the data base or not found"

    def return_book(self, isbn, serial_no, date_of_return):
        if isbn in self.books and serial_no in self.users:
            if isbn in self.users[serial_no].bookissued[serial_no]:
                dt1 = self.users[serial_no].dateissued[isbn][0]
                print(dt1)
                dt2 = date_of_return
                print(dt2)
                date_format = "%d/%m/%Y"
                a = time.mktime(time.strptime(dt1, date_format))
                b = time.mktime(time.strptime(dt2, date_format))
                delta = b - a
                date_difference = int(delta / 86400)
                self.users[serial_no].return_books(isbn, serial_no)
                if date_difference > 7:
                    fine_amount = date_difference * 10
                    return f"the fine amount of book returned for late of {date_difference} days is {fine_amount}"
                else:
                    return "book returned sucessfully  with our fine"
            else:
                return f"this book is not issued for this {isbn}"

        else:
            return "isbn or serial no not found please issue this book then return"

    def add_rating(self, isbn, rating, serial_no):
        self.ratings[isbn] = Bookrating(isbn, rating, serial_no)
        return "Thansks for rating , your rating has been added sucessfully"

    def display(self):
        for isbn, book in self.books.items():
            print(f"ISBN: {isbn}, Title: {book.title}, Area Code: {book.area_code}")

    def average_rating_per_publisher(self):
        # first will create a dictionry wher key will be publisher which isbn has got rating and value as list where for that oublisher
        # has got all the rating
        publisher_ratings = {}  # Dictionary to store publisher ratings
        # Iterate through the ratings to gather data
        for isbn in self.ratings:
            if self.books[isbn].publisher not in publisher_ratings:
                publisher_ratings[self.books[isbn].publisher] = [self.ratings[isbn].rating]
            else:
                publisher_ratings[self.books[isbn].publisher].append(self.ratings[isbn].rating)
            print(publisher_ratings)

    def total_books_per_year(self, year):
        totalbooks = 0
        for isbn in self.books:
            if self.books[isbn].yearofpublication == year:
                totalbooks += 1

    def top_five(self):
        ratinglist = []
        # display the top five book with rating as a parameter
        for isbn in self.ratings:
            ratinglist.append(self.ratings[isbn].rating)

        # Sort the list in ascending order
        sorted_list = sorted(ratinglist)

        # Get the top 5 elements
        top_5_elements = sorted_list[-5:]
        return top_5_elements


library = Case_study_methods()
library.add_book("9780451524935", "To Kill a Mockingbird", "Harper Lee", 1960, "Harper Perennial Modern Classics",
                 "image_url_s_1", "image_url_m_1", "image_url_l_1")
library.add_book("9780743273565", "The Great Gatsby", "F. Scott Fitzgerald", 1925, "Scribner",
                 "image_url_s_2", "image_url_m_2", "image_url_l_2")
library.add_book("9781984855147", "1984", "George Orwell", 1949, "Signet Classic",
                 "image_url_s_3", "image_url_m_3", "image_url_l_3")
library.add_book("9780061120084", "To Kill a Mockingbird", "Harper Lee", 1960, "Harper Perennial Modern Classics",
                 "image_url_s_4", "image_url_m_4", "image_url_l_4")
library.add_book("9780143127550", "The Catcher in the Rye", "J.D. Salinger", 1951, "Back Bay Books",
                 "image_url_s_5", "image_url_m_5", "image_url_l_5")
library.add_book("9781451673319", "The Hobbit", "J.R.R. Tolkien", 1937, "Mariner Books",
                 "image_url_s_6", "image_url_m_6", "image_url_l_6")
library.add_book("9780061120085", "Brave New World", "Aldous Huxley", 1932, "Harper Perennial",
                 "image_url_s_7", "image_url_m_7", "image_url_l_7")
library.add_book("9780061120086", "The Lord of the Rings", "J.R.R. Tolkien", 1954, "Mariner Books",
                 "image_url_s_8", "image_url_m_8", "image_url_l_8")
library.add_book("9781451673318", "Pride and Prejudice", "Jane Austen", 1813, "Penguin Classics",
                 "image_url_s_9", "image_url_m_9", "image_url_l_9")
library.add_book("9780451526342", "Animal Farm", "George Orwell", 1945, "Signet Classic",
                 "image_url_s_10", "image_url_m_10", "image_url_l_10")

# will use check isbn to check weather the add book is pressent or not

print(library.check_isbn("9780451526342"))

# check te del book fuction will first delete a book then we check with check isbn methode

print(library.del_book("9780451526342"))

print(library.check_isbn("9780451526342"))

# will check the update function where will use display titile methode to check weather the book name is changed or not
print(library.display_book_title("9780061120086"))

print(library.update_bookname("9780061120086", 'the lord of kings'))

print(library.display_book_title("9780061120086"))

print(library.check_isbn("2243423423"))
print(library.check_isbn("9781984855147"))

print(library.add_user(1, "bhanjanagr", 201))
print(library.add_user(2, "bellaguntha", 202))
print(library.add_user(3, "bengaluru", 304))
print(library.add_user(4, "delhi", 207))
print(library.add_user(5,"chennai",701))
print(library.add_user(6,"mumbai",508))
print(library.add_user(7,"bhubaneswar",706))

library.display_user(2)
print(library.change_user(2, "hyderadbad", 208))
library.display_user(2)

print(library.issue("9780451524935", 1, "11/9/2023"))
print(library.issue("9780743273565", 2, "25/09/2023"))
print(library.issue("9780061120085", 1, "10/10/2023"))

print(library.return_book("9780743273565", 2, "10/10/2023"))

print(library.add_rating("9780143127550","7.5",1))
print(library.add_rating("9780143127550","8.9",3))
print(library.add_rating("9780143127550","7.8",4))
print(library.add_rating("9780061120085","5.5",5))
print(library.add_rating("9780061120085","6.5",6))
print(library.add_rating("9780061120085","5.9",3))
print(library.add_rating("9780743273565","5.5",2))
print(library.add_rating("9780743273565","5.3",5))
print(library.add_rating("9780743273565","5.2",6))

library.average_rating_per_publisher()
print(library.top_five())


