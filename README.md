# 121428606-MP-EEX5563

# First Fit Memory Allocator

## Overview
The **First Fit Memory Allocator** is a Python-based simulation of memory allocation in an operating system using the **First Fit** algorithm. This program helps visualize how processes are assigned memory blocks in a system by allocating memory in the first available block that is large enough to hold the process.

## Features
- **Memory Block Management**: Allows the user to define memory blocks of different sizes.
- **Process Allocation**: Processes can request memory, and the allocator assigns the first available memory block that fits the request.
- **Automatic Process ID Assignment**: Processes are automatically assigned IDs based on the order of input.
- **Memory Split**: The allocator handles leftover space within allocated blocks and creates new blocks for leftover memory.
- **User Input Validation**: Ensures that users provide valid input (positive integers for memory sizes and requests).
- **Display**: Displays the current state of all memory blocks and processes, including which blocks are allocated and to which process, and lists any unallocated processes.

## Requirements
- Python 3.7 or later.

## Installation

1. Clone this repository to your local machine:
   
   git clone https://github.com/s92068606/121428606-MP-EEX5563.git

Run the program:

python src/main.py

Usage
Upon running the program, the user will be prompted to enter:

The number of memory blocks.
The sizes of each memory block.
The number of processes.
The memory requests for each process.
The program will then allocate memory using the First Fit algorithm and display the final memory allocation status.

Example Input and Output

Example Input:

Enter the maximum number of memory blocks: 3
Enter size for Memory Block 1: 100
Enter size for Memory Block 2: 200
Enter size for Memory Block 3: 300

Enter the maximum number of processes: 3
Enter memory request for Process P1: 200
Enter memory request for Process P2: 150
Enter memory request for Process P3: 150
Example Output:

Final State of Memory Allocation:

Current Memory Blocks:
Block 1: [Size: 100, Status: Free]
Block 2: [Size: 200, Status: Allocated to Process P1]
Block 3: [Size: 150, Status: Allocated to Process P2]
Block 4: [Size: 150, Status: Allocated to Process P3]

Processes:
Process P1 (Memory Request: 200)
Process P2 (Memory Request: 150)
Process P3 (Memory Request: 150)

Unallocated Processes:
All processes have been allocated memory.