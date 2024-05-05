class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Pilha vazia")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Pilha vazia")
            return None
        
stack = Stack()

stack.push(15)
stack.push(24)
stack.push(25)

print("Topo da pilha: ", stack.peek())
print("Elemento desempilhado:", stack.pop()) 
print("Elemento desempilhado:", stack.pop())  

print("Topo da pilha:", stack.peek())
print("Elemento desempilhado:", stack.pop())
print("Elemento desempilhado:", stack.pop()) 