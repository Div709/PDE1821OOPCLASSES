class Book:
    def __init__(self, title, author,copies,borrowed):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = borrowed
    def available_copies(self):
        available = self.copies - self.borrowed
        return available
    def borrow_book(self,n):
        if (self.copies > 0):
            self.borrowed = self.copies - 1
            return self.borrowed
        else:
            print("Sorry, you cannot borrow more books.")
    def return_book(self):
        self.copies = self.copies + 1
        self.borrowed = self.borrowed - 1
        return self.borrowed,self.copies
    def display_book(self,n):
        self.n = n
        for i in n:
            print(f"Name of book is {self.title}")
            print(f"Author name is {self.author}")
            print(f"Copies available: {self.copies}.")
            print(f"Borrowed amount: {self.borrowed}.")

book = []
book_amount = int(input("Enter book amount: "))
i = 0
if book_amount > 3:
    while i < book_amount:
        i +=1
        book_name = input("Enter book name: ")
        book_author = input("Enter book author: ")
        book_copies = int(input("Enter amount of book copies: "))
        book_borrowed = int(input("Enter amount of book borrowed : "))
        book.append(Book(book_name,book_author,book_amount,book_amount))
    user_input = input("Input 1 to display books, 2 to borrow a book, 3 to return a book or 4 to exit: ")
    if user_input == 1:
        book.display_book(book)
else:
    print("Enter a bigger amount of books.")



