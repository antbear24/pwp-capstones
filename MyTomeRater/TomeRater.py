class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print(self.name + ", your email address has been updated")

    def __repr__(self):
        return "User " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_sum = 0
        for rating in self.books.values():
            if rating == None:
                rating_sum += 0
            else:
                rating_sum += rating
        return rating_sum / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("Updated ISBN to {}".format(new_isbn))

    def add_rating(self, rating):
        if rating == None:
            self.ratings.append(rating)
        elif rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.name == other_book.name and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        rating_sum = 0
        for rating in self.ratings:
            if rating == None:
                rating_sum += 0
            else:
                rating_sum += rating
        return rating_sum / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books.keys():
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}".format(email))

    def add_user(self, name, email, user_books=None):
        if self.valid_email(email) == True and email not in self.users:
            self.users[email] = User(name, email)
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        elif self.valid_email(email) != True:
            print("No valid email.")
        else:
            print("A user with that email already exists.")

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        times_read = 0
        most_read = ""
        for book, read_count in self.books.items():
            if read_count > times_read:
                times_read = read_count
                most_read = book
            else:
                continue
        return most_read

    def highest_rated_book(self):
        highest_rating = 0
        top_rated = ""
        for book in self.books.keys():
            if book.get_average_rating() > highest_rating:
                highest_rating  = book.get_average_rating()
                top_rated = book
            else:
                continue
        return top_rated


    def most_positive_user(self):
        avg_rate = 0
        pos_user = ""
        for user in self.users.values():
            if user.get_average_rating() > avg_rate:
                avg_rate = user.get_average_rating()
                pos_user = user
            else:
                continue
        return pos_user

    def valid_email(self, email):
        if "@" in email:
            if ".com" in email or ".edu" in email or ".org" in email:
                return True
            else:
                return False
        else:
            return False
