class Field:
    def __init__(self) -> None:
        self.filename = "logic/field.txt"
        self.field = []
        with open(self.filename) as f:
            data = f.read().split()
            self.field = [None] * len(data)
            for index, value in enumerate(data):
                self.field[index] = list(map(int, value))
                
    def get(self) -> list:
        return self.field

if __name__ == "__main__":
    f = Field()
    print(f.get())
