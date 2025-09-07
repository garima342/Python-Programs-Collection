#1. Array ka size even hoga
#2. Array ko traverse krnge n/2 tk
#3. left side ka sum nikalenge, aur voh right side ke sum ke equal hona chaihye balanced hone ke liye
#4. unbalanced hua toh leftside ka sum - rightside ka sum return kr denge, ki ye number add hoga

arr = [1,5,3,2]
n= len(arr)
leftsum = 0
rightsum = 0
if(n%2==0):
    for i in range (n//2):
        leftsum += arr[i]
        rightsum += arr[n-i-1]
    if leftsum==rightsum:
        print("Array is balanced")
        print("Sum of left side is:", leftsum)
        print("Sum of right side is:", rightsum)
    else:
        print("Array seems to be unbalanced")
        arrbal = abs(leftsum-rightsum)
        print("Add", arrbal, "to balance the array")
