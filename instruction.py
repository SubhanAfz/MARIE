class Instruction:
    def __init__(self, instruction, arg):
        self.instruction = instruction
        self.arg = arg
        self.var = None

    def convert_instruction_to_int(self):
        instruction_map = {
            "Load": 1,
            "Store": 2,
            "Add": 3,
            "Subt": 4,
            "Input": 5,
            "Output": 6,
            "Halt": 7,
            "Skipcond": 8,
            "Jump": 9
        }
        
        # Return the corresponding integer, or a default value (e.g., -1) if not found
        opcode = instruction_map.get(self.instruction, -1)

        if opcode == -1:
            raise ValueError(f"Invalid instruction: {self.instruction}")

        if self.instruction in ["Input", "Output", "Halt"]:
            return opcode << 12

        if self.var is None:
            raise ValueError(f"Invalid {self.instruction} requires a memory addr")
        
        memory_addr = self.var.location
        if memory_addr < 0 or memory_addr > 0xFFF:  # 0xFFF is 4095 in decimal (12 bits)
            raise ValueError(f"Memory address {memory_addr} is out of range")
        
        return (opcode << 12) | memory_addr


        

    def link_instruction_to_var(self, var):
        self.var = var

    def _print_self(self):
        if self.arg is None:
            return f'{self.instruction}'
        else:
            return f'{self.instruction} {self.arg}'
    
    def __repr__(self):
        return self._print_self()
    def __str__(self) -> str:
        return self._print_self()