number = []
positive_list = []
x = 0
def positive_count(num,pos_list):
    for i in num:
        if i > 0:
            pos_list.append(i)
    print(f"The numbers entered are: {num}")
    print(f"There are {len(pos_list)} positive numbers")

while x < 6:
    x+=1
    user_input = int(input("Enter a number: "))
    number.append(user_input)
positive_count(number,positive_list)
