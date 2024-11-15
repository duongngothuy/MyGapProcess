class Library:
    # def __init__(self, title, author, ISBN, publication_year, is_available):
    #     self.title = title
    #     self.author = author
    #     self.ISBN = ISBN
    #     self.publication_year = publication_year
    #     self.is_available = is_available
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_books(self, book):
        self.books.append(book)  
        print(f"Book '{book.title}' added to the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' with '{member.member_id}' added to Library. ")

    def display_available_books(self):
        available_books = [book for book in self.books if book.is_available]
        # any non-empty list is considered truthy (evaluates to True), and an empty list is considered falsy (evaluates to False)
        if available_books: 
            print("Available books in the library which are: ")
            for book in available_books:
                book.display_info()
        else: 
            print("No books available")
    
    def borrow_books(self,member, book):
        if book in self.books and self.members: 
            if book.is_available: 
                member.borrow_book(book)
                print(f"'{book.title}' borrowed by '{member.name}'.")
            else: 
                print(f"'{book.title}' is currently unavailable.")
        else:
            print("Invalid member or book.")
    
    def return_books(self,member, book):
        if book in self.books and self.members: 
            if book.is_available: 
                member.return_book()
                print(f"'{book.title}' returned by '{member.name}'.")    
            else: 
                print(f"'{book.title}' is not borrowed yet.")        
        else:
            print("Invalid member or book.")
    
    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]
        if results: 
            print(f"Search results for '{query}':")
            for book in results:
                book.display_info()
        else: 
            print(f"No books found for '{query}'.")


    class Book:
        #new_info = Library(title, author, ISBN, publication_year, is_available)
        def __init__(self, title, author, ISBN, publication_year, is_available = True):
            self.title = title
            self.author = author
            self.ISBN = ISBN
            self.publication_year = publication_year
            self.is_available = is_available
        def display_info(self):
            print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Public Year: {self.publication_year}, Stock: {self.is_available}")
        
        def markas_borrowed(self):
            self.is_available = False
        
        def markas_returned(self):
            self.is_available = True 
        
    
    class Member:
        def __init__(self, name, member_id): 
            #Books_borrowed list is used within the class 
            #so we dont have to recreate the list when giving new member object 
            self.name = name 
            self.member_id = member_id
            self.books_borrowed = []
        def borrow_book(self, book):
            if book.is_available == True:
                self.books_borrowed.append(book)
                book.markas_borrowed()
                print("It is borrowed")
        def return_book(self, book):
            if book in self.books_borrowed:
                self.books_borrowed.remove(book)
                book.markas_returned()
                print("It is returned")
        def display_borrowed_books(self, book):
            for each_book in self.books_borrowed:
                each_book.display_info()
    

library = Library()

book1 = library.Book("The Long Ships", "Frans G. Bengtsson", "978-1590173466", 1954 )
member1 = library.Member("Duong Ngo", "1234")

book2 = library.Book("1984", "George Orwell", "9780451524935", 1949 )
member2 = library.Member("Thanh Luong", "3456")

book3 =  library.Book("To Kill a Mockingbird", "Harper Lee", "9780446310789", 1960)
member3 = library.Member("Tram Ngo", "6789")



library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

library.register_member(member1)
library.register_member(member2)
library.register_member(member3)

library.display_available_books()
library.borrow_books(member1, book1)
library.display_available_books()
library.return_books(member1, book1)
library.search_books("1984")







                


        



