def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [2, 3, 5,1]
bubblesort(arr)
print("The sorted order is: ")
for i in range(len(arr)):
    print(arr[i])