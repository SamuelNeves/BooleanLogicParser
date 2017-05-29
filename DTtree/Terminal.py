from DTtree.Symbol import Symbol


class Terminal(Symbol):

    def __init__(self, name):
        super().__init__(name)
        print(name)

    def dotStr(self):
        return "    " + self.dotName() + (" [label=\"" + self.name + "\"];\n")
