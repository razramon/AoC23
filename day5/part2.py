from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "test.txt")


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.read().split("\n\n")
    dic = []
    for p in parts:
        line = p.split(":")
        if(line[0] == "seeds"):
            l = list(map(int,line[1].strip().split(" ")))
            lines = []
            for i in range(0,len(l),2):
                lines.append([l[i],l[i+1]])
        else:
            lines = [list(map(int, x.split(" "))) for x in line[1].strip().split("\n")]
            lines = sorted(lines,key=lambda x:x[1])
        dic.append(lines)
    curr = dic[0]
    print(curr)
    for i in range(1,len(dic)):
        next = dic[i]
        next_h = []
        while(curr):
            num = curr.pop(0)
            j = 0
            while(j < len(next) and next[j][1] <= num[0] < next[j][1]+next[j][2] ):
                if(j+1 < len(next) and next[j][1]+next[j][2] <= num[0] < next[j+1][1]):
                    break
                j += 1
            while(num[1] > 0 and j < len(next)):
                if(num[0] < next[j][1]):
                    dist = next[j][1] - num[0]
                    if(dist > num[1]):
                        next_h.append([num[0],num[1]])
                        num[1] = 0
                    else:
                        next_h.append([num[0],dist])
                        num[1] -= dist
                        num[0] = next[j][1]
                else:
                    dist = num[0] - next[j][1]
                    if(next[j][2] > num[1]):
                        next_h.append([num[0],num[1]])
                        num[1] = 0
                    else:
                        next_h.append([num[0],dist])
                        num[1] -= dist
                j += 1
        curr = next_h
        print(curr)
    print(min(curr))





if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    