class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,end='--->')
                n = n.ref
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node
    def add_after_gvn_node(self,data,data1):
        n = self.head
        while n.ref is not None:
            if n.data == data:
                break
            n = n.ref
        if n is None:
            print('node not found')
        else:
            new_node = Node(data1)
            new_node.ref = n.ref
            n.ref = new_node
    def add_before_gvn_node(self,data,data1):
        if self.head is None:
            print('Linked List is empty')
            return
        if self.head.data == data:
            new_node = Node(data1)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == data:
                break
            n = n.ref
        if n.ref is None:
            print('Node not found')
        else:
            new_node = Node(data1)
            new_node.ref = n.ref
            n.ref = new_node
    def del_first_node(self):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            self.head = self.head.ref
    def del_last_node(self):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            n = self.head
            while (n.ref).ref is not None:
                n = n.ref
            n.ref = n.ref.ref
    def del_given_node(self,data):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            n = self.head
            while n.ref.data != data:
                n = n.ref
            n.ref = n.ref.ref




a = LinkedList()
a.add_begin(10)
a.add_end(20)
a.add_end(30)
a.add_after_gvn_node(10,15)
a.add_before_gvn_node(15,12)
#a.del_first_node()
#a.del_last_node()
a.del_given_node(15)
a.printLL()

