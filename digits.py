def binary_digits(n):
    count = 1
    while n > 1:
        count = count +1
        n=n//2
    return count   
s = binary_digits(int(input("숫자 기입")))
print(s)