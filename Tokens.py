class Tokens:
    def __init__(self, listOfTokens):
        self.index = 0
        self.maxIndex = len(listOfTokens) - 1
        self.listOfTokens = listOfTokens

    def value(self):
        if self.index <= self.maxIndex:
            return self.listOfTokens[self.index].value

    def token(self):
        if self.index <= self.maxIndex:
            return self.listOfTokens[self.index].type
        else:
            return "EOF"

    def advance(self):
        self.index += 1

    def look(self, tk):
        if tk == self.listOfTokens[self.index].type:
            return True
        else:
            return False

    def match(self, tk):
        print(self.listOfTokens[self.index].type)
        if tk == self.listOfTokens[self.index].type:
            self.advance()
            return True
        else:
            return False

    def lookAny(self, tkList):
        for element in tkList:
            if element == self.listOfTokens[self.index].type:
                return True
