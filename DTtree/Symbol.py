class Symbol:
    count = 0

    def __init__(self, name):
        self.name = name
        self.id = Symbol.count
        Symbol.count += 1

    def dotName(self):
        return "no" + str(self.id)
