def counting_sort(A):
    output = [0] * len(A)
    count = [0] * (MAX_VAL + 1) 

    for i in A:
        count[i] += 1

    for i in range(1, MAX_VAL + 1):
        count[i] += count[i - 1]

    for i in range(len(A) - 1, -1, -1): 
        output[count[A[i]] - 1] = A[i]
        count[A[i]] -= 1

    for i in range(len(A)):
        A[i] = output[i]

MAX_VAL = 10
data = [1, 4, 1, 2, 7, 5, 2]
print("Original:", data)
counting_sort(data)
print("Counting:", data)