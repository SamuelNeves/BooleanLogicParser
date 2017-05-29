from ASTTree.Expr import Expr


class Oper(Expr):
    def __init__(self, esq, dir, name):
        super().__init__()
        self.esq = esq
        self.dir = dir
        self.name = name

    def toDot(self):
        print("Entroutodot")
        s = "   " + str(self.id) + " [label=\"" + str(self.getOperName()) + "\"];\n"
        s += "   " + str(self.id) + " -> " + str(self.esq.id) + "; \n"
        s += "   " + str(self.id) + " -> " + str(self.dir.id) + "; \n"
        s += self.esq.toDot()
        s += self.dir.toDot()
        return s

    def getOperName(self):
        return self.name
