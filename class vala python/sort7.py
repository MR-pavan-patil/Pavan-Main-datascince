def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot= arr[0]
        less_than_pivot=[x for x in arr[1:]if x<= pivot]
        greater_than_pivot=[x for x in arr[1:]if x>= pivot]
        return quick_sort(less_than_pivot)+[pivot]+quick_sort(greater_than_pivot)
    
    if __name__ =="__main__":
        unsorted_list=[9,7,5,11,12,2,14,3,10,6]
        sorted_list=quick_sort(unsorted_list)
        print("sorted list :",sorted_list)


