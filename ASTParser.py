from LexerAnalyser import LexerAnalyser
from Tokens import Tokens
from Utils import Utils
import sys
from ASTTree.Oper import Oper
from ASTTree.Var import Var
from ASTTree.Not import Not


def E(tokens):
    return E1(tokens, T(tokens))


def E1(tokens, esq):
    ant = tokens.value()
    if tokens.match("IMPLIES"):
        dir = T(tokens)
        m = Oper(esq, dir, "->")
        return E1(tokens, m)
    elif tokens.lookAny(["CLOSEP", "eof"]):
        return esq
    else:
        print("Token inesperado  na entrada.")
        sys.exit(1)
        return None


def T(tokens):
    return T1(tokens, F(tokens))


def T1(tokens, esq):
    if tokens.match("AND"):
        dir = F(tokens)
        m = Oper(esq, dir, "AND")
        return T1(tokens, m)
    elif tokens.match("OR"):
        dir = F(tokens)
        m = Oper(esq, dir, "OR")
        return T1(tokens, m)
    elif tokens.lookAny(["IMPLIES", "CLOSEP", "NOT", "eof"]):
        return esq
    else:
        print("Token inesperado  na entrada.")
        sys.exit(1)
        return None


def F(tokens):
    ant = tokens.value()
    if tokens.match("VAR"):
        return Var(ant)
    elif tokens.match("OPENP"):
        exp = E(tokens)
        if tokens.match("CLOSEP"):
            return exp
        else:
            print("Token inesperado: Esperado ) lido" + tokens.token())
    elif tokens.match("NOT"):
        exp = Not(F(tokens))
        # s = NotTerminal("F", 2)
        # s.add(Terminal("!"))
        # s.add(exp)
        return exp
    else:
        print("Token Inesperado")
        sys.exit(1)


def main(argv):
    try:
        nameOfFile = argv[-1]
    except IndexError:
        nameOfFile = "input.txt"
    contentOfFile = Utils.loadStringFromFile(nameOfFile)
    lexerAnalyser = LexerAnalyser(contentOfFile)
    listOfTokens = lexerAnalyser.returnListOfTokens()
    tokens = Tokens(listOfTokens)
    tree = E(tokens)
    print(tree.esq.name)
    # print(tree.toDot())
    Utils.writeInFile(tree.toDot())
    print("=D")


if __name__ == "__main__":
    main(sys.argv[1:])
