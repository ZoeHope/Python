#The Fibonacci sequence is a set of numbers that starts with a one or a zero, followed by a one, and proceeds based on the rule that each number (called a Fibonacci number) is equal to the sum of the preceding two numbers.

def FibonacciNumbers(n):
    fibonacci_numbers = [0, 1]
    for i in range(2,n):
        fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])
    print(fibonacci_numbers)
    return

FibonacciNumbers(100)
