from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")
addition = 1000000


def main():
    with open(INPUT_FILE, mode="rt") as f:
        contents = f.read().split("\n")
        mat = [list(x) for x in contents]
    rows_empty = []
    for i in range(len(mat)):
        if mat[i].count("#") == 0:
            rows_empty.append(i)

    colums_empty = []
    for i in range(len(mat[0])):
        column = [line[i] for line in mat]
        if column.count("#") == 0:
            colums_empty.append(i)

    galax = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "#":
                galax.append([i, j])

    dist = []
    for i in range(len(galax)):
        for j in range(i + 1, len(galax)):
            empty = 0
            for x in rows_empty:
                minn = min(galax[i][0], galax[j][0])
                maxx = max(galax[i][0], galax[j][0])
                if minn <= x <= maxx:
                    empty += 1
            for x in colums_empty:
                minn = min(galax[i][1], galax[j][1])
                maxx = max(galax[i][1], galax[j][1])
                if minn <= x <= maxx:
                    empty += 1
            dist.append(
                sum(abs(a - b) for a, b, in zip(galax[i], galax[j]))
                + empty * addition
                - empty # remove duplicates
            )  
    print(sum(dist))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
