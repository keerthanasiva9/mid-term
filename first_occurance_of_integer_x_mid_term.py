#Given a sorted array ‘nums’ , return the first occurrence of an integer ‘x’.
#Example : For the given array [2,4,4,4,6,7,7,7,8,9,9,9] & x = 7 ,
# the result should be 5.Please note that you should not use a linear search to solve this problem.

#Time Complexity is O(log(n))
#Space Complexity is O(1)

#Used binary search

def first_occurance(arr,k):

    left,right = 0,len(arr)-1

    #Sorting the input array
    arr.sort()

    #return a random negative value if the element is not present in array
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if k == arr[mid]:
            result = mid
            right = mid - 1
        elif k < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return result

if __name__ == '__main__':
    arr = [2,4,4,4,6,7,7,7,8,9,9,9]
    k = 7
    print("Input array:",arr)
    print("The element to be found",k)
    result = first_occurance(arr,k)
    if result == -1:
        print("Element not present in the array")
    else:
        print("The element is present at:",result)