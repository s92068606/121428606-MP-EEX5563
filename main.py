from allocator import FirstFitAllocator

class InputValidator:
    """
    Provides input validation methods to ensure robust user input handling.
    """
    @staticmethod
    def validate_positive_integer(prompt):
        """
        Prompts the user for a positive integer and validates the input.

        Args:
            prompt (str): The message to display to the user.

        Returns:
            int: A valid positive integer input by the user.
        """
        while True:
            try:
                value = int(input(prompt))
                if value <= 0:
                    raise ValueError("Value must be greater than zero.")
                return value
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a positive integer.")

def main():
    """
    Main function to execute the First Fit Memory Allocator program.
    Handles memory block and process inputs, and displays the final allocation state.
    """
    # Initialize the memory allocator
    allocator = FirstFitAllocator()

    # Welcome message
    print("\nWelcome to the First Fit Memory Allocator!!\n")

    # Step 1: Input the number of memory blocks
    memory_block_limit = InputValidator.validate_positive_integer("Enter the maximum number of memory blocks: ")

    # Step 2: Input sizes of memory blocks
    block_sizes = []
    for i in range(memory_block_limit):
        size = InputValidator.validate_positive_integer(f"Enter size for Memory Block {i + 1}: ")
        block_sizes.append(size)
    allocator.add_memory_blocks(block_sizes)

    # Step 3: Input the number of processes
    print()  # Blank line for better readability
    process_limit = InputValidator.validate_positive_integer("Enter the maximum number of processes: ")

    # Step 4: Input memory requests for each process and add them to the allocator
    for i in range(1, process_limit + 1):
        memory_request = InputValidator.validate_positive_integer(f"Enter memory request for Process P{i}: ")
        process_id = f"P{i}"  # Auto-generated process ID
        allocator.add_process(process_id, memory_request)

    # Step 5: Display the final allocation state
    print("\nFinal State of Memory Allocation:")
    allocator.display_state()

if __name__ == "__main__":
    main()
