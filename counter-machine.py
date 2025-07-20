import csv
import sys

running = True
instructions = []
instruction = 0
length_instructions = 0
registers = {
    "a": 0,
    "b": 0,
    "c": 0,
    "d": 0
}
output = []

with open(sys.argv[1], newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        instructions.extend(row)

try:
    while True:
        stripped_instruction = instructions[instruction].replace(" ","")
        if stripped_instruction[:3] == "inc":
            print(instructions[instruction])
            registers[stripped_instruction[3]] += 1
            instruction += 1
            print(registers)
            print(stripped_instruction[:3])
    
        elif stripped_instruction[:3] == "dec":
            print(instructions[instruction])
            registers[stripped_instruction[3]] -= 1
            instruction += 1
            print(registers)
            print(stripped_instruction[:3])
    
        elif stripped_instruction[:3] == "jez":
            print(instructions[instruction])
            if registers[stripped_instruction[3]] == 0:
                print("jumped")
                instruction = int(stripped_instruction[4:]) - 1
            else:
                instruction += 1
            print(registers)
            print(stripped_instruction[:3])
    
        elif stripped_instruction[:3] == "jnz":
            print(instructions[instruction])
            if registers[stripped_instruction[3]] != 0:
                print("jumped")
                instruction = int(stripped_instruction[4:]) - 1
            else:
                instruction += 1
            print(registers)
            print(stripped_instruction[:3])
    
        elif stripped_instruction[:3] == "out":
            print(instructions[instruction])
            output.append(registers[stripped_instruction[3]])
            instruction += 1
            print(registers)
            print(output)
    
        else:
            print("invalid instruction")
            running = False
            print(registers)
            print(output)
    
        if instruction > len(instructions) - 1:
            running = False
            print(registers)
            print(stripped_instruction[:3])
    
        try:
            if sys.argv[2] == "debug":
                input("")
        except IndexError:
            pass
except KeyboardInterrupt:
    print("")
    print("-------")
    print("STOPPED")
    print("-------")
    print("")
    print("Registers: " + str(registers))
    print("Output: " + str(output))
