# Write a python script to
# Form a list of K random numbers within a limit N where K and N are set by the user. Minimum value of K should be 10.
# Define a function (or two functions) to return the composite numbers and prime numbers of this list as two separate lists.
# Determine the square of all prime numbers and square root of all composite numbers
# Plot both prime numbers Vs their squares and composites Vs their square roots on the same figure object as scatterplots. ( two different subplots on the same figure object)

# --------------------------------CODE----------------------------------------


import random
import math
import matplotlib.pyplot as plt

def generate_random_numbers(k, n):
    if k < 10:
        raise ValueError("Minimum value of K should be 10")
    return [random.randint(1, n) for _ in range(k)]

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def separate_numbers(numbers):
    primes = [num for num in numbers if is_prime(num)]
    composites = [num for num in numbers if num > 1 and not is_prime(num)]
    return primes, composites

def process_numbers(primes, composites):
    prime_squares = [p ** 2 for p in primes]
    composite_roots = [math.sqrt(c) for c in composites]
    return prime_squares, composite_roots

def plot_numbers(primes, prime_squares, composites, composite_roots):
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    
    axes[0].scatter(primes, prime_squares, color='blue', label="Prime Numbers")
    axes[0].set_title("Prime Numbers vs Squares")
    axes[0].set_xlabel("Prime Numbers")
    axes[0].set_ylabel("Squares")
    axes[0].legend()
    
    axes[1].scatter(composites, composite_roots, color='green', label="Composite Numbers")
    axes[1].set_title("Composite Numbers vs Square Roots")
    axes[1].set_xlabel("Composite Numbers")
    axes[1].set_ylabel("Square Roots")
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()

try:
    k = int(input("Enter the number of random numbers to generate (K, minimum 10): "))
    n = int(input("Enter the upper limit for the random numbers (N): "))
    
    numbers = generate_random_numbers(k, n)
    print(f"Generated numbers: {numbers}")
    
    primes, composites = separate_numbers(numbers)
    print(f"Prime numbers: {primes}")
    print(f"Composite numbers: {composites}")
    
    prime_squares, composite_roots = process_numbers(primes, composites)
    
    plot_numbers(primes, prime_squares, composites, composite_roots)

except ValueError as e:
    print(f"Error: {e}")
