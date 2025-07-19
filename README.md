# Counter Machine

## Usage
python main.py [FILE] (debug|nothing)
passing debug makes it run step by step, requiring you to press enter to go to the next instruction, leaving it empty (or passing anything besides debug) will cause it to run normally

## Instruction Set
(Based off of the Minsky instruction set)
- inc(register): Increment register
- dec(register): Decrement register
- jez(register)(line): Jump to line if register == 0
- jnz(register)(line): Jump to line if register != 0
- jmp(line): Jump to line
- hlt: Halts the program

## What will I need to achieve this
### Basic Functionality:
- [X] Reading files
- [X] Interpreting and executing instructions from read files
- [X] Returning output
- [X] Halt automatically at end of program
### Q.O.L:
- [X] Stepping through instructions
