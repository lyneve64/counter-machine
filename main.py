import csv
import sys

running = True
instructions = []
instruction = 0
length_instructions = 0
registers = {
    "a": 0,
    "b": 0,
    "c": 0
}

with open(sys.argv[1], newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        instructions.extend(row)

while running:
    if instructions[instruction][:3] == "inc":
        print(instructions[instruction])
        registers[instructions[instruction][3]] += 1
        instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "dec":
        print(instructions[instruction])
        registers[instructions[instruction][3]] -= 1
        instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jez":
        print(instructions[instruction])
        if registers[instructions[instruction][3]] == 0:
            print("jumped")
            instruction = int(instructions[instruction][4:]) - 1
        else:
            instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jnz":
        print(instructions[instruction])
        if registers[instructions[instruction][3]] != 0:
            print("jumped")
            instruction = int(instructions[instruction][4:]) - 1
        else:
            instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jmp":
        print(instructions[instruction])
        instruction = int(instructions[instruction][3:]) - 1
        print(registers)

    elif instructions[instruction][0] == "hlt":
        print(instructions[instruction])
        running = False
        print(registers)

    else:
        print("invalid instruction")
        running = False
        print(registers)

    if instruction > len(instructions) - 1:
        running = False
        print(registers)

    try:
        if sys.argv[2] == "debug":
            input("")
    except IndexError:
        pass


print(registers)
