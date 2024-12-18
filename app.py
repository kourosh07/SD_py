################################################################################################################################################

# O(1)

def worker(arr, index):
    return arr[index]

################################################################################################################################################

# O(n)

def sum(arr):
    total = 0
    for element in arr:
        total += element
    return total
    
################################################################################################################################################

# O(log(n))

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1  

################################################################################################################################################

# O(nlog(n))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        
        left_half = arr[:mid]
        right_half = arr[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
        
        i = j = k = 0
        
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    
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

################################################################################################################################################

# برعکس کردن استک  بوسیله صف    

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
        for i in self.stack[::-1]:
            print(i)

    def is_empty(self):
        return len(self.stack) == 0
    
    def __len__(self):
        return len(self.stack)
    
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

def reverse_data(stack: Stack):
    Q = Cqueue()
    n_stack = Stack()
    while not (stack.is_empty()):
        Q.insert_queue(stack.pop())
        
    while Q.front != -1:
        n_stack.push(Q.delete_queue())

    n_stack.show()
         
################################################################################################################################################

# برعکس کردن صف بوسیله استک

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

def reverse_data(Q:Cqueue):
    new_Q = Cqueue()     
    stack = Stack()

    while Q.front != -1:
        stack.push(Q.delete_queue())
    
    while not(stack.is_empty()):
        new_Q.insert_queue(stack.pop())
    new_Q.display()

################################################################################################################################################

# توابع بازگشتی     

# محسبه فاکتوریل
def calc_fac(n):
    pass
    if n == 1:
        return 1
    else:
        return n * calc_fac(n-1)


def fibo(n):
    if n < 2:
        return n

    else:
        return fibo(n-1) + fibo(n-2)


def sum_num(a, b):
    if b == 0:
        return a
    else:
        return sum_num(a, b-1) + 1


def multi_num(a, b):
    if b == 0:
        return 0
    else:
        return multi_num(a, b-1) + a


def divi(a, b):
    if a < b:
        return 0
    else:
        return divi(a-b, b) + 1


# Hannoi Tower
def Hannoi(n, A, B, C):
    if n == (1):
        print(A, 'to', C)
    else:
        Hannoi(n-1, A, C, B)
        print(A, 'to', C)
        Hannoi(n-1, B, A, C)
        
################################################################################################################################################

# لیست پیوندی

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_first(self, x):
        a = Node(x)
        a.next = self.head
        self.head = a

    def insert_last(self, x):
        a = Node(x)
        if self.head == None:
            self.head = a
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = a

    def insert_after(self, x, data):  # insert after x
        if self.head is None:
            return
        elif self.head.next is None:
            if self.head.data == x:
                a = Node(data)
                self.head.next = a
            else:
                return None
        temp = self.head
        a = Node(data)
        while temp.data != x:
            if temp.next is None:
                print("not found")
                return
            temp = temp.next
        a.next = temp.next
        temp.next = a

    def delete_first(self):
        if self.head is None:
            print("empty")
            return
        self.head = self.head.next

    def delete_last(self):
        if self.head is None:
            print("empty")
            return
        elif self.head.next is None:
            self.head = None
            return

        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def delete_after(self, x):
        if self.head is None:  # check if empty
            print("empty")
            return
        elif not (self.head.next):  # check if only one object
            return
        temp = self.head
        while temp.data != x:
            if temp.next is None:  # check if x is not available
                return
            temp = temp.next
        if temp.next:  # check if x is the last object
            temp.next = temp.next.next

    def delete(self, x):
        if self.head is None:  # check if empty
            print("empty")
            return
        
        elif self.head.data == x:
            self.head = self.head.next
            print("done")
            return None

        elif self.head.next is None:
            return

        temp = self.head
        while temp.next.data != x:
            if temp.next.next is None:
                return
            temp = temp.next
        temp.next = temp.next.next

# add replace method to class
    def replace(self, old_data, new_data):
        if self.head is None:
            print("empty")
            return
    
        elif self.head.data == old_data:
            self.head.data = new_data
        
        temp = self.head
        while temp.data != old_data:
            if temp.next is None:
                print("your data not found!")
                return
            temp = temp.next
        temp.data = new_data

################################################################################################################################################

# لیست پیوندی حلقوی

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        a = Node(data)
        if self.head is None:
            self.head = a
            a.next = self.head 
            return
        
        a.next = self.head
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = a
        self.head = a

    def insert_last(self, data):
        a = Node(data)
        
        if self.head is None:
            self.head = a
            a.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = a
        a.next = self.head

    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return
        
        temp = self.head
        while temp.data != x:
            if temp.next == self.head:
                print("your data not found")
                return
            temp = temp.next
            
        a = Node(data)
        a.next = temp.next
        temp.next = a

    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next == self.head:
            del (self.head)
            self.head = None
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            
        temp.next = temp.next.next
        del(self.head)
        self.head = temp.next

    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return None

        temp = self.head
        while temp.next.next != self.head:
            temp = temp.next
        del(temp.next)
        temp.next = self.head

    def delete_after(self, x):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next == self.head:
                print("your data not found")
                return
            temp = temp.next
        t = temp.next
        temp.next = t.next
        del(t)

    def delete(self, x):
        if self.head is None:
            print("empty")
            return None

        elif self.head.next == self.head:
            if self.head.data == x:
                del(self.head)
                self.head = None
                return
            else:
                print("your data not found")
                return
            
        temp = self.head
        while temp.next.data != x:
            if temp.next == self.head:
                print("your data not found")
                return None
            temp = temp.next
            
        t = temp.next
        temp.next = t.next
        del(t)

#  write replace method
    def replace(self, old_data, new_data):
        if self.head is None:
            print("empty")
            return None
        temp = self.head
        while temp.data != old_data:
            if temp.next == self.head:
                print("your data not found")
                return None
            temp = temp.next
        temp.data = new_data

################################################################################################################################################

# لیست پیوندی دو طرفه

class dNode:
    def __init__(self, data):
        self.back = None
        self.data = data
        self.next = None
        
class dLinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            return
        
        a.next = self.head
        a.next.back = a
        self.head = a

    def insert_last(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            return
    
        temp = self.head
        while temp.next != None:
            temp = temp.next
        temp.next = a
        a.back = temp

    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        a = dNode(data)
        if temp.next:
            a.next = temp.next
            temp.next = a
            a.back = temp
            a.next.back = a
        else:
            temp.next = a
            a.back = temp

    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next is None:
            del(self.head)
            self.head = None
            return None
        
        temp = self.head
        self.head = self.head.next
        self.head.back = None
        del(temp)

    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        
        temp = self.head
        while temp.next != None:
            temp = temp.next
            
        temp.back.next = None
        del(temp)

    def delete_after(self, x):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next is None:
            return
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        temp.next = temp.next.next
        a = temp.next.back
        temp.next.back = temp
        del(a)

    def delete(self, x):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.data == x:
            a = self.head
            self.head = a.next
            self.head.back = None
            del(a)
            return None
        
        temp = self.head
        while temp.data != x:
            if temp.next is None:
                print("your data not found")
                return None
            temp = temp.next
            
        if temp.next is None:
            temp.back.next = None
            del(temp)
        else:
            temp.back.next = temp.next
            temp.next.back = temp.back
            del(temp)
            
    def show(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            print(self.head.data)
            return
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.data)
                temp = temp.next

################################################################################################################################################

# لیست پیوندی دو طرفه حلقوی

class dNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

class CdLinekd_list:
    def __init__(self):
        self.head = None
    
    def insert_first(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            self.head.next = self.head
            self.head.back = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            a.next = temp.next
            temp.next.back = a
            temp.next = a
            a.back = temp
            self.head = a
    
    def insert_last(self, data):
        a = dNode(data)
        if self.head is None:
            self.head = a
            self.head.next = self.head
            self.head.back = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            a.next = self.head
            self.head.back = a
            temp.next = a 
            a.back = temp
            
    def insert_after(self, x, data):
        if self.head is None:
            print("empty")
            return None
        else:
            temp = self.head
            while temp.data != x:
                if temp.next == self.head:
                    print("your data not found")
                    return None
                else:
                    temp = temp.next
            a = dNode(data)
            a.next = temp.next
            temp.next.back = a 
            temp.next = a
            a.back = temp
        
    def delete_first(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = temp.next.next
            temp.next.back = temp
            del(self.head)
            self.head = temp.next
            
    
    def delete_last(self):
        if self.head is None:
            print("empty")
            return None
        elif self.head.next == self.head:
            del(self.head)
            self.head = None
            return
        else:
            temp = self.head
            
            while temp.next.next != self.head:
                temp = temp.next
            del(temp.next)
            temp.next = self.head
            self.head.back = temp
    
    
    def delete_after(self, x):
        if self.head is None:
            print("empty")
            return None
        temp = self.head
        while temp.data != x:
            if temp.next == self.head:
                print("your data not found")
                return
            temp = temp.next
        t = temp.next
        temp.next = t.next
        t.next.back = temp
        del(t)
    
    def delete(self, x):
        if self.head is None:
            print("empty")
            return None
        
        elif self.head.next == self.head:
            if self.head.data == x:
                del(self.head)
                self.head = None
                return
        else:
            temp = self.head
            while temp.next.data != x:
                if temp.next == self.head:
                    print("your data not found")
                    return None
                temp = temp.next
            t = temp.next
            temp.next = t.next
            t.next.back = temp
            del(t)
                
    def show(self):
        if self.head is None:
            print("empty")
            return None
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.daat)
                temp = temp.next

################################################################################################################################################

# کلاس درخت باینری

class bnode:
    def __init__(self,d):
        self.Lchild = None
        self.data = d
        self.Rchild = None

class btree:
    def __init__(self):
        self.root = None

    def insLeft(self,d):
        if self.root is None:  #شرط خالی بودن
            self.root = bnode(d) #در نظر گرفتن به عنوان ریشه در صورت خالی بودن
        else:
            temp = self.root # کپی از ریشه
            while temp.Lchild: #حرکت تا چپ ترین خانه
                temp = temp.Lchild
            temp.Lchild = bnode(d) # اضافه کردن فرزند چپ به چپ ترین خانه

    def insRight(self,d):
        if self.root: #شرط خالی نبودن
            temp = self.root
            while temp.Rchild: #حرکت تا راست ترین خانه
                temp = temp.Rchild
            temp.Rchild = bnode(d) # اضافه کردن فرزند راست به راست ترین خانه
        else:
            self.root = bnode(d) #در نظر گرفتن به عنوان ریشه در صورت خالی بودن

    def displayNLR(self): # Node-Left-Right نمایش با ترتیب
        self.showNLR(self.root) #صدا زدن متد کمکی
        
    def showNLR(self,root):
        if root: #شرط خالی نبودن
            print(root.data,end=" ") #چاپ ریشه

            self.showLNR(root.Lchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند چپ به عنوان ریشه

            self.showLNR(root.Rchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند راست به عنوان ریشه


    def displayLNR(self): #Left-Node-Right نمایش با ترتیب
        self.showLNR(self.root) #صدا زدن متد کمکی
        
    def showLNR(self,root): #متد کمکی
        if root: #شرط خالی نبودن
            self.showLNR(root.Lchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند چپ به عنوان ریشه

            print(root.data,end=" ") #چاپ ریشه

            self.showLNR(root.Rchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند راست به عنوان ریشه


    def displayLRN(self): #Left-Right_Node نمایش با ترتیب
        self.showLRN(self.root) #صدا زدن متد کمکی
        
    def showLRN(self,node): #متد کمکی
        if node: #شرط خالی نبودن
            self.showLRN(node.Lchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند چپ به عنوان ریشه

            self.showLRN(node.Rchild) #تابع بازگشتی با در نظر گرفتن 
                                      #فرزند راست به عنوان ریشه
            print(node.data,end = ' ') #چاپ ریشه

    def levelOrder(self): #Level نمایش با ترتیب
        list = [] # ایجاد لیست
        temp = self.root # کپی از ریشه
        if temp is None: # شرط خالی بودن
            return
        list.append(temp) #اضافه کردن ریشه به لیست
        while list: #شرط خالی نبودن لیست
            k = list.pop(0) #برداشتن اولین ایتم لیست
            print(k.data,end = ' ') #چاپ ایتم
            
            if k.Lchild: #شرط وجود داشتن فرزند چپ
                list.append(k.Lchild) #اضافه کردن فرزند چپ به لیست
            if k.Rchild: #شرط وجود داشتن فرزند راست
                list.append(k.Rchild) #اضافه کردن فرزند راست به لیست


    def insAfterL(self,x,d): #افزودن فرزند چپ به نود مورد نظر
        self.pinsAfterL(self.root,x,d) # صدا زدن متد کمکی
        
    def pinsAfterL(self,node,x,d): #متد کمکی
        if node: #شرط خالی نبودن
            if node.data == x: #تطابق نود فعلی با نود مورد نظر
                temp = node.Lchild #کپی از فرزند چپ فعلی
                node.Lchild = bnode(d) #قرار دادن داده جدید به عنوان فرزند چپ جدید
                node.Lchild.Lchild = temp # قرار دادن فرزند چپ قبلی به عنوان نوه چپ
            self.pinsAfterL(node.Lchild,x,d) #جستجوی در فرزند های چپ برای رسیدن به نود مورد نظر
            self.pinsAfterL(node.Rchild,x,d) #جستجوی در فرزند های راست برای رسیدن به نود مورد نظر

    def insAfterR(self,x,d): #افزودن فرزند راست  به نود مورد نظر
        self.pinsAfterR(self.root,x,d) # صدا زدن متد کمکی
        
    def pinsAfterR(self,node,x,d): #متد کمکی
        if node: #شرط خالی نبودن
            if node.data == x: #تطابق نود فعلی با نود مورد نظر
                temp = node.Rchild #کپی از فرزند راست  فعلی
                node.Rchild = bnode(d) #قرار دادن داده جدید به عنوان فرزند راست  جدید
                node.Rchild.Rchild = temp # قرار دادن فرزند راست قبلی به عنوان نوه راست
            self.pinsAfterR(node.Rchild,x,d) #جستجوی در فرزند های راست  برای رسیدن به نود مورد نظر
            self.pinsAfterR(node.Lchild,x,d) #جستجوی در فرزند های راست برای رسیدن به نود مورد نظر



    def delLeft(self): #حذف چپ ترین نود
        if self.root is None: #شرط خالی بودن
            return print("empty")
        if self.root.Lchild is None: #شرط عدم وجود فرزند چپ
            temp = self.root.Rchild # کپی از فرزند راست
            del self.root #حذف ریشه
            self.root = temp #قرار دادن فرزند راست به عنوان ریشه جدید
            return
        temp = self.root #کپی از ریشه
        while temp.Lchild.Lchild: #حرکت تا یک خانه قبل از چپ ترین نود
            temp = temp.Lchild
        temp1 = temp.Lchild #کپی از چپ ترین نود
        temp.Lchild = None #حذف چپ ترین نود
        del temp1

    def delRight(self): #حذف راست ترین نود
        if self.root is None: #شرط خالی بودن
            return print("empty")
        if self.root.Rchild is None: #شرط عدم وجود فرزند راست 
            temp = self.root.Lchild # کپی از فرزند چپ
            del self.root #حذف ریشه
            self.root = temp #قرار دادن فرزند راست به عنوان ریشه جدید
            return
        temp = self.root #کپی از ریشه
        while temp.Rchild.Rchild: #حرکت تا یک خانه قبل از راست ترین نود
            temp = temp.Rchild
        temp1 = temp.Rchild #کپی از راست ترین نود
        temp.Rchild = None #حذف راست ترین نود
        del temp1

    def delete(self,x): #حذف کل درخت
        self.predel(self.root , x) #صدا زدن متد کمکی
        
    def predel(self,node,x):
        if node is None: #شرط خالی بودن
            return
        if node.data == x: #تطابق داده با ریشه
            self.root = None #حذف ریشه
            del node
            return

################################################################################################################################################

# کلاس جستجوی درخت باینری

class bnode:
    def __init__(self,d):
        self.Lchild = None
        self.data = d
        self.Rchild = None

class BST:
    def __init__(self):
        self.root = None
        self.list = []

    def add(self , x):
        if self.root is None: #empty
            self.root = bnode(x)
            self.list.append(x)
        else:
            self.padd(self.root , x) #صدا زدن متد کمکی
    def padd(self , root , x):
        if x > root: #اگر دیتای جدید از ریشه بزرگتر باشد
            if root.Rchild == None: #چک کردن فرزند راست
                root.Rchild = bnode(x)
                self.list.append(x)

            else:
                self.padd(root.Rchild,x) #اگر پدر فرزند راست داشته باشد بوسیله
                                         #تابع بازگشتی فرزند راستش به عنوان ریشه در 
                                         # نظر گرفته میشود و شروط دوباره چک مبشوند

        if x < root: #اگر دیتای جدید از ریشه کوچکتر باشد
            if root.Lchild is None: #چک کردن فرزند راست
                root.Lchild = bnode(x)
                self.list.append(x) 

            else:
                self.padd(root.Lchild,x)#اگر پدر فرزند چپ داشته باشد بوسیله
                                         #تابع بازگشتی فرزند چپش به عنوان ریشه در 
                                         # نظر گرفته میشود و شروط دوباره چک مبشوند
        return
    
    
    def show(self):
        return self.pshow(self.root) #صدا زدن متد کمکی
    def pshow(self,root):
        if root: #شرط خالی نبودن
            self.pshow(root.Rchild) #تابع بازگشتی با ورودی فرزند راست به عنوان ریشه
            print(root.data, end=' ')#چاپ ریشه فعلی
            self.pshow(root.Lchild) #تابع بازگشتی با ورودی فرزند چپ به عنوان ریشه
        return
    

#  کوییز
# تابعی بنویسید که یک
# BST
# را از ورودی گرفته و لیست مربوط به آن را بازگرداند
def CreateList(Tree):
    print(Tree.list)


# کوییز
# برعکس تابع قبل
def createTree(A):
    Tree = BST()
    for i in A:
        Tree.add(i)
    return Tree

################################################################################################################################################

# Max Heap کلاس 

class MaxHeap:
    def __init__(self):
        self.list = []  # ایجاد یک لیست برای ذخیره عناصر هیپ

    def insert(self, x):
        """افزودن عنصر به هیپ."""
        self.list.append(x)  # افزودن عنصر به انتهای لیست
        self.Heapifydu(len(self.list) - 1)  # متعادل کردن هیپ به سمت بالا

    def Heapifydu(self, n):
        """متعادل کردن هیپ به سمت بالا."""
        p = (n - 1) // 2  # محاسبه اندیس والد
        if p != n:  # چک کردن اینکه والد با خود عنصر متفاوت باشد
            if self.list[n] > self.list[p]:  # اگر مقدار عنصر بزرگ‌تر از والد باشد
                self.list[n], self.list[p] = self.list[p], self.list[n]  # جابجایی عنصر با والد
                self.Heapifydu(p)  # ادامه متعادل‌سازی از موقعیت والد

    def Heapifyud(self, n):
        """متعادل کردن هیپ به سمت پایین."""
        e = 2 * n + 1  # محاسبه اندیس فرزند چپ
        r = 2 * n + 2  # محاسبه اندیس فرزند راست
        if e < len(self.list):  # بررسی اینکه فرزند چپ در محدوده باشد
            if r < len(self.list):  # بررسی اینکه فرزند راست در محدوده باشد
                if self.list[n] < self.list[e] and self.list[r] < self.list[e]:  # چک کردن بزرگ‌ترین فرزند
                    self.list[e], self.list[n] = self.list[n], self.list[e]  # جابجایی با فرزند چپ
                    self.Heapifyud(e)  # ادامه متعادل‌سازی از موقعیت فرزند چپ
                elif self.list[n] < self.list[r] and self.list[r] > self.list[e]:  # بررسی فرزند راست
                    self.list[r], self.list[n] = self.list[n], self.list[r]  # جابجایی با فرزند راست
                    self.Heapifyud(r)  # ادامه متعادل‌سازی از موقعیت فرزند راست
                else:
                    return  # اگر نیازی به جابجایی نبود
            else:
                if self.list[e] > self.list[n]:  # بررسی تنها فرزند چپ
                    self.list[n], self.list[e] = self.list[e], self.list[n]  # جابجایی با فرزند چپ
                    return
                else:
                    return

    def delRoot(self):
        """حذف عنصر ریشه از هیپ."""
        if len(self.list) == 0:  # اگر هیپ خالی باشد
            return
        if len(self.list) == 1:  # اگر هیپ تنها یک عنصر داشته باشد
            self.list.pop()  # حذف تنها عنصر موجود
            return
        e = len(self.list) - 1  # محاسبه اندیس آخرین عنصر
        self.list[e], self.list[0] = self.list[0], self.list[e]  # جابجایی ریشه با آخرین عنصر
        self.list.pop()  # حذف آخرین عنصر که اکنون ریشه است
        self.Heapifyud(0)  # متعادل‌سازی هیپ به سمت پایین از ریشه

    def display(self):
        """نمایش عناصر هیپ."""
        print("عناصر هیپ:", self.list)

    def delete(self, value):
        """حذف عنصر مشخص شده از هیپ."""
        try:
            index = self.list.index(value)  # پیدا کردن اندیس عنصر
            self.list[index] = self.list[-1]  # جایگزینی عنصر با آخرین عنصر
            self.list.pop()  # حذف آخرین عنصر
            if index < len(self.list):
                self.Heapifyud(index)  # متعادل‌سازی به سمت پایین
                self.Heapifydu(index)  # متعادل‌سازی به سمت بالا
        except ValueError:
            print(f"مقدار {value} در هیپ پیدا نشد.")

################################################################################################################################################

# Min Heap کلاس

class MinHeap:
    def __init__(self):
        self.list = []  # ایجاد یک لیست برای ذخیره عناصر هیپ

    def insert(self, x):
        """افزودن عنصر به هیپ."""
        self.list.append(x)  # افزودن عنصر به انتهای لیست
        self.Heapifydu(len(self.list) - 1)  # متعادل کردن هیپ به سمت بالا

    def Heapifydu(self, n):
        """متعادل کردن هیپ به سمت بالا."""
        p = (n - 1) // 2  # محاسبه اندیس والد
        if p != n:  # چک کردن اینکه والد با خود عنصر متفاوت باشد
            if self.list[n] < self.list[p]:  # اگر مقدار عنصر کوچک‌تر از والد باشد
                self.list[n], self.list[p] = self.list[p], self.list[n]  # جابجایی عنصر با والد
                self.Heapifydu(p)  # ادامه متعادل‌سازی از موقعیت والد

    def Heapifyud(self, n):
        """متعادل کردن هیپ به سمت پایین."""
        e = 2 * n + 1  # محاسبه اندیس فرزند چپ
        r = 2 * n + 2  # محاسبه اندیس فرزند راست
        if e < len(self.list):  # بررسی اینکه فرزند چپ در محدوده باشد
            if r < len(self.list):  # بررسی اینکه فرزند راست در محدوده باشد
                if self.list[n] > self.list[e] and self.list[r] > self.list[e]:  # چک کردن کوچک‌ترین فرزند
                    self.list[e], self.list[n] = self.list[n], self.list[e]  # جابجایی با فرزند چپ
                    self.Heapifyud(e)  # ادامه متعادل‌سازی از موقعیت فرزند چپ
                elif self.list[n] > self.list[r] and self.list[r] < self.list[e]:  # بررسی فرزند راست
                    self.list[r], self.list[n] = self.list[n], self.list[r]  # جابجایی با فرزند راست
                    self.Heapifyud(r)  # ادامه متعادل‌سازی از موقعیت فرزند راست
                else:
                    return  # اگر نیازی به جابجایی نبود
            else:
                if self.list[e] < self.list[n]:  # بررسی تنها فرزند چپ
                    self.list[n], self.list[e] = self.list[e], self.list[n]  # جابجایی با فرزند چپ
                    return
                else:
                    return

    def delRoot(self):
        """حذف عنصر ریشه از هیپ."""
        if len(self.list) == 0:  # اگر هیپ خالی باشد
            return
        if len(self.list) == 1:  # اگر هیپ تنها یک عنصر داشته باشد
            self.list.pop()  # حذف تنها عنصر موجود
            return
        e = len(self.list) - 1  # محاسبه اندیس آخرین عنصر
        self.list[e], self.list[0] = self.list[0], self.list[e]  # جابجایی ریشه با آخرین عنصر
        self.list.pop()  # حذف آخرین عنصر که اکنون ریشه است
        self.Heapifyud(0)  # متعادل‌سازی هیپ به سمت پایین از ریشه

    def display(self):
        """نمایش عناصر هیپ."""
        print("عناصر هیپ:", self.list)

    def delete(self, value):
        """حذف عنصر مشخص شده از هیپ."""
        try:
            index = self.list.index(value)  # پیدا کردن اندیس عنصر
            self.list[index] = self.list[-1]  # جایگزینی عنصر با آخرین عنصر
            self.list.pop()  # حذف آخرین عنصر
            if index < len(self.list):
                self.Heapifyud(index)  # متعادل‌سازی به سمت پایین
                self.Heapifydu(index)  # متعادل‌سازی به سمت بالا
        except ValueError:
            print(f"مقدار {value} در هیپ پیدا نشد.")

################################################################################################################################################

# کلاس گراف

class Graph:
    def __init__(self, n):
        self.M = [[0] * n for _ in range(n)]  # ایجاد ماتریس n*n برای نگهداری گراف

    def insertEdge(self, s, t):
        """افزودن یال به گراف غیر جهت دار."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = 1  # ایجاد یال از گره s به گره t
            self.M[t][s] = 1  # گراف غیرجهت‌دار: ایجاد یال از گره t به گره s

    def delEdge(self, s, t):
        """حذف یال از گراف غیر جهت دار."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = 0  # حذف یال از گره s به گره t
            self.M[t][s] = 0  # حذف یال از گره t به گره s

    def countEdge(self):
        """شمارش تعداد یال‌ها در گراف."""
        c = 0  # شمارنده تعداد یال‌ها
        for i in range(len(self.M[0])):  # بررسی هر گره
            c = sum(self.M[i]) + c  # جمع کردن یال‌های مربوط به گره‌ها
        c = c / 2  # چون گراف غیر جهت‌دار است، باید تعداد یال‌ها را نصف کنیم
        if c / 2 != 0:
            c += 0.5  # اطمینان از تعداد صحیح یال‌ها در صورت نیاز
        print(c)  # نمایش تعداد یال‌ها

    def bfs(self, start):
        """جستجوی عرضی (BFS) در گراف از راس شروع."""
        visited = [False] * len(self.M)  # لیستی برای نشان دادن بازدید شدن گره‌ها
        queue = [start]  # صف برای ذخیره گره‌ها در طی جستجو
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print("مسیر BFS:", end=" ")  # نمایش عنوان مسیر
        while queue:  # تا زمانی که صف خالی نباشد
            node = queue.pop(0)  # گره اول صف را بردار
            print(node, end=" ")  # نمایش گره فعلی
            for i in range(len(self.M[node])):  # بررسی تمام گره‌های متصل به گره فعلی
                if self.M[node][i] == 1 and not visited[i]:  # اگر یالی بین گره‌ها باشد و گره هنوز بازدید نشده باشد
                    queue.append(i)  # افزودن گره به صف
                    visited[i] = True  # علامت‌گذاری گره به عنوان بازدید شده
        print()  # خط جدید پس از اتمام جستجو

    def dfs(self, start):
        """جستجوی عمقی (DFS) در گراف از راس شروع."""
        print(start, end=" ")  # نمایش گره فعلی
        # تغییر مقدار گره به 2 برای نشان دادن اینکه بازدید شده
        self.M[start][start] = 2
        for i in range(len(self.M[start])):  # بررسی تمام گره‌های متصل به گره فعلی
            if self.M[start][i] == 1 and self.M[i][i] != 2:  # اگر یالی بین گره‌ها باشد و گره هنوز بازدید نشده باشد
                self.dfs(i)  # فراخوانی تابع DFS برای گره بعدی

    def display(self):
        """نمایش گراف به صورت ماتریس adjacency."""
        print("ماتریس گراف غیر جهت دار:")
        for row in self.M:
            print(row)

################################################################################################################################################

# کلاس گراف جهت دار

class GraphD:  # گراف جهت دار
    def __init__(self, n):
        self.M = [[0] * n for _ in range(n)]  # ایجاد ماتریس n*n برای نگهداری گراف جهت دار

    def insertEdge(self, s, t):
        """افزودن یال به گراف جهت دار."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = 1  # ایجاد یال از گره s به گره t

    def delEdge(self, s, t):
        """حذف یال از گراف جهت دار."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = 0  # حذف یال از گره s به گره t

    def bfs(self, start):
        """جستجوی عرضی (BFS) در گراف جهت دار."""
        visited = [False] * len(self.M)  # لیستی برای نشان دادن بازدید شدن گره‌ها
        queue = [start]  # صف برای ذخیره گره‌ها در طی جستجو
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print("مسیر BFS:", end=" ")  # نمایش عنوان مسیر
        while queue:  # تا زمانی که صف خالی نباشد
            node = queue.pop(0)  # گره اول صف را بردار
            print(node, end=" ")  # نمایش گره فعلی
            for i in range(len(self.M[node])):  # بررسی تمام گره‌های متصل به گره فعلی
                if self.M[node][i] == 1 and not visited[i]:  # اگر یالی بین گره‌ها باشد و گره هنوز بازدید نشده باشد
                    queue.append(i)  # افزودن گره به صف
                    visited[i] = True  # علامت‌گذاری گره به عنوان بازدید شده
        print()  # خط جدید پس از اتمام جستجو

    def dfs(self, start):
        """جستجوی عمقی (DFS) در گراف جهت دار."""
        print(start, end=" ")  # نمایش گره فعلی
        # تغییر مقدار گره به 2 برای نشان دادن اینکه بازدید شده
        self.M[start][start] = 2
        for i in range(len(self.M[start])):  # بررسی تمام گره‌های متصل به گره فعلی
            if self.M[start][i] == 1 and self.M[i][i] != 2:  # اگر یالی بین گره‌ها باشد و گره هنوز بازدید نشده باشد
                self.dfs(i)  # فراخوانی تابع DFS برای گره بعدی

    def display(self):
        """نمایش گراف به صورت ماتریس adjacency."""
        print("ماتریس گراف جهت دار:")
        for row in self.M:
            print(row)

################################################################################################################################################

# کلاس گراف وزن دار

class GraphW:  # گراف وزن دار
    def __init__(self, n):
        self.M = [[0] * n for _ in range(n)]  # ایجاد ماتریس n*n برای نگهداری گراف وزن دار

    def insertEdge(self, s, t, w):
        """افزودن یال وزن دار به گراف."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = w  # قرار دادن وزن یال در خانه مربوطه

    def delEdge(self, s, t):
        """حذف یال از گراف وزن دار."""
        if s < len(self.M[0]) and t < len(self.M[0]):  # بررسی اینکه ایندکس‌ها معتبر هستند
            self.M[s][t] = 0  # حذف یال از گره s به گره t
            self.M[t][s] = 0  # حذف یال از گره t به گره s (برای گراف غیرجهت‌دار)

    def bfs(self, start):
        """جستجوی عرضی (BFS) در گراف وزن دار."""
        visited = [False] * len(self.M)  # لیستی برای نشان دادن بازدید شدن گره‌ها
        queue = [start]  # صف برای ذخیره گره‌ها در طی جستجو
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print("مسیر BFS:", end=" ")  # نمایش عنوان مسیر
        while queue:  # تا زمانی که صف خالی نباشد
            node = queue.pop(0)  # گره اول صف را بردار
            print(node, end=" ")  # نمایش گره فعلی
            for i in range(len(self.M[node])):  # بررسی تمام گره‌های متصل به گره فعلی
                if self.M[node][i] > 0 and not visited[i]:  # اگر وزن یال مثبت باشد و گره هنوز بازدید نشده باشد
                    queue.append(i)  # افزودن گره به صف
                    visited[i] = True  # علامت‌گذاری گره به عنوان بازدید شده
        print()  # خط جدید پس از اتمام جستجو

    def dfs(self, start):
        """جستجوی عمقی (DFS) در گراف وزن دار."""
        print(start, end=" ")  # نمایش گره فعلی
        # تغییر مقدار گره به 2 برای نشان دادن اینکه بازدید شده
        self.M[start][start] = 2
        for i in range(len(self.M[start])):  # بررسی تمام گره‌های متصل به گره فعلی
            if self.M[start][i] > 0 and self.M[i][i] != 2:  # اگر وزن یال مثبت باشد و گره هنوز بازدید نشده باشد
                self.dfs(i)  # فراخوانی تابع DFS برای گره بعدی

    def display(self):
        """نمایش گراف به صورت ماتریس adjacency (وزن‌دار)."""
        print("ماتریس گراف وزن دار:")
        for row in self.M:
            print(row)

################################################################################################################################################

# کلاس گراف جهت دار و وزن دار

class GraphDW:  
    def __init__(self, n):
        # ایجاد ماتریس adjacency برای گراف جهت‌دار و وزن‌دار با ابعاد n*n
        self.M = [[0] * n for _ in range(n)]

    def insertEdge(self, s, t, w=1):
        """افزودن یال وزن‌دار به گراف جهت‌دار."""
        if s < len(self.M) and t < len(self.M):
            self.M[s][t] = w  # اضافه کردن وزن یال از گره s به گره t

    def delEdge(self, s, t):
        """حذف یال از گراف جهت‌دار."""
        if s < len(self.M) and t < len(self.M):
            self.M[s][t] = 0  # حذف یال از گره s به گره t

    def bfs(self, start):
        """جستجوی عرضی (BFS) در گراف جهت‌دار از راس شروع."""
        visited = [False] * len(self.M)
        queue = [start]
        visited[start] = True
        print("مسیر BFS:", end=" ")

        while queue:
            node = queue.pop(0)  # گره اول صف را خارج می‌کنیم
            print(node, end=" ")  # نمایش گره فعلی
            for i in range(len(self.M[node])):  # بررسی تمام گره‌های متصل به گره فعلی
                if self.M[node][i] > 0 and not visited[i]:  # اگر یالی وجود داشته باشد و گره بازدید نشده باشد
                    queue.append(i)  # اضافه کردن گره به صف
                    visited[i] = True  # نشان دادن اینکه گره بازدید شده است
        print()

    def dfs(self, start):
        """جستجوی عمقی (DFS) در گراف جهت‌دار از راس شروع بدون استفاده از visited."""
        print(start, end=" ")  # نمایش گره فعلی
        # تغییر مقدار گره به 2 برای نشان دادن اینکه بازدید شده
        self.M[start][start] = 2
        for i in range(len(self.M[start])):  # بررسی تمام گره‌های متصل به گره فعلی
            if self.M[start][i] > 0 and self.M[i][i] != 2:  # اگر یالی بین گره‌ها باشد و گره هنوز بازدید نشده باشد
                self.dfs(i)  # فراخوانی تابع DFS برای گره بعدی

    def display(self):
        """نمایش گراف به صورت ماتریس adjacency (وزن‌دار)."""
        print("ماتریس گراف جهت‌دار و وزن‌دار:")
        for row in self.M:
            print(row)


################################################################################################################################################

# کلاس گراف جهت دار با لیست های مجاورت حلقوی

class GraphD:
    def __init__(self, n):
        """ایجاد گراف با n گره و لیست‌های مجاورت حلقوی."""
        self.n = n  # تعداد گره‌ها
        # لیست مجاورت برای هر گره (لیست‌های حلقوی)
        self.adj_list = [[] for _ in range(n)]
    
    def insertEdge(self, s, t, w=1):
        """افزودن یال از گره s به گره t با وزن w به گراف جهت‌دار."""
        if 0 <= s < self.n and 0 <= t < self.n:  # بررسی اینکه گره‌ها در محدوده باشند
            self.adj_list[s].append((t, w))  # افزودن یال از گره s به گره t با وزن w
    
    def delEdge(self, s, t):
        """حذف یال از گره s به گره t از گراف جهت‌دار."""
        if 0 <= s < self.n and 0 <= t < self.n:  # بررسی اینکه گره‌ها در محدوده باشند
            # حذف یال از لیست مجاورت گره s که به گره t اشاره می‌کند
            self.adj_list[s] = [x for x in self.adj_list[s] if x[0] != t]

    def bfs(self, start):
        """جستجوی عرضی (BFS) از گره start."""
        visited = [False] * self.n  # آرایه visited برای پیگیری گره‌های بازدید شده
        queue = [start]  # صف برای مدیریت گره‌ها
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print("مسیر BFS:", end=" ")

        # اجرای الگوریتم BFS
        while queue:
            node = queue.pop(0)  # خارج کردن گره اول صف
            print(node, end=" ")  # نمایش گره فعلی
            # بررسی همسایگان گره و افزودن آنها به صف
            for neighbor, weight in self.adj_list[node]:
                if not visited[neighbor]:  # اگر گره همسایه بازدید نشده باشد
                    visited[neighbor] = True  # علامت‌گذاری به عنوان بازدید شده
                    queue.append(neighbor)  # افزودن گره همسایه به صف
        print()  # برای چاپ در خط جدید

    def dfs(self, start, visited=None):
        """جستجوی عمقی (DFS) از گره start."""
        if visited is None:
            visited = [False] * self.n  # آرایه visited برای پیگیری گره‌های بازدید شده
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print(start, end=" ")  # نمایش گره فعلی

        # بررسی همسایگان گره و بازگشت به آنها در صورت بازدید نشدن
        for neighbor, weight in self.adj_list[start]:
            if not visited[neighbor]:  # اگر گره همسایه بازدید نشده باشد
                self.dfs(neighbor, visited)  # فراخوانی بازگشتی برای گره همسایه

    def display(self):
        """نمایش گراف به صورت لیست‌های مجاورت حلقوی."""
        print("لیست‌های مجاورت حلقوی گراف:")
        # نمایش لیست مجاورت برای هر گره
        for i in range(self.n):
            # لیست همسایگان هر گره به همراه وزن یال‌ها
            neighbors = [f"{neighbor} (وزن: {weight})" for neighbor, weight in self.adj_list[i]]
            # چاپ گره و همسایگانش
            print(f"گره {i}: {', '.join(neighbors) if neighbors else 'هیچ یالی ندارد'}")
            

################################################################################################################################################

# کلاس گراف جهت دار و وزن دار با لیست های پیوندی حلقوی

class Node:
    def __init__(self, data, weight):
        """ایجاد یک گره جدید با داده و وزن مشخص."""
        self.data = data  # داده (گره همسایه)
        self.weight = weight  # وزن یال
        self.next = None  # پیوند به گره بعدی (که در ابتدا None است)

class GraphDW:
    def __init__(self, n):
        """ایجاد گراف جهت‌دار و وزن‌دار با n گره و لیست‌های پیوندی حلقوی."""
        self.n = n  # تعداد گره‌ها
        self.adj_list = [None] * n  # لیست پیوندی برای هر گره (لیست حلقوی)

    def insertEdge(self, s, t, w=1):
        """افزودن یال از گره s به گره t با وزن w به گراف جهت‌دار و وزن‌دار."""
        if 0 <= s < self.n and 0 <= t < self.n:  # بررسی اینکه گره‌ها در محدوده باشند
            new_node = Node(t, w)  # ایجاد یک گره جدید برای همسایه t با وزن w
            if self.adj_list[s] is None:
                # اگر گره s لیست همسایگان ندارد، گره جدید به لیست اضافه می‌شود
                self.adj_list[s] = new_node
                new_node.next = new_node  # گره جدید خود به خود اشاره کند (حلقوی)
            else:
                # در غیر این صورت، گره جدید به انتهای لیست پیوندی اضافه می‌شود
                current = self.adj_list[s]
                while current.next != self.adj_list[s]:  # پیدا کردن آخرین گره
                    current = current.next
                current.next = new_node
                new_node.next = self.adj_list[s]  # پیوند حلقوی

    def delEdge(self, s, t):
        """حذف یال از گره s به گره t از گراف جهت‌دار و وزن‌دار."""
        if 0 <= s < self.n and 0 <= t < self.n:  # بررسی اینکه گره‌ها در محدوده باشند
            current = self.adj_list[s]
            if current is None:
                return  # اگر گره s هیچ همسایه‌ای نداشته باشد، کاری انجام نمی‌دهیم
            prev = None
            # پیمایش لیست پیوندی تا گره مورد نظر پیدا شود
            while current.data != t:
                prev = current
                current = current.next
                if current == self.adj_list[s]:  # به حلقه رسیدیم و یال پیدا نشد
                    return
            if prev is None:
                # اگر گره اول باشد (همسایه اول)
                if current.next == self.adj_list[s]:
                    # اگر فقط یک گره وجود داشته باشد
                    self.adj_list[s] = None
                else:
                    # اگر چند گره در لیست باشند
                    last = self.adj_list[s]
                    while last.next != self.adj_list[s]:  # پیدا کردن آخرین گره
                        last = last.next
                    self.adj_list[s] = current.next
                    last.next = self.adj_list[s]
            else:
                prev.next = current.next  # حذف یال از لیست پیوندی

    def bfs(self, start):
        """جستجوی عرضی (BFS) از گره start."""
        visited = [False] * self.n  # آرایه visited برای پیگیری گره‌های بازدید شده
        queue = [start]  # صف برای مدیریت گره‌ها
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print("مسیر BFS:", end=" ")

        # اجرای الگوریتم BFS
        while queue:
            node = queue.pop(0)  # خارج کردن گره اول صف
            print(node, end=" ")  # نمایش گره فعلی
            current = self.adj_list[node]
            if current:  # اگر گره همسایگان دارد
                while True:
                    if not visited[current.data]:  # اگر گره همسایه بازدید نشده باشد
                        visited[current.data] = True  # علامت‌گذاری به عنوان بازدید شده
                        queue.append(current.data)  # افزودن گره همسایه به صف
                    current = current.next
                    if current == self.adj_list[node]:  # بازگشت به گره شروع (حلقوی)
                        break
        print()  # برای چاپ در خط جدید

    def dfs(self, start, visited=None):
        """جستجوی عمقی (DFS) از گره start."""
        if visited is None:
            visited = [False] * self.n  # آرایه visited برای پیگیری گره‌های بازدید شده
        visited[start] = True  # علامت‌گذاری گره شروع به عنوان بازدید شده
        print(start, end=" ")  # نمایش گره فعلی

        # پیمایش همسایگان و فراخوانی بازگشتی برای هر همسایه
        current = self.adj_list[start]
        while current:
            if not visited[current.data]:  # اگر گره همسایه بازدید نشده باشد
                self.dfs(current.data, visited)  # فراخوانی بازگشتی برای گره همسایه
            current = current.next
            if current == self.adj_list[start]:  # بازگشت به گره شروع (حلقوی)
                break

    def display(self):
        """نمایش گراف به صورت لیست‌های پیوندی حلقوی."""
        print("لیست‌های پیوندی حلقوی گراف:")
        # نمایش لیست پیوندی برای هر گره
        for i in range(self.n):
            current = self.adj_list[i]
            neighbors = []
            if current:
                while True:
                    neighbors.append(f"{current.data} (وزن: {current.weight})")
                    current = current.next
                    if current == self.adj_list[i]:  # به حلقه رسیدیم
                        break
            print(f"گره {i}: {', '.join(neighbors) if neighbors else 'هیچ یالی ندارد'}")


################################################################################################################################################
