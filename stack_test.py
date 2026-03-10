import sys

def recursive_function(depth):
    if depth % 500 == 0:
        print(f"Current recursion depth: {depth}")
    recursive_function(depth + 1)

print("Starting recursion test...")

try:
    sys.setrecursionlimit(100000)
    recursive_function(1)
except RecursionError:
    print("[!] Python's internal recursion limit reached.")
except Exception as e:
    print(f"[!] System error occurred: {e}")
