class MemoryBlock:
    """
    Represents a single memory block with a size, allocation status, and associated process.
    """
    def __init__(self, size):
        self.size = size
        self.is_allocated = False
        self.allocated_to = None  # Tracks the process ID that owns this block

    def __repr__(self):
        status = f"Allocated to Process {self.allocated_to}" if self.is_allocated else "Free"
        return f"[Size: {self.size}, Status: {status}]"
