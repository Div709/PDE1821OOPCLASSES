def result_check(number):
    if number > 50:
        print("Result: Pass")
    else:
        print("Result: Fail")
user_input = int(input("Enter your marks: "))
result_check(user_input)