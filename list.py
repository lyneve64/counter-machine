import csv
import sys

running = True
instructions = []
instruction = 0
length_instructions = 0
registers = {
    "a": 0,
    "b": 1,
    "c": 1
}

with open(sys.argv[1], newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        instructions.extend(row)

for i in range(len(instructions)):
    print(str(i + 1) + ": " + instructions[i])
