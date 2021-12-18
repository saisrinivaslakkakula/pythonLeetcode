class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertEnd(self,datalist:list=[])->Node:
        node1 = Node(datalist[0])
        self.head = node1 #point head and tail to starting element of the list
        self.tail = node1
        i=1
        while(i<len(datalist)): # traverse through the array
            node = Node(datalist[i]) # create new node for every element
            self.tail.next = node # current tail's next must point to new node address,
                                    # this appends new node to the end
            self.tail = node # current tail must updated to newly inserted node at the end
            i+=1
        return self.head
    def insertBegin(self,datalist:list=[])->Node:
        node1 = Node(datalist[0])
        self.head = node1  # point head and tail to starting element of the list
        self.tail = node1
        i = 1
        while (i < len(datalist)):  # traverse through the array
            node = Node(datalist[i])  # create new node for every element
            node.next = self.head  # newly created node's next must be head
            # this appends new node in the beginning of the list
            self.head = node  # head must be updated
            i += 1
        return self.head




singleLinkedList = singleLinkedList()
dataList = [1, 2, 3, 4, 5,6,7]
#sllhead = singleLinkedList.insertEnd(dataList)
sllhead = singleLinkedList.insertBegin(dataList)


while(sllhead!=None):
    print(sllhead.value)
    sllhead = sllhead.next

