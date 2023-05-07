from StackExample import Stack

def parChacker(SymbolString):
    s = Stack()
    index = 0
    balanced = True
    while index < len(SymbolString) and balanced:
        symbol = SymbolString[index]
        if symbol in "({[<":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and s.isEmpty():
        return True
    else:
        return False

def matches(open, close):
    opens = "({[<"
    closes = ")}]>"
    return opens.index(open) == closes.index(close)

print(parChacker("()()()()"))
print(parChacker("(((((())))()()())("))
print(parChacker("()(())"))
print(parChacker("({[<>]})"))
print(parChacker("({[])>"))