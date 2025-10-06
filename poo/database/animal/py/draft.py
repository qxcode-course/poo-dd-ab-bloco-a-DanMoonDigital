class Animal:
    def __init__(self, species: str, sound: str):
        self.species: str = species
        self.sound: str = sound
        self.age: int = 0

        





def main():
    animal = Animal ("", "")
    while True:
        line: str = input ()
        print("$" + line)
        args: list [str] = line.split(" ")