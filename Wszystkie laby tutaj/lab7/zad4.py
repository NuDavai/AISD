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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


ONP = "73+52-2^*="
ONP = list(ONP)
kolejka=Stack()
for i in range(len(ONP)):
    x=ONP[i]
    if x=='+':
        a=int(kolejka.pop())
        b=int(kolejka.pop())
        c=b+a
        kolejka.push(c)
    elif x=='-':
        a=int(kolejka.pop())
        b=int(kolejka.pop())
        c=b-a
        kolejka.push(c)
    elif x=='*':
        a=int(kolejka.pop())
        b=int(kolejka.pop())
        c=b*a
        kolejka.push(c)
    elif x=='/':
        a=int(kolejka.pop())
        b=int(kolejka.pop())
        c=b/a
        kolejka.push(c)
    elif x=='^':
        a=int(kolejka.pop())
        b=int(kolejka.pop())
        c=b**a
        kolejka.push(c)
    elif x.isnumeric():
        kolejka.push(x)
    elif x == '=':
        print(kolejka.pop())