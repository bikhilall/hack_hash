import datetime
from hashlib import sha256

class Cell:
    def __init__(self) -> None:
        pass

    def predict(self, data):
        print(data)


ai = Cell()
data = ""

for i in range(9):
    data = sha256(str(data).encode('utf-8')).hexdigest()
    ai.predict(data)
    

