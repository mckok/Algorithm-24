def insertion_sort(A, n):
    for i in range(1, n):
        j = i - 1
        while j >= 0 and A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1


my_list = [7, 4, 9, 6, 3, 8, 7, 5]

list_length = len(my_list)

insertion_sort(my_list, list_length)

print(my_list)