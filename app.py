# O(1)

def worker(arr, index):
    return arr[index]

arr = [1, 2, 3, 4, 5]
index = 2
print(worker(arr, index))  

# O(n)

def sum(arr):
    total = 0
    for element in arr:
        total += element
    return total

arr = [1, 2, 3, 4, 5]
print(sum(arr)) 

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

arr = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 8
result = binary_search(arr, target)
if result != -1:
    print(f"عنصر {target} در شاخص {result} پیدا شد.")
else:
    print(f"عنصر {target} پیدا نشد.")

# %%

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

arr = [38, 27, 43, 3, 9, 82, 10]
print("آرایه قبل از مرتب‌سازی:", arr)
merge_sort(arr)
print("آرایه بعد از مرتب‌سازی:", arr)

################################################################
# %%
class Stack:
    def __init__(self, limit=100):
        self.Stack=[]
        self.limit= limit
    
    def push(self, data):
        if len(self.Stack)>=self.limit:
            return -1
        else:
            self.Stack.append(data)

    def pop(self):
        if len(self.Stack)<=self.limit:
            return -1
        else:
            self.Stack.pop()

##################################################################
