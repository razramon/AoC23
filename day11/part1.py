from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        contents = f.read().split("\n")
        mat = [list(x) for x in contents]
    new_mat = []
    for i in range(len(mat)):
        if mat[i].count("#") == 0:
            new_mat.append(["."] * len(mat[0]))
            new_mat.append(["."] * len(mat[0]))
        else:
            new_mat.append(mat[i].copy())

    count = 0
    for i in range(len(mat[0])):
        column = [line[i] for line in mat]
        if column.count("#") == 0:
            for j in range(len(new_mat)):
                new_mat[j].insert(i + count, ".")
            count += 1

    galax = []
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0])):
            if new_mat[i][j] == "#":
                galax.append([i, j])

    dist = []
    for i in range(len(galax)):
        for j in range(i + 1, len(galax)):
            dist.append(sum(abs(a - b) for a, b, in zip(galax[i], galax[j])))
    print(sum(dist))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
