
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getdata(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


# temp=Node(93)


class unOrderdList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getdata() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getdata() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def remove_ith_node(self, i):
        current = self.head
        previous = None
        count = 0

        while current is not None and count < i:
            previous = current
            current = current.getNext()
            count += 1
        if current is not None:
            if previous is None:
                self.head = current.getNext()
            else:
                previous.setNext(current.getNext())

    def merge_sorted_lists(list1, list2):
        merged_list = unOrderdList()

        current1 = list1.head
        current2 = list2.head

        while current1 is not None and current2 is not None:
            if current1.getdata() > current2.getdata():
                merged_list.add(current1.getdata())
                current1 = current1.getNext()
            else:
                merged_list.add(current2.getdata())
                current2 = current2.getNext()

        while current1 is not None:
            merged_list.add(current1.getdata())
            current1 = current1.getNext()

        while current2 is not None:
            merged_list.add(current2.getdata())
            current2 = current2.getNext()

        return merged_list


list1 = unOrderdList()
list1.add(1)
list1.add(3)
list1.add(5)

list2 = unOrderdList()
list2.add(2)
list2.add(4)
list2.add(6)

merged_list = unOrderdList.merge_sorted_lists(list1, list2)
print(merged_list.size())
current = merged_list.head
while current is not None:
    print(current.getdata())
    current = current.getNext()






