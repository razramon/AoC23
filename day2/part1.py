from pathlib import Path
import time

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def main():
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()

    sum = 0
    for line in lines:
        line = line.split(":")
        id = int(line[0].split(" ")[1])
        games = line[1].split(";")
        bad = False
        for g in games:
            cubes = g.split(",")
            for cube in cubes:
                cube = cube.strip()
                print(cube)
                if cube.split(" ")[1] == "blue" and int(cube.split(" ")[0]) > 14:
                    bad = True
                if cube.split(" ")[1] == "green" and int(cube.split(" ")[0]) > 13:
                    bad = True
                if cube.split(" ")[1] == "red" and int(cube.split(" ")[0]) > 12:
                    bad = True
            if bad:
                break
        if bad:
            continue

        sum += id

    print(sum)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
