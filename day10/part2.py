from pathlib import Path
import time
from collections import Counter, defaultdict, deque
import re
from termcolor import colored
from tqdm import *
from shapely.strtree import STRtree

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
        mat = [list(line) for line in contents.splitlines()]
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
    maze = [[start, "S"]]
    counter = 1
    while (
        paths[0][0][0] != paths[1][0][0] or paths[0][0][1] != paths[1][0][1]
    ) or counter < max_len:
        for i in range(len(paths)):
            maze.append(paths[i][1])
            paths[i] = to_go(mat, paths[i][1], paths[i][0])
        counter += 1

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if [i, j] not in maze:
                mat[i][j] = "."

    bigmat = [["."] * (len(mat[0]) * 2)] * (len(mat) * 2)
    bigmat[::2] = mat
    newlines = []
    for line in mat:
        i = 0
        newline = []
        while i < len(line):
            line.insert(i + 1, "-" if line[i] in "LF-" else ".")
            newline += ["|" if line[i] in "F|7" else ".", "."]
            i += 2
        newlines.append(newline)
    bigmat[1::2] = newlines
    bigmat.insert(0, ["."] * len(bigmat[0]))

    # Flood algorithm, starting from the start, because it is not for sure
    curQueue = [[0, 0]]
    while curQueue:
        x, y = curQueue.pop()
        bigmat[y][x] = " "
        if x - 1 >= 0 and bigmat[y][x - 1] == ".":
            curQueue.append([x - 1, y])
        if x + 1 < len(bigmat[0]) and bigmat[y][x + 1] == ".":
            curQueue.append([x + 1, y])
        if y + 1 < len(bigmat) and bigmat[y + 1][x] == ".":
            curQueue.append([x, y + 1])
        if y - 1 >= 0 and bigmat[y - 1][x] == ".":
            curQueue.append([x, y - 1])
    print(sum(line[::2].count(".") for line in mat))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
