'''
items_Quantity = int(input("How many items customer bought: "))
i = 0
items = []

def calculate_total(item):
    total = sum(item) # sum() gives sum of a list
    return total

def apply_discount(total):
    new_total = (90/100) * total
    return new_total

while i < items_Quantity:
    i = i + 1
    item_price= int(input(f"Enter price item {i}: "))
    items.append(item_price)

    if i == items_Quantity:
        total_price = calculate_total(items)
        i = 0
        if total_price > 1000:
            total_price_after_discount = apply_discount(total_price)
            print(f"Total amount to pay is {total_price_after_discount}")
        else:
            print(f"Total amount to pay is {total_price}") '''

#Question 2
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



