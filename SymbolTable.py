class SymbolTable:
    def __init__(self):
        self.table = {}

    def set(self, symbol, attributes):
        self.table[symbol] = attributes

    def get(self, symbol):
        return self.table.get(symbol, None)

    def delete(self, symbol):
        if symbol in self.table:
            del self.table[symbol]

    def display(self):
        for symbol, attributes in self.table.items():
            print(f"{symbol}: {attributes}")