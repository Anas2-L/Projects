class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    
    def printlist(self):
        tempo=self.head
        while(tempo):
            print(tempo.data)
            tempo=tempo.next

    def reversell(self):
        prev=None
        current=self.head
        while(current!=None):
            next=current.next
            current.next=prev
            prev=current
            current=next
        
        self.head=prev

    

linkl=Linkedlist()
linkl.push(55)
linkl.push(75)
linkl.push(95)
linkl.push(105)

print("original linked list\n")
linkl.printlist()

linkl.reversell()

print("\nReversed linked list\n")
linkl.printlist()