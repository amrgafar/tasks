def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    number = 10  # Example number
    result = fibonacci(number)
    print(f"The {number}-th Fibonacci number is:", result)
    return result

main()
