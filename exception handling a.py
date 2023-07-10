numbers = input("Enter a list of numbers : ").split()
index = int(input("Enter the index: "))
try:
    element = numbers[index]
    print(f"The element at index {index} is: {element}")
except IndexError:
    print("Error: Index is out of range!")
