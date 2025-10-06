class Towel: 
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20
        if self.size == "G":
            return 30
        return 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("Toalha enchargada")
            self.wetness = self.getMaxWetness()

    def wringOut(self):
        self.wetness = 0

    def isDry(self) -> bool:
        return self.wetness == 0
    
    def show(self):
        print(self)

    def __str__(self) -> str:
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"
    
toalha = Towel("Azul", "G")
toalha.show()
toalha.dry(10)
toalha.show()
print(toalha.isDry())
toalha.dry(10)
toalha.show
toalha.wringOut()
toalha.show()
