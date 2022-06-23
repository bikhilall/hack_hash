import datetime
from hashlib import sha256
from itertools import count

class Cell:
    total_cells = 0
    cell_by_id = {}

    def __init__(self):
        self.value = 0
        self.data = 0
        self.prediction = 0
        self.error = 0
        self.id = self.total_cells
        self.childern = []
        
        Cell.total_cells += 1
        Cell.cell_by_id[self.id] = self
        print(f"created cell with id {self.id}")

    def predict(self, data):
        self.data = data
        self.error = self.prediction - self.data
        if not data: return 0
        if data & 1:
            self.value = 1
            self.prediction = self.get_child(1).predict(data >> 1)
            
        else:
            self.value = 0
            self.prediction = self.get_child(0).predict(data << 1)
        
    def get_child(self, child_index):
        while len(self.childern)<=child_index:
            self.childern.append(Cell())
        return self.childern[child_index]


ai = Cell()
data = ""

for i in range(9):
    data = int(sha256(str(data).encode('utf-8')).hexdigest(),16)
    ai.predict(data)
    

