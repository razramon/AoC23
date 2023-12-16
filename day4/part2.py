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
    n = len(cards)
    copies = [1]*n
    for i in range(n):
        point = 0
        card = cards[i]
        for x in card[1]:
            if(not x.isdigit()):
                continue
            if(x in card[0]):
                card[0].remove(x)
                point += 1
        if(point != 0):
            for j in range(i+1,min(n,i+point+1)):
                copies[j] += copies[i]
    print(sum(copies))


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    