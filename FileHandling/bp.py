def largestArea(arr1, n, arr2, m):
     
    # Initialize variables
    end = 0
    start = 0
    i = 0
    j = 0
 
    # Sort array arr1[]
    arr1.sort(reverse = False)
 
    # Sort array arr2[]
    arr2.sort(reverse = False)
 
    # Traverse arr1[] and arr2[]
    while (i < n and j < m):
         
        # If arr1[i] is same as arr2[j]
        if (arr1[i] == arr2[j]):
             
            # If no starting point
            # is found yet
            if (start == 0):
                start = arr1[i]
            else:
                 
                # Update maximum end
                end = arr1[i]
                 
            i += 1
            j += 1
 
        # If arr[i] > arr2[j]
        elif (arr1[i] > arr2[j]):
            j += 1
        else:
            i += 1
 
    # If no rectangle is found
    if (end == 0 or start == 0):
        return 0
    else:
         
        # Return the area
        return (end - start)
 
# Driver Code
if __name__ == '__main__':
     
    # Given point
    arr1 = [ 1, 2, 4 ]
 
    # Given length
    N = len(arr1)
 
    # Given points
    arr2 = [ 1, 3, 4 ]
 
    # Given length
    M =  len(arr2)
 
    # Function Call
    print(largestArea(arr1, N, arr2, M))
 
# This code is contributed by ipg2016107