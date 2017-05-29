import PLY.lex as lex
import sys

class LexerAnalyser:
    def __init__(self, inputString):
        tokens = ['IMPLIES', 'OR', 'AND', 'NOT', 'VAR', 'TRUE', 'FALSE', 'OPENP', 'CLOSEP']
        t_IMPLIES = r'\→'
        t_OR = r'\∨'
        t_AND = r'\∧'
        t_NOT = r'\¬'
        t_VAR = r'[a-z][a-zA-Z0-9_]*'
        t_TRUE = r'T'
        t_FALSE = r'F'
        t_OPENP = r'\('
        t_CLOSEP = r'\)'

        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            sys.exit(1)
            t.lexer.skip(1)

        def t_eof(t):
            self.eof = t

        self.lex = lex
        self.lex.lex()
        self.lex.input(inputString)

    def nextToken(self):
        tok = self.lex.token()
        return tok

    def returnListOfTokens(self):
        listOfTokens = []
        token = self.nextToken()
        while token:
            listOfTokens.append(token)
            token = self.nextToken()
        listOfTokens.append(self.eof)
        return listOfTokens
