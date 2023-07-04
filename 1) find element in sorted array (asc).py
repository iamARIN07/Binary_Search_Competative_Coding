arr = [1,2,3,4,5,6,7,8,9,10]

# linear search
# i = 0
# element = 2
# while i < 10:
#     if arr[i] == 4 :
#         print(arr[i])
#         print("FOUND")
#         break
        
#     else:
#         print("Not found")

#     i = i+1
#     print(i)



def find_arr(given_arr,element):

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

find_arr(arr,10)



