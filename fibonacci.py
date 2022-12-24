
# Fibonacci series up to n
def fib(n):
    a = 0
    b = 1
    for i in range(0, n):
        print(a, end=' ')
        a = b
        b = a + b
    print()

print("This is a fibonacci calculator program")

check = True
while check:
    num = input("Enter the number of series:")
    if num == 'exit':
        break
    num = int(num)
    print("Fibonacci series:")
    fib(num)
