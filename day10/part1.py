from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def to_go(mat, prev, curr):
    symbol = mat[curr[0]][curr[1]]
    next_pos = []
    if symbol == "|":
        next_pos.append([curr[0] - 1, curr[1]])
        next_pos.append([curr[0] + 1, curr[1]])
    elif symbol == "-":
        next_pos.append([curr[0], curr[1] - 1])
        next_pos.append([curr[0], curr[1] + 1])
    elif symbol == "L":
        next_pos.append([curr[0], curr[1] + 1])
        next_pos.append([curr[0] - 1, curr[1]])
    elif symbol == "J":
        next_pos.append([curr[0], curr[1] - 1])
        next_pos.append([curr[0] - 1, curr[1]])
    elif symbol == "7":
        next_pos.append([curr[0] + 1, curr[1]])
        next_pos.append([curr[0], curr[1] - 1])
    elif symbol == "F":
        next_pos.append([curr[0] + 1, curr[1]])
        next_pos.append([curr[0], curr[1] + 1])
    for pos in next_pos:
        if pos[0] != prev[0] or pos[1] != prev[1]:
            break
    return [pos] + [curr]


def main():
    with open(INPUT_FILE, mode="rt") as f:
        contents = f.read()
        start_i = contents.replace("\n", "").index("S")
        mat = contents.split("\n")
        start = [start_i // len(mat[0]), start_i % len(mat[0])]
    paths = []
    if mat[start[0]][start[1] - 1] in "F-L":  # left
        paths.append([[start[0], start[1] - 1], start])
    if mat[start[0]][start[1] + 1] in "7-J":  # right
        paths.append([[start[0], start[1] + 1], start])
    if mat[start[0] - 1][start[1]] in "F|7":  # above
        paths.append([[start[0] - 1, start[1]], start])
    if mat[start[0] + 1][start[1]] in "|LJ":  # under
        paths.append([[start[0] + 1, start[1]], start])
    max_len = len(mat[0]) * len(mat) // 2
    counter = 1
    while (
        paths[0][0][0] != paths[1][0][0] or paths[0][0][1] != paths[1][0][1]
    ) or counter < max_len:
        for i in range(len(paths)):
            paths[i] = to_go(mat, paths[i][1], paths[i][0])
        counter += 1
        if not (paths[0][0][0] != paths[1][0][0] or paths[0][0][1] != paths[1][0][1]):
            break

    print(counter)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
