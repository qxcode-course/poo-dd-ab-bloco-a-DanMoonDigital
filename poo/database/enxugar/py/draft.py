class Towel:
    def __int__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("Toalha encharcada")
            self.wetness = self.getMaxWetness()

    def writngOut(self):
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size =="G":
            return 30
        return 0
    
    def _str__(self) -> str:
        return f"Cor:{self.color}, Tam: {self.size}", Umidade: {self.wetness}"

def main():
    toalha = towel("", "")
    while True:
        print("$", end="")
        line: str = input()
        args: list[str] = line.split(" ")