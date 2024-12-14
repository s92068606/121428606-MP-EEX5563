from memory_block import MemoryBlock
from process import Process

class FirstFitAllocator:
    """
    Implements the First Fit memory allocation algorithm with process management.
    """
    def __init__(self):
        self.memory_blocks = []  # List of memory blocks
        self.processes = []      # List of processes

    def add_memory_blocks(self, block_sizes):
        """
        Add memory blocks to the allocator.
        """
        for size in block_sizes:
            self.memory_blocks.append(MemoryBlock(size))

    def add_process(self, process_id, memory_request):
        """
        Add a new process with its memory request and automatically allocate memory.
        """
        process = Process(process_id, memory_request)
        self.processes.append(process)
        allocated = self._allocate_memory_automatically(process)
        if not allocated:
            print(f"Process {process_id} (Request: {memory_request}) could not be allocated to any block.")

    def _allocate_memory_automatically(self, process):
        """
        Automatically allocate memory to the given process using the First Fit algorithm.
        """
        for block in self.memory_blocks:
            if not block.is_allocated and block.size >= process.memory_request:
                block.is_allocated = True
                block.allocated_to = process.process_id
                print(f"Memory of size {block.size} allocated to Process {process.process_id}.")
                return True
        return False  # Memory allocation failed

    def display_state(self):
        """
        Display memory blocks, all processes, and unallocated processes at once.
        """
        print("\nCurrent Memory Blocks:")
        for idx, block in enumerate(self.memory_blocks):
            print(f"Block {idx + 1}: {block}")

        print("\nProcesses:")
        for process in self.processes:
            print(process)

        print("\nUnallocated Processes:")
        unallocated = [p for p in self.processes if all(b.allocated_to != p.process_id for b in self.memory_blocks)]
        if unallocated:
            for process in unallocated:
                print(process)
        else:
            print("All processes have been allocated memory.")
