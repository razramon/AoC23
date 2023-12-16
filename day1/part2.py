from pathlib import Path
import time
import re

SCRIPT_DIR = Path(__file__).parent
INPUT_FILE = Path(SCRIPT_DIR, "input.txt")

def main():
    with open(INPUT_FILE, mode="rt") as f:
        lines = f.readlines()
    swtch = {"one":"o1e","two":"t2o","three":"t3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}
    sum = 0
    for line in lines:
        line = line.strip()
        for key in swtch:
            line = line.replace(key,swtch[key])
        for key in swtch:
            line = line.replace(key,swtch[key])
        digits =  "".join(re.findall(r'\d+',line))
        if(len(digits) > 0):
            sum += int(digits[0]+digits[-1])
    
    print(sum)

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
    