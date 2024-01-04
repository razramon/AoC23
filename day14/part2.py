from pathlib import Path
import time
import re
import numpy as np
from tqdm import *

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def cycle(matrix, matrixs):
    found_cycle = False
    for c in range(4):
        mat = np.rot90(matrix, k=c + 1)
        if c % 2 != 0:
            mat = np.flip(mat)
        for i in range(len(mat)):
            parts = np.array([list(x) for x in "".join(mat[i]).split("#")], dtype=list)
            for j in range(len(parts)):
                parts[j] = np.sort(parts[j])[::-1]
                if len(parts) > 1:
                    parts[j] = np.append(parts[j], "#")
            if len(parts) > 1:
                mat[i] = np.concatenate(parts)[:-1]
            else:
                mat[i] = parts
    new_mat = ["\n".join(["".join(x) for x in matrix])]
    if new_mat in matrixs:
        found_cycle = True
    matrixs.append(new_mat)
    return matrix, matrixs, found_cycle


def main():
    with open(INPUT_FILE, mode="rt") as f:
        matrix = np.array([list(x) for x in f.read().split("\n")])
    matrixs = ["\n".join(["".join(x) for x in matrix])]

    number_of_cycles = 1000000000
    for _ in tqdm(range(number_of_cycles)):
        matrix, matrixs, found_cycle = cycle(matrix, matrixs)
        if found_cycle:
            break

    if found_cycle:  # we have 4*number_of_cycles spins
        start = matrixs.index(matrixs[-1])
        dist = len(matrixs) - start - 1  # after this number of spins we get a cycle
        left = (number_of_cycles - start) % dist
        for i in range(left):
            matrix, _, _ = cycle(matrix, [])

    dist = 0
    matrix = np.rot90(matrix, k=1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "O":
                dist += len(matrix[0]) - j

    print(dist)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
