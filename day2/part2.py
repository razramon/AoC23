from pathlib import Path
import time
import math

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()
    
    sum = 0
    for line in lines:
        line = line.split(":")
        games = line[1].split(";")
        blue = -math.inf
        green = -math.inf
        red = -math.inf
        for g in games:
            cubes = g.split(",")
            for cube in cubes:
                cube = cube.strip()
                if(cube.split(" ")[1] == "blue"):
                    blue = max(blue, int(cube.split(" ")[0]))
                if(cube.split(" ")[1] == "green"):
                    green = max(green, int(cube.split(" ")[0]))
                if(cube.split(" ")[1] == "red"):
                    red = max(red, int(cube.split(" ")[0]))
        print(line, blue,red,green)
        total = 1
        if(blue != -math.inf):
            total *= blue                    
        if(red != -math.inf):
            total *= red
        if(green != -math.inf):
            total *= green
        sum += total
    
    print(sum)

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    