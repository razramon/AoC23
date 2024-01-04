from pathlib import Path
import time
import re
import numpy as np
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def get_indx(s):
    indx = 0
    for c in s:
        indx = (indx + ord(c)) * 17 % 256
    return indx


def main():
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.read().strip().split(",")
    hashm = {}
    for i in range(256):
        hashm[i] = []
    for part in parts:
        if "=" in part:
            content = part.split("=")
            lbl = content[0]
            i = get_indx(lbl)
            fl = int(content[1])
            found = False
            for j in range(len(hashm[i])):
                if lbl == hashm[i][j][0]:
                    hashm[i][j][1] = fl
                    found = True

            if not found:
                hashm[i].append([lbl, fl])
        else:
            lbl = part.split("-")[0]
            i = get_indx(lbl)
            lbls = [x[0] for x in hashm[i]]
            if lbl in lbls:
                hashm[i].pop(lbls.index(lbl))
    amount = 0
    for i in hashm:
        for j in range(len(hashm[i])):
            amount += (i + 1) * (j + 1) * hashm[i][j][1]
    print(amount)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
