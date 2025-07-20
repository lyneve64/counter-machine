# Counter Machine

## Usage
### Running a program
python main.py [FILE] (debug|nothing)
passing debug makes it run step by step, requiring you to press enter to go to the next instruction, leaving it empty (or passing anything besides debug) will cause it to run normally

Ctrl + C to exit

### Listing a program's instructions
python list.py [FILE]

## Instruction Set
(Based off of the Minsky instruction set)
- inc(register): Increment register
- dec(register): Decrement register
- jez(register)(line): Jump to line if register == 0
- jnz(register)(line): Jump to line if register != 0
- out(register): Adds the current value of register to a list, which outputs upon program end

## What will I need to achieve this
### Basic Functionality:
- [X] Reading files
- [X] Interpreting and executing instructions from read files
- [X] Returning output
- [X] Halt automatically at end of program
### Q.O.L:
- [X] Stepping through instructions
