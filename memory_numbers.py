class MemoryNumber:
    def __init__(self, base_value):
        """
        Initialize with a base value and an empty memory chain.
        """
        self.base_value = base_value
        self.value = base_value
        self.memory_chain = []  # Stores (label, transformation function) pairs

    def apply(self, transformation, label=None):
        """
        Applies a transformation and records it in memory.
        Args:
            transformation: A function taking a number and returning a number.
            label: A string describing the transformation.
        """
        old_value = self.value
        self.value = transformation(self.value)
        self.memory_chain.append({
            "label": label or transformation.__name__,
            "input": old_value,
            "output": self.value
        })

    def undo_last(self):
        """
        Undoes the last transformation. Note: Only works if original value was saved.
        """
        if self.memory_chain:
            self.memory_chain.pop()
            self.value = self.base_value
            for step in self.memory_chain:
                self.value = step["output"]

    def reset(self):
        """
        Resets to the base value and clears memory.
        """
        self.value = self.base_value
        self.memory_chain.clear()

    def trace(self):
        """
        Prints a readable memory trace.
        """
        print("🧠 Memory Trace:")
        for i, step in enumerate(self.memory_chain):
            print(f"  Step {i+1}: {step['label']} | {step['input']} ➜ {step['output']}")

    def __repr__(self):
        return f"<MemoryNumber: {self.value} | Steps: {len(self.memory_chain)}>"

