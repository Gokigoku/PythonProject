import sys
class Stack:
    def __init__(self):
        self.stack=[]
        self.max=5
    def is_empty(self):
        return self.stack==[]
    def insert(self,data):
        if len(self.stack)==self.max:
            print("Stack is Full i.e Stack Overflow")
        else:
            self.stack.append(data)
    def delet(self):
        if self.is_empty():
            print("Unable to delete i.e Stack Underflow")
        else:
            print("Delted item is ",self.stack.pop())
    def getsize(self):
        print("Stack size is ",len(self.stack))
    def display(self):
        print("Stack consist of :")
        for s in self.stack:
            print(s ,end=' ')
    def search(self):
        s=int(input("Enter the element to be search: "))
        for t in self.stack:
            if t==s:
                print("Element Found")
                break
        else:
            print("Item not Found")
stack=Stack()
while True:
    print("\n-----Stack Menu-----\n 1.push\n 2.pop\n 3.size\n 4.display\n 5.search\n 6.Exit")
    try:
        ch = int(input("Enter your choice: "))
    except:
        print("Invalid input")
    if ch==1:
        data=int(input("Enter the item to be insert: "))
        stack.insert(data)
    if ch==2:
        stack.delet()
    if ch==3:
        stack.getsize()
    if ch==4:
        stack.display()
    if ch==5:
        stack.search()
    if ch==6:
        sys.exit()


