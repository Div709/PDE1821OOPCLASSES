def calculate_area(length,width):
    area = length*width
    return area
length_input = int(input("Enter length: "))
width_input = int(input("Enter width: "))
print(f"The area of the rectangle is:{calculate_area(length_input,width_input)}")