from DTtree.Symbol import Symbol


class NotTerminal(Symbol):
    def __init__(self, name, size):
        super().__init__(name)
        # print(name)
        self.size = size
        self.childs = []

    def add(self, symbol):
        self.childs.append(symbol)

    def dotStr(self):
        s = " " + self.dotName() + "[label=\"" + self.name + "\"];\n"
        for i in range(0, len(self.childs)):
            # print("I", i)
            # try:
            #     # print("TM",len(self.childs[i]))
            # except Exception:
            #     # print("fail")
            s += "    " + self.dotName() + "->" + self.childs[i].dotName() + ";\n"
            s += self.childs[i].dotStr()
            # print(len(self.childs[i].childs),"SIZE")
        return s
