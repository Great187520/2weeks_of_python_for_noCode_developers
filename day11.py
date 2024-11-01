#Data Structures and Algorithms
#list, stacks, queues, linked Lists etc

#Lists
""" my_list = [1, 2, 3, 4, 5]
my_list.append(6) # Add an element
print(my_list) """

#Stacks
""" stack = []
stack.append(1)
stack.append(2)
stack.pop()
 """
#Queue
""" from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()
print(queue) """

#Linked Lists
""" class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
 """
#basic sorting and searching algorithms
#sorting 
#Types Bubble and Merge

""" def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([65, 34, 25, 12, 22, 11, 90])) 
 """

#Merge sort

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
            j +=  1
            k += 1

    return arr

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

#Searching Algorithms
#Types Linear and Binary

""" def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

print(linear_search([10, 20, 30, 40], 30)) """

#Binary search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1

sorted_array = [10, 20, 30, 40, 50]
print(binary_search(sorted_array, 30))

#Time Complexity: Introduction to Big O Notation

def sort_and_search(arr, target):
    sorted_arr = merge_sort(arr)
    print("Sorted Array:", sorted_arr)

    result = binary_search(sorted_arr, target)
    return result

arr = [34, 7, 23, 32, 5, 62]
target = 23
index = sort_and_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")

else:
    print(f"Element {target} not found in the array")