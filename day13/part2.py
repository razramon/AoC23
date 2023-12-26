from pathlib import Path
import time
import re
import numpy as np

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        contents = f.read().split("\n\n")

    summ = 0
    mult = [100, 1]
    for part in contents:
        mat = np.array([list(x) for x in part.split("\n")])
        for o in range(2):
            found = False
            if o == 1:
                mat = mat.T

            for i in range(mat.shape[0]):
                j = i + 1
                k = i
                dist = 0
                while k >= 0 and j < mat.shape[0]:
                    if "".join(mat[k]) != "".join(mat[j]):
                        if dist >= 1 or sum(mat[k] != mat[j]) > 1:
                            break
                        else:
                            dist += 1
                    if (k == 0 or j == mat.shape[0] - 1) and dist == 1:
                        summ += mult[o] * (i + 1)
                        found = True
                    k -= 1
                    j += 1
                if found:
                    break
            if found:
                break
    print(summ)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
