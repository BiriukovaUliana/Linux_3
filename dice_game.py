import random
import sys

filename = "dice_results.txt"

try:
    with open(filename, "w") as f:
        for i in range(1, 2001):
            result = random.randint(1, 6)
            line = f"Roll #{i}: Result {result}\n"
            f.write(line)
            f.flush()
    print("Success")
except OSError as e:
    print(f"Error: {e}")
