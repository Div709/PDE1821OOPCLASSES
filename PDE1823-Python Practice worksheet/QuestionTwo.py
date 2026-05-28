# Question 2
def even_odd(n):
    if n % 2 == 0:
        print(f"{n} is an even number")
    else:
        print(f"{n} is an odd number")
user_input = int(input("Enter a number: "))
even_odd(user_input)