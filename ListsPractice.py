class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertEnd(self, datalist: list = []) -> Node:
        node1 = Node(datalist[0])
        self.head = node1  # point head and tail to starting element of the list
        self.tail = node1
        i = 1
        while i < len(datalist):  # traverse through the array
            node = Node(datalist[i])  # create new node for every element
            self.tail.next = node  # current tail's next must point to new node address,
            # this appends new node to the end
            self.tail = node  # current tail must updated to newly inserted node at the end
            i += 1
        return self.head

    def insertBegin(self, datalist: list = []) -> Node:
        node1 = Node(datalist[0])
        self.head = node1  # point head and tail to starting element of the list
        self.tail = node1
        i = 1
        while i < len(datalist):  # traverse through the array
            node = Node(datalist[i])  # create new node for every element
            node.next = self.head  # newly created node's next must be head
            # this appends new node in the beginning of the list
            self.head = node  # head must be updated
            i += 1
        return self.head

    def traverseSingleLinkedList(self, head: Node):
        while (head != None):
            print(head.value)
            head = head.next
    def searchinTheList(self,val:int,head:Node)->Node:
        while(head!=None):
            if head.value == val:
                return head
            head = head.next
        return None
    def deleteElemntinMiddleOfList(self,head:Node,val:int):
        while head.next!=None:
            #print(head.next.value)
            if head.next.value == val:
                #print("Found here!!")
                RemovalNode:Node = head.next
                head.next = head.next.next
                RemovalNode.next = None
            head = head.next


class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def insertEnd(self, datalist: list = []) -> Node:
        # *** Refer to DLL_insert_End.jpeg for more clarification *** #
        if len(datalist) ==0 : return None
        node1 = Node(datalist[0]) # create an initial node and point it's head and tail to this node
        self.head = self.tail = node1
        node1.next = self.head # in DLL, current node's next will always point to head
        i=1
        while(i<len(datalist)):
            new_node = Node(datalist[i])  #create the new node with data
            self.tail.next = new_node # tail is end og DLL; however pointing to head. we need to cut the link of tail
               # which is pointing to head. that link must be established to the new node created.
            new_node.next = self.head # newly created node's next must be pointed to head to complete circular property
            self.tail = new_node # to keep tack of last inserted node, the tail must be updated to new node's address
            i+=1
        return self.head
    def traveseDoubleLinkedList(self,head:Node):
        headptr = head
        while head.next!=headptr:
            print(head.value)
            head = head.next



doublyLinkedList = doublyLinkedList()
dataList = [1, 2, 3, 4, 5, 6, 7]
dllhead= doublyLinkedList.insertEnd(dataList)
doublyLinkedList.traveseDoubleLinkedList(dllhead)
