class Towel: 
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def dry(self, amount: int):
        self.wetness += amount
        if self.wetness > self.getMaxWetness():
            print("Toalha enchargada")
            self.wetness = self.getMaxWetness()

    def wrintOut(self):
        self.wetness = 0

    def getMaxWetness(self) -> int:
        if self.size == "P":
            return 10
        if self.size == "M":
            return 20 
        if self.size == "G":
            return 30
        return 0