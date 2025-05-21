def count_from_negative_to_positive_infinity():
    """
    Generator function to simulate counting from negative infinity to positive infinity.
    """
    # Start from a very large negative number
    current = -1e100  # This is a very large negative number

    while True:
        yield current
        current += 1

        # Reset to a very large negative number after reaching a very large positive number
        if current > 1e100:  # This is a very large positive number
            current = -1e100

# Example usage of the generator
counter = count_from_negative_to_positive_infinity()

# Print a few values to demonstrate
for _ in range(10):
    print(next(counter))
  
