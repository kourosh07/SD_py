################################################################################################################################################

# کلاس استک

class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def peek(self):
        if len(self.stack) != 0:
            return -1
        else:
            return self.stack[-1]

    def push(self, data):
        if len(self.stack) > self.limit:
            return -1
        else:
            self.stack.append(data)

    def pop(self):

        if len(self.stack) >= 0:
            return self.stack.pop()
        else:
            return -1

    def find(self, data):
        if len(self.stack) <= 0:
            return -1
        for i in range(1, len(self.stack)):
            if self.stack[i] == data:
                return i
        return -1
    def replace(self, data, new_data):
        if len(self.stack) <= 0:
            return -1
        else:
            if data in self.stack:
                self.stack[self.stack.index(data)] = new_data
            else:
                return -1

    def show(self):
        for i in self.stack:
            print(i)

    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)

################################################################################################################################################

# تبدیل دسیمال به باینری

def d2b(number):
    my_stack = Stack()
    while number !=0:
        my_stack.push(number % 2)
        number //= 2
    while not(my_stack.is_empty()):
        print(my_stack.pop(), end='')
        
################################################################################################################################################

# کلاس صف

class Queue:
    def __init__(self, limit=100):
        self.Q = [None] * limit
        self.limit = limit
        self.front = -1
        self.rear = -1

    def enqueue(self, data):
        if self.rear >= self.limit-1:
            return -1
        elif self.front == -1:
            self.front= 0
            self.rear = 0
            self.Q[0] = data
        else:
            self.rear += 1
            self.Q[self.rear] = data
    
    def dequeue(self):
        if self.front == -1:
            return -1
        elif self.rear < self.front:
            return -1
        else:
            self.front += 1

    def show(self):
        for i in range(self.front, self.rear+1):
            print(self.Q[i])
            
    def replace(self, data, place):
        if self.place > self.front and self.place < self.rear:
            self.Q[place] = data

################################################################################################################################################

# کلاس صف حلقوی         

class Cqueue:
    def __init__(self, limit=10) -> None:
        self.Q = [None] * limit
        self.limit = limit
        self.rear = -1
        self.front = -1

    def insert_queue(self, data):
        if (self.rear+1) % self.limit == self.front:
            print('full')
            return -1

        elif self.front == -1:
            self.front += 1
            self.rear += 1
            self.Q[0] = data

        else:
            self.rear  = (self.rear+1) % self.limit
            self.Q[self.rear] = data

    def delete_queue(self):
        if self.front == -1:
            # print("empty")
            return None

        elif self.front == self.rear:
            a = self.front
            self.front= -1
            self.rear = -1
            return self.Q[a]

        else:
            b = self.front
            self.front = (self.front+1) % self.limit
            return self.Q[b]

    def display(self):
        if self.rear == -1 and self.front == -1:
            print("empty")
            return -1
        elif self.front <= self.rear:
            for i in range(self.front, self.rear+1):
                print(self.Q[i])
        else:
            for i in range(self.front, self.limit):
                print(self.Q[i])

            for i in range(0, self.rear + 1):
                print(self.Q[i])



    def replace(self, data, new_data):
        flag = False
        if self.rear == -1 and self.front == -1:
            print("empty")
        else:
            if self.front< self.rear:
                for i in range(self.front, self.rear + 1):
                    if self.Q[i] == data:
                        self.Q[i] =  new_data
                        flag = True
            elif self.front == self.rear:
                if self.Q[self.front] == data:
                    self.Q[self.front] = new_data
                    flag = True
            elif self.front > self.rear:
                for i in range(self.front, self.limit):
                    if self.Q[i] == data:
                        self.Q[i] = new_data
                        flag = True
                for i in range(0, self.rear+1):
                    if self.Q[i] == data:
                        self.Q[i] =  new_data
                        flag = True
        if not(flag):
            print("Your data not found")
