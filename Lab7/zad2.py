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

nawiasy_raw="(((()))))"
nawiasy=list(nawiasy_raw)
s=Stack()
flaga=True
for i in range(len(nawiasy)):
    if nawiasy[i]=='(':
        s.push('(')
    elif nawiasy[i]==')':
        if s.isEmpty():
            flaga=False
            print("za dużo nawiasów zamykających, nie jest ok")
        else: s.pop()
if s.isEmpty() and flaga:
    print("Jest git, wszystko dobrze poszło")
else:
    print("Coś poszło nie tak")