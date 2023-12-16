from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    parts = defaultdict(list)
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.read().split("\n\n")
        inst = lines[0]
        for line in lines[1].split("\n"):
            line = line.split("=")
            to = line[1].strip().split(", ")
            parts[line[0].strip()] = [to[0][1:], to[1][:-1]]
    steps = 0
    inf_loop = False
    curr = "AAA"
    while curr != "ZZZ" and not inf_loop:
        for ins in inst:
            if curr == parts[curr][1] == parts[curr][0]:
                print("inf loop")
                inf_loop == True
                break
            if ins == "R":
                curr = parts[curr][1]
            else:
                curr = parts[curr][0]
            steps += 1
        if steps % 10000 == 0:
            print(steps)
    print(steps)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
