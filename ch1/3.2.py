def sequential_search(A, key):
    for i in range(len(A)) :
        if A[i] == key :
            return i
    return -1
list = [4, 5, 7, 8, 10]
s=int(input("정수를 입력하시오"))
number=sequential_search(list,s)
print(number)