#Question 9
log = []
avg = []
i = 0
def calculate_total_steps(steps):
    total = sum(steps)
    print(f'Total amount of steps is {total}')
def calculate_average_steps(total):
    average_steps = sum(total)/7
    print(f"Average steps this week is {average_steps}")
    avg.append(average_steps)
def get_activity_level(average):
    if average[0] > 8000:
        print("You are Highly Active!")
    elif 5000 <= average[0] <= 7999:
        print("You are Highly Active!")
        print("You are Moderately Active!")
    else:
        print("You are Lowly Active!")
while i <= 7:
    i += 1
    if i == 1:
        daily_steps = int(input("Input your steps for Monday: "))
        log.append(daily_steps)
    elif i == 2:
        daily_steps = int(input("Input your steps for Tuesday: "))
        log.append(daily_steps)
    elif i == 3:
        daily_steps = int(input("Input your steps for Wednesday: "))
        log.append(daily_steps)
    elif i == 4:
        daily_steps = int(input("Input your steps for Thursday: "))
        log.append(daily_steps)
    elif i == 5:
        daily_steps = int(input("Input your steps for Friday: "))
        log.append(daily_steps)
    elif i == 6:
        daily_steps = int(input("Input your steps for Saturday: "))
        log.append(daily_steps)
    else:
        daily_steps = int(input("Input your steps for Sunday: "))
        log.append(daily_steps)
        break
calculate_total_steps(log)
calculate_average_steps(log)
get_activity_level(avg)