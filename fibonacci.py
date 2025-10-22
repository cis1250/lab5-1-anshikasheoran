# Get and validate user input
def get_number_of_terms():
    while True:
        try:
            n = int(input("Enter how many terms of the Fibonacci sequence you want: "))
            if n > 0:
                return n
            else:
                print("Error: Please enter a positive integer greater than 0.")
        except ValueError:
            print("Error: Invalid input. Please enter a whole number.")

# Generate Fibonacci sequence
def generate_fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Print the Fibonacci sequence
def print_sequence(sequence):
    print("\nFibonacci Sequence:")
    print(", ".join(map(str, sequence)))

# Main function to control program flow
def main():
    n = get_number_of_terms()
    sequence = generate_fibonacci(n)
    print_sequence(sequence)

# Function to run the program
if __name__ == "__main__":
    main()
