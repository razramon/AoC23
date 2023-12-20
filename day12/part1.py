from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")


def dfs(graph, curr, arr):
    count = 0
    if len(curr) == len(graph):
        curr = [x for x in curr.split(".") if x != ""]
        if len(curr) != len(arr):
            return 0
        for i in range(len(curr)):
            if curr[i] != arr[i]:
                return 0
        return 1
    i = len(curr)
    if graph[i] == "?":
        count += dfs(graph, curr + ".", arr)
        count += dfs(graph, curr + "#", arr)
    else:
        count += dfs(graph, curr + graph[i], arr)
    return count


def main():
    parts = []
    with open(INPUT_FILE, mode="rt") as f:
        contents = f.read().split("\n")
        for line in contents:
            line = line.split(" ")
            parts.append([list(line[0]), [int(x) * "#" for x in line[1].split(",")]])
    count = 0
    for line, arr in parts:
        count += dfs(line, "", arr)
    print(count)


if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
