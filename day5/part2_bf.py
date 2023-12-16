from pathlib import Path
import time
import re
from termcolor import colored
import math
from tqdm import *

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.read().split("\n\n")
    dic = []
    for p in parts:
        line = p.split(":")
        if line[0] == "seeds":
            l = list(map(int, line[1].strip().split(" ")))
            lines = []
            for i in range(0, len(l), 2):
                lines.append([l[i], l[i] + l[i + 1]])
            print(lines)
        else:
            lines = [list(map(int, x.split(" "))) for x in line[1].strip().split("\n")]
            lines = sorted(lines, key=lambda x: x[1])
        dic.append(lines)
    counter = 0
    found = False
    while not found:
        num = counter
        for i in range(len(dic) - 1, 0, -1):
            next = dic[i]
            j = 0
            while j < len(next) and not (next[j][0] <= num < next[j][0] + next[j][2]):
                j += 1
            if j != len(next) and next[j][0] <= num < next[j][0] + next[j][2]:
                num = next[j][1] + num - next[j][0]
        for x in dic[0]:
            if x[0] <= num < x[1]:
                found = True
                break
        if not found:
            counter += 1
        if counter % 100000 == 0:
            print(counter)
    print(counter)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
