def factorial(n):
    result=1
    for i in range(2,n+1):
        result*=i
    return result
def is_palindrome(num):
    num=str(num)
    return num==num[::-1]
def count_digits(num):
    return len(str(num))
num=int(input("enter the number:"))
if num%2==1:
    fact= factorial(num)
    digit_count= count_digits(fact)
    print(f"the factorial of {num} is {fact}")
    print(f"the number of digits in the factorial is {digit_count}")
else:
    if is_palindrome(num):
        print(f"the number {num} is a palindrome")
    else:
        print(f"the number {num} is not a palindrome")
