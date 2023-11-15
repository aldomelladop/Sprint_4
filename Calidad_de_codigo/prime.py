import math

def is_prime(n):
    """
    Check whether a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    """Main function to print prime numbers up to 100."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()

if __name__ == '__main__':
    main()
