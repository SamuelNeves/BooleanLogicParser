from ASTTree.Expr import Expr


class Not(Expr):
    def __init__(self, child):
        super().__init__()
        self.child = child
        self.name = "!"

    def getOperName(self):
        return self.name

    def toDot(self):
        print("Entroutodot")
        s = "   " + str(self.id) + " [label=\"" + str(self.getOperName()) + "\"];\n"
        s += "   " + str(self.id) + " -> " + str(self.child.id) + "; \n"
        s += self.child.toDot()
        return s
