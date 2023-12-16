from pathlib import Path
import time
from collections import Counter, defaultdict
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    lines = []
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()

    parts = defaultdict(list)
    for line in lines:
        line = line.strip().split(" ")
        x = [list(x) for x in Counter(line[0]).most_common()]
        d = dict(x)
        if "J" in d.keys():
            amount = d["J"]
            if amount == 4:
                x[1][1] += amount
                del x[0]
            if amount == 3:
                x[1][1] += amount
                del x[0]
            if amount == 2:
                if x[0][0] == "J":
                    x[1][1] += amount
                    del x[0]
                else:
                    x[0][1] += amount
            if amount == 1:
                if x[0][0] == "J":
                    x[1][1] += amount
                    del x[0]
                else:
                    x[0][1] += amount

        if x[0][1] == 5:  # five of a kind
            parts[0].append([line[0], int(line[1])])
        elif x[0][1] == 4:  # four of a kind
            parts[1].append([line[0], int(line[1])])
        elif x[0][1] == 3:
            if x[1][1] == 2:  # full house
                parts[2].append([line[0], int(line[1])])
            else:  # three of a kind
                parts[3].append([line[0], int(line[1])])
        elif x[0][1] == 2:
            if x[1][1] == 2:  # two pairs
                parts[4].append([line[0], int(line[1])])
            else:  # one pair
                parts[5].append([line[0], int(line[1])])
        else:  # high card
            parts[6].append([line[0], int(line[1])])

    order_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"][::-1]
    someorder = {letter: val for val, letter in enumerate(order_list)}
    for x in parts:
        parts[x].sort(key=lambda x: [someorder.get(letter) for letter in x[0]])

    rank = 1
    for i in range(6, -1, -1):
        if i in parts:
            for x in parts[i]:
                x.append(rank)
                rank += 1

    for i in range(6, -1, -1):
        if i in parts:
            for x in parts[i]:
                print(x[0], x[1], x[2])
    s = 0
    for i in range(6, -1, -1):
        if i in parts:
            for x in parts[i]:
                # print(x[0], x[1], x[2])
                s += x[1] * x[2]
    print(s)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
