import pickle
class Memory():
    def __init__(self, memory_file_name):
        MEMORY_SIZE = 4096
        self.memory = [0] * MEMORY_SIZE
        self.memory_file_name = memory_file_name

    def save_to_file(self):
        with open(self.memory_file_name, "wb") as file:
            pickle.dump(self.memory, file)

    def load_from_file(self):
        with open(self.memory_file_name, "rb") as file:
            self.memory = pickle.load(file)


    def __getitem__(self, index):
        return self.memory[index]
    def __setitem__(self, index, value):
        self.memory[index] = value

    def _print_self(self):
        return str(self.memory)

    def __repr__(self):
        return self._print_self()
    def __str__(self) -> str:
        return self._print_self()