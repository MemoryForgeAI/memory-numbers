from memory_numbers import MemoryNumber
import random

class ReflectionAgent:
    def __init__(self):
        self.reflections = []
        self.strategy = "random"  # Can later evolve to smarter strategies

    def attempt_task(self, a, b, op):
        task_label = f"{a} {op} {b}"
        target = eval(f"{a} {op} {b}")
        mem_number = MemoryNumber(0)
        success = False
        attempts = 0

        print(f"\n🎯 Task: {task_label} = {target}")

        while not success and attempts < 5:
            if self.strategy == "random":
                guess = random.randint(target - 3, target + 3)
                mem_number.apply(lambda x: guess, f"guessed {guess}")

            print(f"Try {attempts + 1}: Guessed {mem_number.value}")
            if mem_number.value == target:
                print("✅ Success!")
                success = True
            else:
                print("❌ Incorrect.")
            attempts += 1

        self.reflect(task_label, mem_number, success)
        return success

    def reflect(self, task_label, memory_number, success):
        reflection = {
            "task": task_label,
            "success": success,
            "trace": memory_number.memory_chain.copy()
        }
        self.reflections.append(reflection)

    def review_reflections(self):
        print("\n=== AGENT REFLECTION LOG ===")
        for i, r in enumerate(self.reflections):
            print(f"\nReflection {i+1}: {r['task']} — {'✅' if r['success'] else '❌

