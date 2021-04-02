#Q-3 : Given a binary array, find the maximum number of consecutive 1s in this array.
#Example : For the given array [0,1,0,1,1,0,1,1,1,0,0,0] the result should be 3.

#Time Complexity is O(n)
#Space Complexity is O(1)

#Traversing the arr from left to right and increase the value of count when arr[i] = 1
# and compare it with the max count of 1's till now and return the largest value.


def no_of_consecutive_ones(arr):
    result =0
    count = 0

    if len(arr) == 0:
        return 0

    for i in range(0, len(arr)):
        if arr[i] == 0:
            count = 0
        else:
            count += 1
            result = max(result, count)

    return result

if __name__ == '__main__':
    arr = [0,1,0,1,1,0,1,1,1,0,0,0]
    print("Input array:",arr)
    result = no_of_consecutive_ones(arr)
    if result == 0:
        print("There are no 1s present in the array")
    else:
        print("The number of 1s present in the array is:",result)