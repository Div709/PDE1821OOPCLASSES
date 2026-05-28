# Question 3
shopping_list= [ ]
def store_in_list(name,list):
    list.append(name)
i = 0
while i < 5:
    i+=1
    user_input = input("Enter an item: ")
    store_in_list(user_input,shopping_list)

print(f"Your shopping list is:")
for item in shopping_list:
    print(item)

