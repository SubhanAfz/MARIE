
# MARIE Emulator

[subhan.work](https://subhan.work)

The **MARIE** Emulator is a Python3 based simulation of the **MARIE** architecture (**M**achine **A**rchitecture that is **R**eally **I**ntuitive and **E**asy)

This also includes an assembler which creates the binary files for the **MARIE** Emulator

Instruction set:

Load X - load contents of variable X into the Accumulator

Store X - stores the contents of the accumulator at the variable X

Add X - adds contents of variable X to AC

Subt X - subtracts contents of variable X from AC

Input - Input a value from input device into AC

Output - Outputs the value from AC

Halt - Terminates program

Skipcond X(Condition var) - Skips next instruction on condition. 

When condition var is 0, it skips if accumulator is less than 0

When condition var is 1024, it skips if accumulator is equal to 0

When condition var is 2048, it skips if accumulator is more than 0

Jump X - Loads value of variable X into PC

Define X - Defines a variable at the end of the program (more of an assembler instruction, doesnt run on runtime, only when assembled. )

To assemble a program:

Windows:
python build.py [MARIE instructions] [Binary file]

Linux:
python3 build.py [MARIE instructions] [Binary file]

To run the program:

Windows:
python CPU.py [Binary file]

Linux:
python3 CPU.py [Binary file]
