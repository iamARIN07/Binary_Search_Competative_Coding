'''
Order of the sorted array is not mentioned. It can be either asc or desc
'''

# asc
def bin_search_asc(given_arr,element):

    start = 0 
    end = len(given_arr) - 1

    while start <= end:
        mid = int((start + ((end-start)/2)))
        if element == given_arr[mid]:
            print(f"Element found at index position: {mid}")
            break
        elif element < given_arr[mid]:
            end = mid - 1
        elif element > given_arr[mid]:
            start = mid + 1

    else:      
        print("Element not Found in the given array")


# desc
def bin_search_desc(given_arr,element):

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

# main
def bin_search3(arr,element):

    if len(arr) != 1:
        if arr[0] < arr[1]:
            bin_search_asc(arr,element)
        else:
            bin_search_desc(arr,element)

    else:
        if arr[0] == element:
            print("Element matched in size 1 array")
        else:
            print("Element did not match in size 1 array")

# run
arr1 = [2,4,6,8,10,12,14,16,18,20]
arr2 = [10,8,6,4,2] 
arr3 = [2]
element = 10
bin_search3(arr3,element)
    
    


    
