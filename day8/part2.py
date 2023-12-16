from pathlib import Path
import time
from collections import Counter, defaultdict
import re
import math
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def main():
    parts = defaultdict(list)
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.read().split("\n\n")
        inst = lines[0]
        for line in lines[1].split("\n"):
            line = line.split("=")
            to = line[1].strip().split(", ")
            parts[line[0].strip()] = [to[0][1:], to[1][:-1]]
    got = []
    start = [key for key in parts.keys() if key[2] == "A"]
    for curr in start:
        steps = 0
        while curr[2] != "Z":
            for ins in inst:
                if ins == "R":
                    curr = parts[curr][1]
                else:
                    curr = parts[curr][0]
                steps += 1
        got.append(steps)
    result = got[0]
    for x in range(1, len(got)):
        result = lcm(got[x], result)
    print(result)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
