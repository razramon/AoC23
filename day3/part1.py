from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check(x, y, lines):
    for i in range(max(0, x - 1), min(len(lines), x + 2)):
        for j in range(max(0, y - 1), min(len(lines[i]), y + 2)):
            if not lines[i][j].isdigit() and lines[i][j] != ".":
                return True
    return False


def main():
    lines = []
    with open(INPUT_FILE, mode="rt") as f:
        for line in f.readlines():
            lines.append(line.strip())
    summing = 0
    for i in range(len(lines)):
        curr = ""
        got = False
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                if not got:
                    got = check(i, j, lines)
                curr += lines[i][j]
                if j == len(lines[i]) - 1 and curr != "" and got:
                    summing += int(curr)
            else:
                if curr != "" and got:
                    summing += int(curr)
                curr = ""
                got = False
    print(summing)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
