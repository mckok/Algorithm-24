import math
def factorial(n) :
    if n == 1:
        return 1
    else :
        return n *math. factorial(n-1)
    
s=factorial(int(input("숫자를 기입하세요")))
print(s)
    