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
        print("increment")
        match instructions[instruction][3]:
            case "a":
                print("register a")
                registers["a"] += 1
            case "b":
                print("register b")
                registers["b"] += 1
            case "c":
                print("register c")
                registers["c"] += 1
            case _:
                print("invalid register")
        instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "dec":
        print("decrement")
        match instructions[instruction][3]:
            case "a":
                print("register a")
                registers["a"] -= 1
            case "b":
                print("register b")
                registers["b"] -= 1
            case "c":
                print("register c")
                registers["c"] -= 1
            case _:
                print("invalid register")
        instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jez":
        print("jump if zero")
        if registers[instructions[instruction][3]] == 0:
            instruction = int(instructions[instruction][4:]) - 1
        else:
            instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jnz":
        print("jump if not zero")
        if registers[instructions[instruction][3]] != 0:
            instruction = int(instructions[instruction][4:]) - 1
        else:
            instruction += 1
        print(registers)

    elif instructions[instruction][:3] == "jmp":
        print("jump")
        instruction = int(instructions[instruction][3:]) - 1
        print(registers)

    elif instructions[instruction][0] == "hlt":
        print("halt")
        running = False
        print(registers)

    else:
        print("invalid instruction")
        running = False
        print(registers)

    if instruction > len(instructions) - 1:
        running = False
        print(registers)
        

print(registers)
