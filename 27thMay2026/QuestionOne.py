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
            print(f"Total amount to pay is {total_price}")




