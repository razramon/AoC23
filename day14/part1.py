from pathlib import Path
import time
import re
import numpy as np

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        mat = np.array([list(x) for x in f.read().split("\n")])
    mat = mat.T
    for i in range(len(mat)):
        parts = np.array([list(x) for x in "".join(mat[i]).split("#")])
        for j in range(len(parts)):
            parts[j] = np.sort(parts[j])[::-1]
            if len(parts) > 1:
                parts[j] = np.append(parts[j], "#")
        if len(parts) > 1:
            mat[i] = np.concatenate(parts)[:-1]
        else:
            mat[i] = parts
    dist = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == "O":
                dist += len(mat[0]) - j

    print(dist)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
