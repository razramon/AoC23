from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def check(x,y,lines):
    for i in range(max(0,x-1),min(len(lines),x+2)):
        for j in range(max(0,y-1),min(len(lines[i]),y+2)):
            if(lines[i][j] == '*'):
                return True, i,j
    return False, -1 ,-1

def main():
    lines = []
    with open(INPUT_FILE, mode="rt") as f:
        for line in f.readlines():
            lines.append(line.strip())
            
    sym_places = {}
    for i in range(len(lines)):
        curr = ""
        got = False
        for j in range(len(lines[i])):
            if(lines[i][j].isdigit()):
                if(not got):
                    got, x, y = check(i,j,lines)
                    if(got):
                        if(f"{x},{y}" not in sym_places):
                            sym_places[f"{x},{y}"]=[]
                curr += lines[i][j]
                if(j == len(lines[i])-1 and curr != "" and got):
                    sym_places[f"{x},{y}"].append(int(curr))
            else:
                if(curr != "" and got):
                    sym_places[f"{x},{y}"].append(int(curr))
                curr = ""
                got = False

    print(sym_places)
    summing = 0
    for k in sym_places:
        if(len(sym_places[k])==2):
            summing += sym_places[k][0] * sym_places[k][1]
    print(summing)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    