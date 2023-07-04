def find_arr(given_arr,element):

    start = 0 
    end = len(given_arr) - 1

    while start <= end:
        mid = int((start + ((end-start)/2)))
        if element == given_arr[mid]:
            print(f"Element found at index position: {mid}")
            break
        elif element < given_arr[mid]:
            start = mid + 1
        elif element > given_arr[mid]:
            end = mid -1

    else:      
        print("Element not Found in the given array")


arr = [10,8,6,4,3,2,1]
find_arr(arr,6)