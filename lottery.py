import random
import signal
import sys

def handle_cpu_limit(signum, frame):
    print("\n[!] CPU Time limit reached!")
    sys.exit(0)

signal.signal(signal.SIGXCPU, handle_cpu_limit)

print("Running lottery... Generating numbers until CPU limit hits.")

try:
    while True:
        res1 = random.sample(range(1, 50), 7)
        res2 = random.sample(range(1, 37), 6)
except:
    sys.exit(0)
