from ASTTree.Expr import Expr


class Var(Expr):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def toDot(self):
        return "    " + str(self.id) + " [label=\"" + str(self.name) + "\"] ; \n"

