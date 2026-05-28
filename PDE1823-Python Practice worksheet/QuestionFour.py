list = []
x = 0
def calculate_sum(n):#
    sum_of_numbers = sum(n)
    return sum_of_numbers
while x<5:
    x+=1
    user_input = int(input("Enter a number: "))
    list.append(user_input)
sum = calculate_sum(list)
print(f"The total is: {sum}")