from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.read().split("\n")
        parts = [[int(x) for x in line.split(" ")] for line in lines]
    for i in range(len(parts)):
        ext = [[parts[i][j] - parts[i][j - 1] for j in range(1, len(parts[i]))]]
        indx = 0
        while sum(ext[indx]) != 0:
            ext.append(
                [ext[indx][j] - ext[indx][j - 1] for j in range(1, len(ext[indx]))]
            )
            indx += 1
        ext[-1].append(0)
        for j in range(len(ext) - 2, -1, -1):
            ext[j].append(ext[j][-1] + ext[j + 1][-1])
        parts[i].append(parts[i][-1] + ext[0][-1])

    print(sum([part[-1] for part in parts]))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
