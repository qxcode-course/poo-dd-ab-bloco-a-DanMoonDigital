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
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"

def main():
    toalha = Towel("", "")
    while True:
        print("$", end="")
        line: str = input()
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args [0] == "new":
            color = args [1]
            size = args [2]
            toalha = Towel(color, size)
        elif args [0] == "show":
            print(toalha)
        elif args [0] == "dry":
            amount = int(args[1])
            toalha.dry(amount)
        else:
            print("fail: comando desconhecido")
main()