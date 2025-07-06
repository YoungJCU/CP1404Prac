"""
CP1404 prac
time prediction: 30
practical:
"""
class ProgrammingLanguage:
    def __init__(self,name,typing,reflection,year=int):
        self.name=name
        self.typing=typing
        self.reflection=reflection
        self.year=year

    def is_dynamic(self):
        return self.typing=="Dynamic"