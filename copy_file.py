import sys
import os

if len(sys.argv) != 3:
    print("Program need two arguments")
    sys.exit(1)

src = sys.argv[1]
dest = sys.argv[2]

if not os.path.isfile(src) or not os.access(src, os.R_OK):
    print(f"Cannot open file {src} for reading")
    sys.exit(1)

try:
    with open(dest, 'ab'): 
        pass
except OSError:
    print(f"Cannot open file {dest} for writing")
    sys.exit(1)

try:
    with open(src, 'rb') as f_src, open(dest, 'wb') as f_dest:
        while True:
            chunk = f_src.read(1024)
            if not chunk:
                break
            f_dest.write(chunk)
            f_dest.flush()
    print("Copy successful")
except OSError as e:
    print(f"Error during copy (possibly size limit): {e}")
