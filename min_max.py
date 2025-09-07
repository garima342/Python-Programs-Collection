array =[]
array_size = int(input("Enter the number of elements in the array: "))
for i in range(array_size):
    element = int(input("Enter the elements of the array:"))
    array.append(element)
min = array[0]
max = array[0]
for i in range (len(array)):
    if array[i]<min:
        min = array[i]
    elif array[i]>max:
        max = array[i]
print(min, " ", max)