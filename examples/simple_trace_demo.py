import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from memory_numbers import MemoryNumber

def main():
    print("Starting MemoryNumber demo...\n")

    # Create a MemoryNumber and apply transformations
    num = MemoryNumber(10)
    num.apply(lambda x: x + 5, "add 5")
    num.apply(lambda x: x * 2, "multiply by 2")
    num.apply(lambda x: x - 3, "subtract 3")

    # Display final result and memory trace
    print(f"\nFinal Value: {num.value}")
    num.trace()

if __name__ == "__main__":
    main()
