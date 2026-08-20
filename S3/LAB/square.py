m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
square_set = {i*i for i in range(m,n+1) if i%2==0}
print("square of even numbers:",square_set)