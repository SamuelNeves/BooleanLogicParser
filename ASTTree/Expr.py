class Expr:
    count = 0

    def __init__(self):
        self.id = Expr.count
        Expr.count += 1

