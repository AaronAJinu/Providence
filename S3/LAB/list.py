n = int(input("Enter the number of elements: "))
my_list = []
for i in range(n):
    element = int(input("Enter the element : "))
    my_list.append(element)
    unique_element = []
for item in my_list:
    if item not in unique_element:
        unique_element.append(item)
print("Original List: ",my_list)
print("Unique Element: ",unique_element)