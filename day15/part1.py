from pathlib import Path
import time
import re
import numpy as np

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.read().strip().split(",")
    amount = 0
    for part in parts:
        curr = 0
        for c in part:
            curr = (curr + ord(c)) * 17 % 256
        amount += curr
    print(amount)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
