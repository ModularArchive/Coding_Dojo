def odd_even():
    for x in range(1, 2001):
        if x % 2 == 0: 
            print x, "This is an even number"
        else:
            print x,  "This is an odd number"
odd_even()

def multiply(arr, num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
num_array = [3, 6, 8, 10, 67]
print multiply(num_array, 5)


def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for x in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x

# I managed to get it to work by having all of the files together
#However I would like to get it to work with the multiply option not involving the other code files, what can I do to get such a result?