class Book:
    def __init__(self,title,author,copies,borrowed):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = borrowed
    def available_copies(self):
        return self.copies - self.borrowed
    def return_book(self,n):
        self.borrowed = self.borrowed - n
        return self.borrowed
        print("Book returned successfully")
    def display_book(self):
        print(f"{self.title} - {self.author} - {self.copies} - {self.borrowed}")
    def borrow_book(self,n):
        if self.copies - self.borrowed >= 1:
            self.borrowed = self.borrowed + n
        print("Book borrowed successfully")
books = []
user_input = input("How many books you want to enter: ")
while int(user_input) > 0:
    if int(user_input) < 3:
        print("Please enter a number greater than 3")
    else:
        n = 0
        while n < int(user_input):
            name = str(input("Enter Book Title: "))
            writer= str(input("Enter Book Author: "))
            no_copies = int(input("Enter Book copies: "))
            no_borrowed = int(input("Enter Book borrowed: "))
            n = n + 1
            book_obj= Book(name,writer,no_copies,no_borrowed)
            books.append(book_obj)
    print(f"Enter 1 to Display Books")
    print(f"Enter 2 to Return Books")
    print(f"Enter 3 to Borrow Books")
    print(f"Enter 4 to End Program")
    menu = int(input("Enter your choice: "))
    while int(menu) > 0:
        if int(menu) == 1:
            for i in books:
                i.display_book()
        elif int(menu) == 2:
            book_index = int(input("Enter index of book: "))
            book_return_num = int(input("Enter the number of book you want to return: "))
            books[book_index].return_book(book_return_num)
        elif int(menu) == 3:
            book_index = int(input("Enter index of book: "))
            book_borrow_num = int(input("Enter the number of book you want to borrow: "))
            books[book_index].borrow_book(book_borrow_num)
        elif int(menu) == 4:
            print("Program ended!")
            break
        else:
            print("Please enter a valid choice")












