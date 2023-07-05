'''
Find the 1st or last occurance of an element in an sorted array
'''

def bin_search_first_4(given_arr,element):

    start = 0 
    end = len(given_arr) - 1
    result = None
    while start <= end:
        mid = int((start + ((end-start)/2)))
        if element == given_arr[mid]:
            result = mid
            end = mid-1 
        elif element < given_arr[mid]:
            end = mid - 1
        elif element > given_arr[mid]:
            start = mid + 1
      
    return result
    
def bin_search_last_4(given_arr,element):

    start = 0 
    end = len(given_arr) - 1
    result = None

    while start <= end:
        mid = int((start + ((end-start)/2)))
        if element == given_arr[mid]:
            result = mid
            start = mid+1            
        elif element < given_arr[mid]:
            end = mid - 1
        elif element > given_arr[mid]:
            start = mid + 1      

    return result

# run    
arr = [2,3,4,6,7,8,10,10,10]

first_occ = bin_search_first_4(arr,10)
last_occ = bin_search_last_4(arr,10)

print(last_occ)
print(first_occ)
    


    