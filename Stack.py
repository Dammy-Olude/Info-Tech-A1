class Stack:
    def __init__(self):
        self.data = []
    def push(self, item):
        '''
        push: Adds an item to the end of the collection
        '''
        self.data.append(item)  #adds an item at the end of the list like a stack would FILO

    def pop(self):
        """
        pop: Removes the last item from the collection and returns it
        """
        return self.data.pop()   #takes the last element of the list out like a stack would FILO
    def peek(self):
        """
        peek: Observes the last item in the collection without removing it
        """
        return self.data[-1]  #observe the last item in the list
    def is_empty(self):
        """
        is_empty: Returns whether the stack is empty or not (boolean)
        """
        if len(self.data) == 0 :   #checks if the length of the list equals 0
            return True  #returns keyword True which stands for boolean 1
        else:
            return False   # returns keyword False which stands for boolean 0


"""
Main
"""
stack = Stack()
print('is_empty:', stack.is_empty())
stack.push('A')
stack.push('B')
stack.push('C')
print('peek:', stack.peek())
print('pop:', stack.pop())
print('peek', stack.peek())
print('is_empty:', stack.is_empty())

