def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    
    if(pos+1 == left+k):
        return A[pos]
    elif (pos+1 > left+k):
        return quick_select(A, left, pos-1, k)
    else :
        return quick_select(A, pos+1, right, k-(pos+1-left))
array = [12, 3, 5, 7, 4, 19, 26, 23, 15]
print("입력 리스트 =", array)
print("[정렬기법] 3번째 작은 수: ", kth_smallest_sort(array, 3))
print("[정렬기법] 6번째 작은 수: ", kth_smallest_sort(array, 6))
n = len(array)
print("[축소정복] 3번째 작은 수: ", quick_select(array, 0, n-1, 3))
print("[축소정복] 6번째 작은 수: ", quick_select(array, 0, n-1, 6))