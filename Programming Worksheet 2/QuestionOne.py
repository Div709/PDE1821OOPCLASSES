# Try 1
'''
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
        print("Book returned successfully")
        return self.borrowed
    def display_book(self):
        print("Library Book list:")
        print(f"Title - {self.title}| Author - {self.author}| Number of Copies - {self.copies}| Amount Borrowed - {self.borrowed}")
        print("---------------------------------------------------------------------------------------------------------------------------")
    def borrow_book(self,n):
        if self.copies - self.borrowed >= 1:
            self.borrowed = self.borrowed + n
            print("Book borrowed successfully")
        else:
            print("Too many books to borrow")
books = []
user_input = input("How many books you want to enter: ")

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
menu = 0
while int(menu) >= 0:
    if int(menu) == 0:
        print(f"Enter 1 to Display Books")
        print(f"Enter 2 to Return Books")
        print(f"Enter 3 to Borrow Books")
        print(f"Enter 4 to End Program")
        menu = int(input("Enter your choice: "))
    elif int(menu) == 1:
        for i in books:
            menu = 0
            i.display_book()
    elif int(menu) == 2:
        x = 1
        while x > 0 :
            book_index = int(input("Enter index of book: "))
            if books[book_index] not in books:
                print("Book does not exist")
                print("Please enter a valid index")
                x = 0
            else:
                book_return_num = int(input("Enter the number of book you want to return: "))
                books[book_index].return_book(book_return_num)
                menu = 0
                break
    elif int(menu) == 3:
        book_index = int(input("Enter index of book: "))
        book_borrow_num = int(input("Enter the number of book you want to borrow: "))
        books[book_index].borrow_book(book_borrow_num)
    elif int(menu) == 4:
        print("Program ended!")

    else:
        print("Please enter a valid choice")
'''
# Try 2
class Book:
    def __init__(self, title, author, copies, borrowed):
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed = borrowed

    def available_copies(self):
        return self.copies - self.borrowed

    def borrow_book(self, n):
        if n <= self.available_copies():
            self.borrowed += n
            print("Book borrowed successfully")
        else:
            print("Not enough copies available")

    def return_book(self, n):
        if n <= self.borrowed:
            self.borrowed -= n
            print("Book returned successfully")
        else:
            print("You cannot return more than borrowed")

    def display_book(self, index):
        print(f"{index} - {self.title} | {self.author} | Copies: {self.copies} | Borrowed: {self.borrowed}")


# ---------------- MAIN PROGRAM ----------------

books = []

# Input of books
num = int(input("Enter number of books (at least 3): "))
while num < 3:
    num = int(input("Please enter at least 3 books: "))

for i in range(num):
    print(f"\nEnter details for book {i}:")
    title = input("Title: ")
    author = input("Author: ")
    copies = int(input("Copies: "))
    borrowed = int(input("Borrowed: "))

    books.append(Book(title, author, copies, borrowed))

# The Menu
while True:
    print("\n--- MENU ---")
    print("1. Display Books")
    print("2. Return Book")
    print("3. Borrow Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nLibrary Books:")
        for i in range(len(books)):
            books[i].display_book(i)

    elif choice == "2":
        index = int(input("Enter book index: "))
        if 0 <= index < len(books):
            n = int(input("How many books to return: "))
            books[index].return_book(n)
        else:
            print("Invalid index")

    elif choice == "3":
        index = int(input("Enter book index: "))
        if 0 <= index < len(books):
            n = int(input("How many books to borrow: "))
            books[index].borrow_book(n)
        else:
            print("Invalid index")

    elif choice == "4":
        print("Program ended!")
        break

    else:
        print("Invalid choice")











