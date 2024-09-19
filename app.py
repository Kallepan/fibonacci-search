from typing import List

"""
Fibonacci search is a comparison-based technique that uses Fibonacci numbers to search an element in a sorted array.
It is similar to the binary search technique but has a lower time complexity.
The time complexity of the Fibonacci search technique is O(log n).
"""


# Generate Fibonacci series
def gen_fib(number: int) -> List[int]:
    fib = [0, 1]
    for i in range(2, number):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


# Fibonacci search
def fibonacci_search(input: List[int], to_find: int) -> int:
    fib = gen_fib(len(input))

    # Offset is used to keep track of the eliminated range from the input list
    offset = -1

    # Loops over the Fibonacci series
    while fib[-1] > 1:
        # Find the index of the element to be searched
        i = min(offset + fib[-2], len(input) - 1)

        # Check if the element is less than, greater than or equal to the element to be searched
        # If the element is less than the element to be searched
        if input[i] < to_find:
            fib = fib[:-1]
            offset = i

        # If the element is greater than the element to be searched
        elif input[i] > to_find:
            fib = fib[:-2]

        # If the element is equal to the element to be searched
        else:
            print(f"Element found at index {i}")
            return i

    # We did not find the element :(
    print("Element not found")
    return -1


def main():
    search_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    to_find = 5
    fibonacci_search(search_list, to_find)


if __name__ == "__main__":
    main()
