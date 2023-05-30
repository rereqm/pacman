class ScoreCounter:
    def __init__(self, n = 0) -> None:
        self.counter = n
        
    def add(self, x) -> None:
        self.counter += x
        
    def get(self) -> int:
        return self.counter
