from instruction import Instruction
from memory import Memory
from variable import Variable
import copy
class Parser:
    def __init__(self, file_handle, memory_file_name='memory.memory'):
        self.file = file_handle
        self.instructions = []
        self.variables = []
        self.memory = Memory(memory_file_name)

        self.parse()

        self.get_all_vars()


        #we need to get length of whole program and then set the memory addresses of the variables
        self.set_memory_addresses_vars()


        self.link_instructions_to_vars()
        #link all variables to the instructions

        #now we can compile the instructions to memory
        self.compile_to_memory()
        self.memory.save_to_file()


    def link_instructions_to_vars(self):
        for instruction in self.instructions:
            argument = instruction.arg
            for variable in self.variables:
                if variable.varname == argument:
                    instruction.link_instruction_to_var(variable)


    def set_memory_addresses_vars(self):
        for i, variable in enumerate(self.variables):
            variable.set_location(len(self.instructions)+i)


    def compile_to_memory(self):
        for index, instruction in enumerate(self.instructions):
            self.memory[index] = instruction.convert_instruction_to_int()

    def parse(self):        
        for line in self.file:
            command = line.strip().split(' ') # get instruction and arguments as list
            instruction = command[0] 
            arg = None
            try:
                arg = command[1] # if there is an argument then get it
            except IndexError:
                arg = None

            inst = Instruction(instruction, arg) # create instruction
            self.instructions.append(inst)

    def get_all_vars(self):
        # get all variables in the program 
        # they are defined by the instructon Define X
        # Default value is 0
        instructions = copy.deepcopy(self.instructions)
        indicies_to_delete = []
        for i, instruction in enumerate(instructions):
            if instruction.instruction == "Define":
                varname = instruction.arg
                self.variables.append(Variable(varname))
                indicies_to_delete.append(i)

        for i in sorted(indicies_to_delete, reverse=True):
            del self.instructions[i]



