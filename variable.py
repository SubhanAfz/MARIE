class Variable:
    def __init__(self, varname):
        self.varname = varname
        self.location = None

    def set_location(self, location):
        self.location = location

    def _print_self(self):
        return f'{self.varname}: location: {self.location}'

    def __repr__(self):
        return self._print_self()
    def __str__(self) -> str:
        return self._print_self()
    

