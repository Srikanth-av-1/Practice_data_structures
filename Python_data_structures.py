class Node:
    def __init__(self,data):
        self.data = data
        self.pref = None
        self.nref = None
class doublyLinkedList:
    def __init__(self):
        self.head = None
    def printLL(self):
        if self.head is None:
            print('Linked list is empty')
        else:
            n = self.head
            while n is not None:
                print(n.data,end='--->')
                n = n.nref
    def print_reverse(self):
        print()
        if self.head is None:
            print('Linked List is empty')
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data,end='<---')
                n = n.pref
    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.nref = self.head
            #new_node.nref.pref = new_node
            self.head = new_node
        else:
            new_node.nref = self.head
            new_node.nref.pref = new_node
            self.head = new_node
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.nref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n
    def add_after_gvn_node(self,data,data1):
        n = self.head
        while n.nref is not None:
            if n.data == data:
                break
            n = n.nref
        if n is None:
            print('node not found')
        else:
            new_node = Node(data1)
            new_node.nref = n.nref
            n.nref.pref = new_node
            new_node.pref = n
            n.nref = new_node
    def add_before_gvn_node(self,data,data1):
        if self.head is None:
            print('Linked List is empty')
            return
        if self.head.data == data:
            new_node = Node(data1)
            new_node.nref = self.head
            self.head.pref = new_node
            self.head = new_node
            return
        n = self.head
        while n.nref is not None:
            if n.nref.data == data:
                break
            n = n.nref
        if n.nref is None:
            print('Node not found')
        else:
            new_node = Node(data1)
            new_node.nref = n.nref
            n.nref.pref = new_node
            n.nref = new_node
            new_node.pref = n
    def del_first_node(self):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            self.head = self.head.nref
            self.head.nref.pref = self.head

    def del_last_node(self):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            n = self.head
            while n.nref.nref is not None:
                n = n.nref
            n.nref = n.nref.nref
            #n.nref.pref = n
    def del_given_node(self,data):
        if self.head is None:
            print('Linked List is empty deletion not possible')
        else:
            n = self.head
            while n.nref.data != data:
                n = n.nref
            n.nref = n.nref.nref
            n.nref.pref = n





a = doublyLinkedList()
a.add_begin(50)
a.add_begin(40)
a.add_begin(30)
a.add_end(60)
a.add_after_gvn_node(30,35)
a.add_before_gvn_node(50,45)
a.del_last_node()
a.del_given_node(40)
a.printLL()
a.print_reverse()

