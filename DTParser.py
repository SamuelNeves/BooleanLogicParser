from LexerAnalyser import LexerAnalyser
from Tokens import Tokens
from DTtree.NotTerminal import NotTerminal
from DTtree.Terminal import Terminal
from Utils import Utils
import sys


def E(tokens):
    s = NotTerminal("E", 2)
    s.add(T(tokens))
    s.add(E1(tokens))
    return s


def E1(tokens):
    if tokens.match("IMPLIES"):
        print("AND")
        s = NotTerminal("E1", 3)
        s.add(Terminal("->"))
        s.add(T(tokens))
        s.add(E1(tokens))
        return s
    elif tokens.lookAny(["CLOSEP", "eof"]):
        s = NotTerminal("E1", 1)
        s.add(Terminal("lambda"))
        return s
    else:
        print("Token inesperado  na entrada.")
        sys.exit(1)
        return None


def T(tokens):
    s = NotTerminal("T", 2)
    s.add(F(tokens))
    s.add(T1(tokens))
    return s


def T1(tokens):
    if tokens.match("AND"):
        s = NotTerminal("T1", 3)
        s.add(Terminal("AND"))
        s.add(F(tokens))
        s.add(T1(tokens))
        return s
    elif tokens.match("OR"):
        s = NotTerminal("T1", 3)
        s.add(Terminal("OR"))
        s.add(F(tokens))
        s.add(T1(tokens))
        return s
    elif tokens.lookAny(["IMPLIES", "CLOSEP", "NOT", "eof"]):
        s = NotTerminal("T1", 1)
        s.add(Terminal("lambda"))
        return s
    else:
        print("Token inesperado  na entrada.")
        sys.exit(1)
        return None


def F(tokens):
    ant = tokens.value()
    if tokens.match("VAR"):
        s = NotTerminal("F", 1)
        s.add(Terminal(ant))
        return s
    elif tokens.match("OPENP"):
        exp = E(tokens)
        if tokens.match("CLOSEP"):
            s = NotTerminal("F", 3)
            s.add(Terminal("("))
            s.add(exp)
            s.add(Terminal(")"))
            return s
        else:
            print("Token inesperado: Esperado ) lido" + tokens.token())
    elif tokens.match("NOT"):
        exp = F(tokens)
        s = NotTerminal("F", 2)
        s.add(Terminal("!"))
        s.add(exp)
        return s
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
    Utils.writeInFile(tree.dotStr())
    print("=D")


if __name__ == "__main__":
    main(sys.argv[1:])
