from pathlib import Path
import time
import re
from termcolor import colored

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        parts = f.read().split("\n\n")
    dic = []
    for p in parts:
        line = p.split(":")
        if(line[0] == "seeds"):
            lines = sorted(list(map(int,line[1].strip().split(" "))))
        else:
            lines = [list(map(int, x.split(" "))) for x in line[1].strip().split("\n")]
            lines = sorted(lines,key=lambda x:x[1])
        dic.append(lines)
    curr = dic[0]
    print(curr)
    for i in range(1,len(dic)):
        next = dic[i]
        for k in range(len(curr)):
            num = curr[k]
            j = 0
            while(j < len(next) and not (next[j][1] <= num < next[j][1]+next[j][2])):
                j += 1
            
            print("see",num,next, j)
            if(j == len(next)):
                print("not found",num, next)
            if(j != len(next) and next[j][1] <= num < next[j][1]+next[j][2]):
                print("found",next[j][1], num, next[j][1]+next[j][2])
                curr[k] = next[j][0] + num - next[j][1]
        print(curr)
        print("---------------")
    print(curr)
    print(min(curr))





if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    