class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.length -= 1
        return temp

    def print_items(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

my_stack = Stack(3)
my_stack.push(2)
my_stack.push(5)
my_stack.push(10)
my_stack.pop()
my_stack.push(89)
my_stack.print_items()
