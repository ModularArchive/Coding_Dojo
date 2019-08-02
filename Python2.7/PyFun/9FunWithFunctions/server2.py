def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
num_array = [3, 6, 8, 10, 67]
print multiply(num_array, 5)
