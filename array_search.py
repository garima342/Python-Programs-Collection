array = []
array_size = int(input("Enter the number of elements in the array: "))
for i in range(array_size):
    element = int(input(f"Enter element {i + 1}: "))
    array.append(element)
    
target = int(input("Enter a number to search for: "))
for i in range (len(array)):
    if array[i] == target:
        print(f"Element found at index {i}")
        break
else:
    print("Element not found!")
