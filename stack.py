class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Stack is empty. Cannot pop.")

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("Stack is empty. Cannot peek.")

# Example usage
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.stack)  # Output: Stack: [10, 20, 30]

try:
    print("Peek:", stack.peek())  # Output: Peek: 30
    print("Pop:", stack.pop())    # Output: Pop: 30
except IndexError as e:
    print(e)

print("Stack after pop:", stack.stack)  # Output: Stack after pop: [10, 20]

print("Is stack empty?", stack.is_empty())  # Output: Is stack empty? False

