class MaxStack:

    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val > self.max_stack[-1]:
            self.max_stack.append(val)
        else:
            self.max_stack.append(self.max_stack[-1])

    def pop(self):
        if self.max_stack:
            self.max_stack.pop()

        return self.stack.pop()

    def max(self):
        return self.max_stack[-1]
