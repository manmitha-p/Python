def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact
def permutation(n,r):
    return factorial(n)/factorial(n-r)
def combination(n,r):
    return permutation(n,r)/factorial(r)
print(permutation(5,1))
print(combination(5,2))