def gcd(a,b) :
    while b !=0:
        r = a%b
        a = b
        b = r
    return a
print("60과 28의 최대공약수=", gcd(60,28))