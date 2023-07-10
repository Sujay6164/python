def check_ascending_order(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True
n= input("Enter the list of numbers : ").split()
n= [int(num) for num in n]
is_ascending = check_ascending_order(n)
if is_ascending:
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")
