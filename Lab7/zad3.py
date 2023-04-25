# BLAD JAKIS WYWALA, TRZEBA SPRAWDZIC

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return  self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

nawiasy_raw="{[()]}"
nawiasy=list(nawiasy_raw)
flagaW=True
flagaO=True
flagaK=True
sW=Stack()
so=Stack()
sK=Stack()
for i in range(len(nawiasy)):
    if nawiasy[i] == '(':
        so.push('(')
    elif nawiasy[i] == ')':
        if so.isEmpty():
            flagaO=False
            print("za dużo nawiasów zamykających okraglych, nie jest ok")
    if nawiasy[i] == '{':
        sW.push('{')
    elif nawiasy[i] == '}':
        if sW.isEmpty():
            flagaW=False
            print("za dużo nawiasów zamykających klamrowych, nie jest ok")
    if nawiasy[i] == '[':
        sK.push('[')
    elif nawiasy[i] == ']':
        if sK.isEmpty():
            flagaK=False
            print("za dużo nawiasów zamykających kwadratowych, nie jest ok")
if so.isEmpty() and flagaO:
    print("Jest git, nawiasy okrągłe ok")
else:
    print("Coś poszło nie tak (nawiasy okrągłe)")
if sW.isEmpty() and flagaW:
    print("Jest git, nawiasy klamrowe ok")
else:
    print("Coś poszło nie tak (nawiasy klamrowe)")
if sK.isEmpty() and flagaK:
    print("Jest git, nawiasy kwadratowe ok")
else:
    print("Coś poszło nie tak (nawiasy kwadratowe)")