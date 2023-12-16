from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    cards = []
    with open(INPUT_FILE, mode="rt") as f:
        for line in f.readlines():
            parts = line.strip().split(":")[1].split("|")
            cards.append([parts[0].strip().split(" "),parts[1].strip().split(" ")])
    points = 0
    for card in cards:
        point = 0
        for x in card[1]:
            if(not x.isdigit()):
                continue
            if(x in card[0]):
                card[0].remove(x)
                if(point == 0):
                    point = 1
                else:
                    point *= 2

        points += point
    print(points)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    