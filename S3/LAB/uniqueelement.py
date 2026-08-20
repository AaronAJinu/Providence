text = input("Enter the string:")
unique = set()
for ch in text:
    unique.add(ch)
print("Unique characters:",unique)