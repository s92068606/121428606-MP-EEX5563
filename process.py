class Process:
    """
    Represents a process that requests memory.
    """
    def __init__(self, process_id, memory_request):
        self.process_id = process_id
        self.memory_request = memory_request

    def __repr__(self):
        return f"Process {self.process_id} (Memory Request: {self.memory_request})"