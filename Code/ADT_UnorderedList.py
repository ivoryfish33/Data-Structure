class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newData):
        self.data = newData
    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self,item):
        # O(1)
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        # O(1)
        current = self.head
        count = 0 
        while current != None:
            count = count + 1
            current = current.getNext()
        return count

    def isEmpty(self):
        # O(1)
        if self.head == None:
            return True
        else:
            return False

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() != item:
                current = current.getNext()
            else:
                found = True
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData != item:
                previous = current
                current = current.getNext()
            else:
                found = True
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    
                

# temp = Node(93)
# print(temp.getData())

if __name__ == "__main__":
    mylist = UnorderedList()
    print(mylist.isEmpty())
    mylist.add(31)
    print(mylist.isEmpty())
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    print(mylist.isEmpty())