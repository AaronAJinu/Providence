n = int(input("Enter the number of tuple:"))
my_list = []
for i in range (n):
    print(f"Enter a number {i+1}:")
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))
    my_list.append((a,b))
print("\n Unordered list:")
for t in my_list:
    print(t)
for i in range(n):
    for j in range(0,n -i -1):
        if my_list[j][1]>my_list[j+1][1]:
            temp = my_list[j]
            my_list[j] = my_list[j+1]
            my_list[j+1] = temp
print("\n Ordered list:")
for t in my_list:
    print(t)

