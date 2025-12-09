'''Mutable, can store different types of data types'''
import sys

lst = []
prev_size = sys.getsizeof(lst)
print(f"Initial size: {prev_size} bytes")
og_id = id(lst)
for i in range(1, 10_000_000):
    og_id = id(lst)
    lst.append(i)
    new_size = sys.getsizeof(lst)
    new_id = id(lst)
    if new_size != prev_size:  # Detect resizing
        print(f"List resized after adding {i+1} elements: {new_size} bytes")
        prev_size = new_size
        print(f"Id same: {og_id == new_id}")