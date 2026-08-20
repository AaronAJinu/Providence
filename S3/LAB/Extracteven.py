m = int(input("Enter a number:"))
number = []
for i in range(m):
    num = int(input(f"Enter the element {i+1}: "))
    number.append(num)
    even_number = []

for num in number:
    if num%2==0:
        even_number.append(num)
print("Orginal number is:",number)
print("Even number is :",even_number)
