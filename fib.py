def fibonacci(n):
    """Return a list with the first n Fibonacci numbers in an easy, readable way."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


if __name__ == "__main__":
    import sys
    # Allow passing the count as a command-line argument, otherwise ask the user.
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            print("Please provide a valid integer number.")
            sys.exit(1)
    else:
        try:
            count = int(input("How many Fibonacci numbers do you want? "))
        except ValueError:
            print("Please enter a valid integer.")
            sys.exit(1)

    nums = fibonacci(count)
    print("Fibonacci series (first {}):".format(count))
    print(", ".join(str(x) for x in nums))
