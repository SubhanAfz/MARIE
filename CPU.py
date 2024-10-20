import sys
from memory import Memory

class CPU:
    def __init__(self, memory_file_name):
        self.memory = Memory(memory_file_name)
        self.memory.load_from_file()
        self.AC = 0
        self.PC=0
        self.IR =0
        self.MAR = 0
        self.MBR = 0
        self.IN =0
        self.OUT=0
        self.running=True
    def fetch(self):
        self.MAR = self.PC
        self.MBR = self.memory[self.MAR]
        self.IR = self.MBR
        self.PC += 1
        
    def decode_execute(self):
        opcode = self.IR >> 12
        addr = self.IR & 0xFFF

        # Execute the instruction based on the opcode
        if opcode == 1:
            self.load(addr)
        elif opcode == 2:
            self.store(addr)
        elif opcode == 3:
            self.add(addr)
        elif opcode == 4:
            self.subt(addr)
        elif opcode == 5:
            self.input()
        elif opcode == 6:
            self.output()
        elif opcode == 7:
            self.halt()
        elif opcode == 8:
            self.skipcond(addr)
        elif opcode == 9:
            self.jump(addr)

    def load(self,addr):
        self.MAR = addr
        self.MBR = self.memory[self.MAR]
        self.AC = self.MBR
        

    def store(self,addr):
        self.MAR =addr
        self.MBR = self.AC
        self.memory[self.MAR] = self.MBR


    def add(self,addr):
        self.MAR =addr
        self.MBR = self.memory[self.MAR]
        self.AC += self.MBR


    def subt(self,addr):
        self.MAR =addr
        self.MBR = self.memory[self.MAR]
        self.AC -= self.MBR

    def input(self):
        self.AC = int(input("Enter a number to store in AC, decimal format: "))

    def output(self):
        print(f'AC: {self.AC}')

    def halt(self):
        self.running=False

    def skipcond(self, condition):
        if condition ==0:
            if self.AC <0:
                self.PC +=1
        if condition ==1024:
            if self.AC ==0:
                self.PC +=1
        if condition == 2048:
            if self.AC >0:
                self.PC +=1


    def jump(self,addr):
        self.MAR = addr
        self.MBR = self.memory[self.MAR]
        self.PC = self.MBR

    def run(self):
        self.running=True
        while self.running:
            self.fetch()
            self.decode_execute()



file_name = sys.argv[1]


MARIE = CPU(f'{file_name}')

MARIE.run()