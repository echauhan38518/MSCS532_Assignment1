def insertion_sort(arr):
    arrSize = len(arr) #initialize and set the length of array
    print( "Size of the array is:" + f"{arrSize}")
    if arrSize <= 1:
        print("The array length is 1 or 0 so return")
        return
    for i in range (1,arrSize): #Iterate over the elements of array starting at index 1
        key = arr[i] #Store the value of current element
        j = i - 1
        while j >= 0 and arr[j] < key: #Move elements to one position ahead if value is less than key
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

customArr = [11,23,44,61,62,17]
insertion_sort(customArr)
print("Elements in the array in decreasing order:")
print(customArr) #display the sorted array 
