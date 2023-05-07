from StackExample import Stack

def onp(SymbolString):
    s = Stack()
    index = 0
    while index < len(SymbolString):
        symbol = SymbolString[index]
        if symbol.isdigit() == True:
            s.push(symbol)

        elif symbol == "+" or symbol == "-" or symbol == "/" or symbol == "*":
            a = str(s.peek())
            s.pop()
            b = str(s.peek())
            s.pop()
            c = eval(b+symbol+a)
            s.push(c)

        elif symbol == "^":
            symbol = "**"
            a = str(s.peek())
            s.pop()
            b = str(s.peek())
            s.pop()
            c = eval(b+symbol+a)
            s.push(c)

        elif symbol == "=":
            return s.peek()
        index += 1

print(onp( "7 3 + 5 2 - 2 ^ * =" ))



