from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.readlines()
    t = int("".join([x for x in parts[0].split(":")[1].strip().split(" ") if x != ""]))
    dis = int("".join([x for x in parts[1].split(":")[1].strip().split(" ") if x != ""]))
    print(t, dis)

    way = 0
    for j in range(1,t):
        if(j*(t-j) > dis):
            way += 1
    print(way)
            

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")