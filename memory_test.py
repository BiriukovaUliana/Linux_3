import sys
import time

print("Starting memory allocation test...")
data = []

try:
    for i in range(1, 1000):
        data.append(' ' * (10**7)) 
        if i % 5 == 0:
            print(f"Allocated: {i * 10} MB")
        time.sleep(0.1) 

except MemoryError:
    print("\n[!] Python caught a MemoryError!")
except Exception as e:
    print(f"\n[!] System error: {e}")
