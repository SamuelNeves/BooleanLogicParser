from ASTTree.Oper import Oper


class Or(Oper):
    def __init__(self, esq, dir):
        super().__init__()
        self.esq = esq
        self.dir = dir

    def getOperName(self):
        return "OR"
