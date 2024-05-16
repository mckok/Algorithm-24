def kth_smallest_sort(A, k):
   A.sort()
   return A[k-1]
A = [3, 5, 7, 9]
print(kth_smallest_sort(A, 3))