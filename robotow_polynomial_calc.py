import math

def J(k,x):
    return (2**(k+1)-(-1)**(k+1) + (6*(-1)**(k+1))*x )/(3*(2**k))

def P(n,x):
    if n == 1:
        return (1-2*x)/2
    res = 1
    for i in range(2*n-2):
        # print(i+1)
        res *= J(i+1,x)
    res *= (1-J(2*n-1,x))
    return res

def sum_p(iter,x):
    res = 0
    for j in range(iter):
        res += P(j+1,x)
    return res

def find_root(lower, upper):
    mid = (lower+upper)/2
    res = sum_p(100,mid)
    epsilon = 10**(-15)
    while abs(res-0.5) > epsilon:
        if res-0.5 > 0:
            lower = mid
            mid = (lower + upper)/2
            res = sum_p(100,mid)
            print("Current: " + str(res))
        else:
            upper = mid
            mid = (lower+upper)/2
            res = sum_p(100,mid)
            print("Current: " + str(res))
    print(mid)
    print(res)

def find_root(lower, upper):
    mid = (lower+upper)/2
    res = sum_p(100,mid)
    epsilon = 10**(-15)
    while abs(res-0.5) > epsilon:
        if res-0.5 > 0:
            lower = mid
            mid = (lower + upper)/2
            res = sum_p(100,mid)
            print("Current: " + str(res))
        else:
            upper = mid
            mid = (lower+upper)/2
            res = sum_p(100,mid)
            print("Current: " + str(res))
    print(mid)
    print(res)


# print(J(1,1)*J(2,1)*(1-J(3,1)))
# print(P(3,0.5))
# find_root(0.25,0.30)
# print(sum_p(500,0.273068366561617))
# print(sum_p(3,0.25))
print(sum_p(500,0))
